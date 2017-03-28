require Integer

defmodule LetsReview do
  def solve(s) do
    even_s = Stream.with_index(String.codepoints(s))
    |> Enum.filter(&(Integer.is_even(elem(&1, 1))))
    |> Enum.map(&(elem(&1, 0)))
    |> Enum.join("")
    odd_s = Stream.with_index(String.codepoints(s))
    |> Enum.filter(&(Integer.is_odd(elem(&1, 1))))
    |> Enum.map(&(elem(&1, 0)))
    |> Enum.join("")

    even_s <> " " <> odd_s
  end

  def main() do
    n = IO.gets("")
    |> String.trim()
    |> Integer.parse()
    |> elem(0)

    inputs = for _ <- 1..n do
      IO.gets("")
      |> String.trim()
    end

    for input <- inputs do
      solve(input)
      |> IO.puts()
    end
  end
end

LetsReview.main()
