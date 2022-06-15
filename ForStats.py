class ForStats():
    def Stat_HP(PokemonBase_HP, PokemonIV2, PokemonEV2, PokemonLevel):
        Hp = (((2 * PokemonBase_HP + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + PokemonLevel + 10
        return Hp

    def OtherStat_Attack(PokemonBase_Attack, PokemonIV2, PokemonEV2, PokemonLevel,PokemonNature):
        Stat_Attack = ((((2 * PokemonBase_Attack + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + 5) * (((2 * PokemonBase_Attack + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + PokemonNature
        return Stat_Attack

    def OtherStat_Defense(PokemonBase_Defense, PokemonIV2, PokemonEV2, PokemonLevel,PokemonNature):
        Stat_Defense = ((((2 * PokemonBase_Defense + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + 5) * (((2 * PokemonBase_Defense + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + PokemonNature
        return Stat_Defense

    def OtherStat_SPAttack(PokemonBase_SPAttack, PokemonIV2, PokemonEV2, PokemonLevel,PokemonNature):
        Stat_SPAttack = ((((2 * PokemonBase_SPAttack + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + 5) * (((2 * PokemonBase_SPAttack + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + PokemonNature
        return Stat_SPAttack

    def OtherStat_SPDefense(PokemonBase_SPDefense, PokemonIV2, PokemonEV2, PokemonLevel,PokemonNature):
        Stat_SPDefense = ((((2 * PokemonBase_SPDefense + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + 5) * (((2 * PokemonBase_SPDefense + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + PokemonNature
        return Stat_SPDefense

    def OtherStat_Speed(PokemonBase_Speed, PokemonIV2, PokemonEV2, PokemonLevel,PokemonNature):
        Stat_Speed = ((((2 * PokemonBase_Speed + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + 5) * (((2 * PokemonBase_Speed + PokemonIV2 + (PokemonEV2/4)) * PokemonLevel)/100) + PokemonNature
        return Stat_Speed