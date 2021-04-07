  (*
  Copyright (c) 2021 STCHEPINSKY Nathan
 
  Permission is hereby granted, free of charge, to any person obtaining a copy of
  this software and associated documentation files (the "Software"), to deal in
  the Software without restriction, including without limitation the rights to
  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
  the Software, and to permit persons to whom the Software is furnished to do so,
  subject to the following conditions:
 
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
 
  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
  FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
  COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
  IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
  CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

*)

type voisin = int list ;; 
type graphe = voisin array ;;

type poids = Inf | P of int ;;

let somme a b = match a,b with
    | Inf,_ -> Inf
    | _,Inf -> Inf
    | (P a),(P b) -> P (a + b);;

let mini a b = match a,b with
    | Inf,x -> x
    | x,Inf -> x
    | (P a),(P b) -> P (min a b);;


let inferieur  a b= match a,b with
    | Inf,_ -> false
    | _,Inf -> true
    | (P a),(P b) -> a < b;;
    
 
let get_weight = function 
	| P a -> a;;


(* tri par selection*)
let rec min_list w current_sommet = function 
		| [e] -> e,[]
		| e::q -> let m, li2 = min_list w current_sommet q in 
										if m <= (get_weight w.(current_sommet).(e)) then
											m,e :: li2
										else
											e,q
		| _ -> failwith "liste vide";;

	
		
let rec tri_selection w current_sommet = function 
	| [] -> []
	| li -> let m,li2 = min_list w current_sommet li in m :: tri_selection w current_sommet li2;;
	
	
let w = [|[|P 0; P 7; P 1|]|]  in tri_selection w 0 [1;2];;



(*parcours_voisins [1;2] [|P 0;Inf;P 10|] [|[|P 0; P 7; P 9|]|] 0;;*)

let drijska_adj voisins mat sommet =
	let nb_sommet = Array.length voisins in
		let smallest_path = Array.make nb_sommet Inf
		and s = Array.make nb_sommet Inf
		and nb_append_S = ref 0
		and current_sommet = ref sommet in
			for i = 0 to nb_sommet - 1 do
				smallest_path.(i) <- mat.(sommet).(i); (* Chemin initiaux*)
			done;
			print_string "\nStart parcours\n";
			while !nb_append_S < nb_sommet do (* ie tant que complmentaire S =\= 0*)
				print_string "\n Visite du sommet : ";
				print_int !nb_append_S;
				print_string "\n";
				s.(!nb_append_S) <- P !current_sommet; (* On m le sommet visite*)
				nb_append_S := !nb_append_S + 1; (* On a ajoute un sommet*)
				print_string "\nStart sorting";
				let sorted_voisins = tri_selection mat !current_sommet voisins.(!current_sommet) in
					print_string "\nSorted\n";
					let rec parcours_voisins voisins = match voisins with (* Modifie d en conc�quence*)
							| [] -> ()
							| e :: q ->
							(*print_int e;
						print_string "\n";print_int (get_weight (somme mat.(!current_sommet).(e) (smallest_path.(!current_sommet))));
									print_string "\n";
									print_int (get_weight smallest_path.(e));*)
										
										if inferieur (somme mat.(!current_sommet).(e) (smallest_path.(!current_sommet))) smallest_path.(e) then (* Si le poids du chemin du sommet actuel jusqu'au voisin + le poids du sommet est plus petit que le point du voisin alors*)
											smallest_path.(e) <- somme mat.(!current_sommet).(e) smallest_path.(!current_sommet);
										parcours_voisins q;
					in parcours_voisins sorted_voisins;
						print_string "Parcours voisins ..... OK\n";
						let rec select_next_voisin = function
								| [] -> print_string "Plus de voisins disponibles ayant eux aussi des voisins"; nb_append_S := nb_sommet (* On provoque la fin de la boucle while*)
								| e :: q when voisins.(e) <> [] -> current_sommet := e (* Bon candidat*)
								| e :: q -> select_next_voisin q (* On continu notre recherche*)
						in select_next_voisin sorted_voisins;
							print_string "Next voisins ..... OK\n";
			done;
			print_string "\n************ DIJKSTRA ALGORITHM SUCCESS************\n\nPoids des plus courts chemins trouvés : \n";
			smallest_path;;
					

let voisin = [| [1; 2]; [3; 5]; [1; 4; 5]; []; [1; 3]; [4] |] ;;
let mat = [|[|P 0; P 7; P 1; Inf; Inf; Inf|];
		[|Inf; P 0; Inf; P 4; Inf; P 1|];
		[|Inf; P 5; P 0; Inf; P 2; P 7|];
		[|Inf; Inf; Inf; P 0; Inf; Inf|];
		[|Inf; P 2; Inf; P 5; P 0; Inf|];
		[|Inf; Inf; Inf; Inf; P 3; P 0|]|];;
		

drijska_adj voisin mat 0;;