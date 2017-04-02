defmodule Recursion do
  def factorial(n) do
    cond do
      n <= 1 -> 1
      true -> n * factorial(n - 1)
    end
  end

  def main() do
    {n, _} = IO.gets("")
    |> Integer.parse()

    IO.puts(factorial(n))
  end
end

Recursion.main()
