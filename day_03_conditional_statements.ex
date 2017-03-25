defmodule ConditionalStatement do
  def solve(n) do
    cond do
      rem(n, 2) == 1 ->
        "Weird"
      2 <= n and n <= 5 ->
        "Not Weird"
      6 <= n and n <= 20 ->
        "Weird"
      20 <= n ->
        "Not Weird"
    end
  end

  def main() do
    {n, _} = Integer.parse(IO.gets(""))

    IO.puts(solve(n))
  end
end

ConditionalStatement.main()
