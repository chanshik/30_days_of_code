defmodule Loops do
  def solve(n) do
    for i <- 1..10 do
      IO.puts("#{n} x #{i} = #{n * i}")
    end
  end

  def main() do
    {n, _} = Integer.parse(IO.gets(""))

    solve(n)
  end
end

Loops.main()
