class ForEV():
    def ForEV_call(Pokemon_Base,PokemonIV2,PokemonEV2,PokemonLevel):
        call = ((2*Pokemon_Base+ PokemonIV2 +(PokemonEV2/4))*PokemonLevel/100)
        return call
    def Need4EV(IncreaseValue, Modifier, call, PokemonLevel):
        NeedEV = ((((IncreaseValue/Modifier)-(call))*400/PokemonLevel)/4)*4
        return NeedEV