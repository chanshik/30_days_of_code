defmodule Arrays do
  def solve(arr) do
    Enum.reverse(arr)
    |> Enum.join(" ")
  end

  def main() do
    n = IO.gets("")
    |> Integer.parse()
    |> elem(0)

    arr = IO.gets("")
    |> String.trim()
    |> String.split(" ")
    |> Enum.map(&(elem(Integer.parse(&1), 0)))

    IO.puts(solve(arr))
  end
end

Arrays.main()
