defmodule Prime do
  @doc """
  Day 25: Running Time and Complexity

  https://www.hackerrank.com/challenges/30-running-time-and-complexity
  """
  def is_prime(1) do
    "Not prime"
  end

  def is_prime(2) do
    "Prime"
  end

  def is_prime(3) do
    "Prime"
  end

  def is_prime(num) do
    bound = round(Float.floor(:math.sqrt(num)))

    try do
      for divisor <- 2..bound do
        if rem(num, divisor) == 0 do
          throw :break
        end
      end

      "Prime"
    catch
      :break -> "Not prime"
    end
  end

  def main() do
    {n, _} = IO.gets("")
    |> Integer.parse()

    for _ <- 1..n do
      {num, _} = IO.gets("")
      |> Integer.parse()

      IO.puts(is_prime(num))
    end
  end
end

Prime.main()
