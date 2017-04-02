defmodule BinaryNumbers do
  use Bitwise

  def solve(n, max_num, nums) when n == 0 do
    Enum.max(nums ++ [max_num])
  end

  def solve(n, max_num, nums) do
    if band(n, 1) == 1 do
      solve(n >>> 1, max_num + 1, nums)
    else
      if max_num > 0 do
        solve(n >>> 1, 0, nums ++ [max_num])
      else
        solve(n >>> 1, 0, nums)
      end
    end
  end

  def main() do
    {n, _} = IO.gets("") |> Integer.parse()

    IO.puts(solve(n, 0, []))
  end
end

BinaryNumbers.main()
