type dist = 
	| Inf
	| P of int;;
	
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
    

type graph = dist array array;;


let floyd_warshall (delta:graph) = 
	let n = (Array.length delta.(0)) in 
		for k = 0 to (n-1) do 
			for i = 0 to (n-1) do
				for j=0 to (n-1) do
					if inferieur (somme (delta.(i).(k)) (delta.(k).(j))) (delta.(i).(j)) then 
						delta.(i).(j) <- somme (delta.(i).(k)) (delta.(k).(j))
				done;
			done;
		done;;