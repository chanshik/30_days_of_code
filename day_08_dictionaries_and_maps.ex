defmodule DictAndMaps do
  def make_dict(entries) do
    dicts = entries
    |> Enum.map(fn (entry) -> %{Enum.at(entry, 0) => Enum.at(entry, 1)} end)
    |> Enum.reduce(%{}, fn (k, acc) -> Map.merge(acc, k) end)
  end

  def query(dicts) do
    case IO.gets("") do
      :eof -> :ok
      {:error, _} -> :ok
      data ->
        q = String.trim(data)

        if Map.has_key?(dicts, q) do
          IO.puts("#{q}=#{dicts[q]}")
        else
          IO.puts("Not found")
        end
        
        query(dicts)
    end
  end

  def main() do
    {n, _} = IO.gets("")
    |> Integer.parse()

    entries = for _ <- 1..n do
      IO.gets("")
      |> String.trim()
      |> String.split()
    end

    dicts = make_dict(entries)
    query(dicts)
  end
end

DictAndMaps.main()
