from django.db import models


class TabelaAgua(models.Model):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=100,
    )

    # Boleanos

    verificacao_efeito_toxico_cronico = models.BooleanField(
        verbose_name='não verificação de efeito tóxico crônico a organismos, de acordo com os critérios estabelecidos pelo órgão ambiental competente ',
        blank=False,
        default=False,        
    )

    verificacao_efeito_toxico_agudo = models.BooleanField(
        verbose_name='não verificação de efeito tóxico agudo a organismos, de acordo com os critérios estabelecidos pelo órgão ambiental competente, ou, na sua ausência, por instituições nacionais ou internacionais renomadas',
        blank=False,
        default=False,        
    )

    materiais_flutuantes = models.BooleanField(
        verbose_name='materiais flutuantes, inclusive espumas não naturais: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    oleos_graxas_virtualmente_ausentes = models.BooleanField(
        verbose_name='óleos e graxas: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    substancias_comuniquem_gosto_odor = models.BooleanField(
        verbose_name='substâncias que comuniquem gosto ou odor: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    corantes_provenientes_fontes_antropicas = models.BooleanField(
        verbose_name='corantes provenientes de fontes antrópicas: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    residuos_solidos_objetaveis = models.BooleanField(
        verbose_name='resíduos sólidos objetáveis: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    cor_verdadeira = models.BooleanField(
        verbose_name='cor verdadeira: nível de cor natural do corpo de água em mg Pt/L',
        blank=False,
        default=False,        
    )

    nao_presenca_corantes = models.BooleanField(
        verbose_name='não tem presença de corantes provenientes de fontes antrópicas que não sejam removíveis por processo de coagulação, sedimentação e filtração convencionais ',
        blank=False,
        default=False,        
    )

    coliformes_termotolerantes_limite_200 = models.BooleanField(
        verbose_name='coliformes termotolerantes: para o uso de recreação de contato primário deverão ser obedecidos os padrões de qualidade de balneabilidade, previstos na Resolução CONAMA n° 274, de 2000. Para os demais usos, não deverá ser excedido um limite de 200 coliformes termotolerantes por 100 mililitros em 80% ou mais, de pelo menos 6 amostras, coletadas durante o período de um ano, com freqüência bimestral.',
        blank=False,
        default=False,        
    )

    coliformes_termotolerantes_limite_1000 = models.BooleanField(
        verbose_name='coliformes termotolerantes: para uso de recreação de contato primário deverá ser obedecida a Resolução CONAMA n° 274, de 2000. Para os demais usos, não deverá ser excedido um limite de 1.000 coliformes termotolerantes por 100 mililitros em 80% ou mais de pelo menos 6 (seis) amostras coletadas durante o período de um ano, com freqüência bimestral.',
        blank=False,
        default=False,        
    )

    coliformes_termotolerantes_limite_2500 = models.BooleanField(
        verbose_name='coliformes termotolerantes: para o uso de recreação de contato secundário não deverá ser excedido um limite de 2500 colif. termotolerantes por 100 mililitros em 80% ou mais de pelo menos 6 amostras, coletadas durante o período de um ano, com freqüência bimestral.',
        blank=False,
        default=False,        
    )

    cianobacterias_dessedentacao_animais = models.BooleanField(
        verbose_name='cianobactérias para dessedentação de animais: os valores de densidade de cianobactérias não deverão exceder 50.000 cel/ml, ou 5mm3/L',
        blank=False,
        default=False,        
    )

    odor_aspecto_nao_objetaveis = models.BooleanField(
        verbose_name='odor e aspecto: não objetáveis',
        blank=False,
        default=False,        
    )

    oleos_graxas_toleram_iridescencias = models.BooleanField(
        verbose_name='óleos e graxas: toleram-se iridescências',
        blank=False,
        default=False,        
    )

    substancias_facilmente_sedimentaveis = models.BooleanField(
        verbose_name='substâncias facilmente sedimentáveis que contribuam para o assoreamento de canais de navegação: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    fenois_totais_C6H5OH = models.BooleanField(
        verbose_name='fenóis totais (substâncias que reagem com 4 - aminoantipirina) até 1,0 mg/L de C6H5OH',
        blank=False,
        default=False,        
    )

    substancias_produzem_odor_turbidez_virtualmente_ausentes = models.BooleanField(
        verbose_name='substâncias que produzem odor e turbidez: virtualmente ausentes',
        blank=False,
        default=False,        
    )

    coliformes_termotolerantes_limite_43_por_100ml = models.BooleanField(
        verbose_name='coliformes termolerantes: para o uso de recreação de contato primário deverá ser obedecida a Resolução CONAMA n° 274, de 2000. Para o cultivo de moluscos bivalves destinados à alimentação humana, a média geométrica da densidade de coliformes termotolerantes, de um mínimo de 15 amostras coletadas no mesmo local, não deverá exceder 43 por 100 mililitros, e o percentil 90% não deverá ultrapassar 88 coliformes termolerantes por 100 mililitros.',
        blank=False,
        default=False,        
    )

    coliformes_termotolerantes_limite_2500_por_100ml = models.BooleanField(
        verbose_name='coliformes termotolerantes: não deverá ser excedido um limite de 2500 por 100 mililitros em 80% ou mais de pelo menos 6 amostras coletadas durante o período de um ano, com freqüência bimestral',
        blank=False,
        default=False,        
    )

    coliformes_termotolerantes_limite_4000 = models.BooleanField(
        verbose_name='coliformes termotolerantes: não deverá ser excedido um limite de 4.000 coliformes termotolerantes por 100 mililitros em 80% ou mais de pelo menos 6 amostras coletadas durante o período de um ano, com freqüência bimestral. ',
        blank=False,
        default=False,        
    )

    ## I - condições de qualidade de água - valores
                                        
    salinidade_agua = models.FloatField(
        verbose_name='salinidade da água em partes por mil (‰) ou g/kg - g/kg',
        blank=False,
        null=True,
    )

    dbo_5_dias_a_20_C = models.FloatField(
        verbose_name='DBO 5 dias a 20°C - mg/L O2',
        blank=False,
        null=True,
    )

    od_qualquer_amostra = models.FloatField(
        verbose_name='OD, em qualquer amostra - mg/L O2',
        blank=False,
        null=True,
    )

    turbidez_unidades_nefelometrica_turbidez= models.FloatField(
        verbose_name='turbidez em unidades nefelométrica de turbidez (UNT) - UNT',
        blank=False,
        null=True,
    )

    ph = models.FloatField(
        verbose_name='Potencial hidrogeniônico (pH) - UNT',
        blank=False,
        null=True,
    )

    cor_verdadeira = models.FloatField(
        verbose_name='cor verdadeira em mg Pt/L - mg Pt/L',
        blank=False,
        null=True,
    )

    clorofila_a = models.FloatField(
        verbose_name='clorofila a em ìg/L - ìg/L',
        blank=False,
        null=True,
    )

    densidade_cianobacterias = models.FloatField(
        verbose_name='densidade de cianobactérias em cel/mL - cel/Ml',
        blank=False,
        null=True,
    )

    carbono_organico_total= models.FloatField(
        verbose_name='carbono orgânico total em mg/L, como C - mg/L',
        blank=False,
        null=True,
    )

    ## Valores

    arsenio_total = models.FloatField(
        verbose_name='Arsênio total - mg/L As',
        blank=False,
        null=True,
    )

    corofila_a = models.FloatField(
        verbose_name='Clorofila a - µg/L',
        blank=False,
        null=True,
    )

    densidade_de_cianobactérias  = models.FloatField(
        verbose_name='Densidade de cianobactérias  - cel/mL',
        blank=False,
        null=True,
    )

    solidos_dissolvidos_totais   = models.FloatField(
        verbose_name='Sólidos dissolvidos totais -  mg/L',
        blank=False,
        null=True,
    )

    aluminio_dissolvido = models.FloatField(
        verbose_name='Alumínio dissolvido - mg/L Al',
        blank=False,
        null=True,
    )

    antimonio  = models.FloatField(
        verbose_name='Antimônio - mg/L Sb',
        blank=False,
        null=True,
    )

    bario_total   = models.FloatField(
        verbose_name='Bário total - mg/L Ba',
        blank=False,
        null=True,
    )

    berilio_total   = models.FloatField(
        verbose_name='Berílio total - mg/L Be',
        blank=False,
        null=True,
    )

    boro_total = models.FloatField(
        verbose_name='Boro total - mg/L B',
        blank=False,
        null=True,
    )

    cadmio_total  = models.FloatField(
        verbose_name='Cádmio total  - mg/L Cd',
        blank=False,
        null=True,
    )

    chumbo_total  = models.FloatField(
        verbose_name='Chumbo total  - mg/L Pb',
        blank=False,
        null=True,
    )

    cianeto_livre = models.FloatField(
        verbose_name='Cianeto livre -  mg/L CN',
        blank=False,
        null=True,
    )

    cloreto_total = models.FloatField(
        verbose_name='Cloreto total - mg/L Cl',
        blank=False,
        null=True,
    )

    cloro_residual_total_combinado_livre = models.FloatField(
        verbose_name='Cloro residual total (combinado + livre) -  mg/L Cl',
        blank=False,
        null=True,
    )

    cobalto_total = models.FloatField(
        verbose_name='Cobalto total - mg/L Co',
        blank=False,
        null=True,
    )

    cobre_dissolvido = models.FloatField(
        verbose_name='Cobre dissolvido - mg/L Cu',
        blank=False,
        null=True,
    )

    cromo_total = models.FloatField(
        verbose_name='Cromo total - mg/L Cr',
        blank=False,
        null=True,
    )

    ferro_dissolvido = models.FloatField(
        verbose_name='Ferro dissolvido - mg/L Fe',
        blank=False,
        null=True,
    )

    fluoreto_total = models.FloatField(
        verbose_name='Fluoreto total-  mg/L F',
        blank=False,
        null=True,
    )

    fosforo_total_ambiente_lentico = models.FloatField(
        verbose_name='Fósforo total (ambiente lêntico) - mg/L P',
        blank=False,
        null=True,
    )

    fosforo_total_ambiente_intermediario = models.FloatField(
        verbose_name='Fósforo total (ambiente intermediário, com tempo de residência entre 2 e 40 dias, e tributários diretos de ambiente lênt.) - mg/L P',
        blank=False,
        null=True,
    )

    fosforo_total_ambiente_lotico = models.FloatField(
        verbose_name='Fósforo  total  (amb.  lótico  e tributários de ambientes intermediários) - mg/L P',
        blank=False,
        null=True,
    )

    litio_total = models.FloatField(
        verbose_name='Lítio total - mg/L Li',
        blank=False,
        null=True,
    )

    manganes_total = models.FloatField(
        verbose_name='Manganês total - mg/L Mn',
        blank=False,
        null=True,
    )

    mercurio_total = models.FloatField(
        verbose_name='Mercúrio total - mg/L Hg',
        blank=False,
        null=True,
    )

    niqueltotal = models.FloatField(
        verbose_name='Níquel total -  mg/L Ni',
        blank=False,
        null=True,
    )

    nitrato = models.FloatField(
        verbose_name='Nitrato - mg/L N',
        blank=False,
        null=True,
    )

    nitrito = models.FloatField(
        verbose_name='Nitrito - mg/L N',
        blank=False,
        null=True,
    )

    nitrogenio_amoniacal_total = models.FloatField(
        verbose_name='Nitrogênio amoniacal total - mg/L N',
        blank=False,
        null=True,
    )

    polifosfatos = models.FloatField(
        verbose_name='Polifosfatos (determinado pela diferença entre fósforo ácido hidrolisável total e fósforo reativo total)',
        blank=False,
        null=True,
    )

    prata_total = models.FloatField(
        verbose_name='Prata total - mg/L Ag',
        blank=False,
        null=True,
    )

    selenio_total = models.FloatField(
        verbose_name='Selênio total - mg/L Se',
        blank=False,
        null=True,
    )

    sulfato_total = models.FloatField(
        verbose_name='Sulfato total - mg/L SO4',
        blank=False,
        null=True,
    )

    sulfeto_H2S_nao_dissociado = models.FloatField(
        verbose_name='Sulfeto (H2S não dissociado) -  mg/L S',
        blank=False,
        null=True,
    )

    taliototal = models.FloatField(
        verbose_name='Tálio total - mg/L Tl ',
        blank=False,
        null=True,
    )

    uranio_total = models.FloatField(
        verbose_name='Urânio total -  mg/L U',
        blank=False,
        null=True,
    )

    vanadio_total = models.FloatField(
        verbose_name='Vanádio total -  mg/L V',
        blank=False,
        null=True,
    )

    zinco_total = models.FloatField(
        verbose_name='Zinco total -  mg/L Zn',
        blank=False,
        null=True,
    )

    acrilamida = models.FloatField(
        verbose_name='Acrilamida - µg/L',
        blank=False,
        null=True,
    )

    alacloro = models.FloatField(
        verbose_name='Alacloro - µg/L',
        blank=False,
        null=True,
    )

    aldrin_dieldrin = models.FloatField(
        verbose_name='Aldrin + Dieldrin - µg/L',
        blank=False,
        null=True,
    )

    atrazina = models.FloatField(
        verbose_name='Atrazina - µg/L',
        blank=False,
        null=True,
    )

    benzeno = models.FloatField(
        verbose_name='Benzeno - µg/L',
        blank=False,
        null=True,
    )

    benzidina = models.FloatField(
        verbose_name='Benzidina - mg/L',
        blank=False,
        null=True,
    )

    benzo_antraceno = models.FloatField(
        verbose_name='Benzo (a) antraceno - µg/L',
        blank=False,
        null=True,
    )

    benzo_pireno = models.FloatField(
        verbose_name=' Benzo (a) pireno - µg/L',
        blank=False,
        null=True,
    )

    benzo_b_fluoranteno = models.FloatField(
        verbose_name='Benzo(b) fluoranteno - µg/L',
        blank=False,
        null=True,
    )

    benzo_k_fluoranteno = models.FloatField(
        verbose_name='Benzo(k) fluoranteno - µg/L',
        blank=False,
        null=True,
    )

    carbaril = models.FloatField(
        verbose_name='Carbaril - µg/L',
        blank=False,
        null=True,
    )

    clordano_cis_trans = models.FloatField(
        verbose_name='Clordano (cis + trans) - µg/L',
        blank=False,
        null=True,
    )

    _2_clorofenol = models.FloatField(
        verbose_name='2-Clorofenol - µg/L',
        blank=False,
        null=True,
    )

    criseno  = models.FloatField(
        verbose_name='Criseno - µg/L',
        blank=False,
        null=True,
    )

    _2_4_d  = models.FloatField(
        verbose_name='2,4-D - µg/L',
        blank=False,
        null=True,
    )

    demeton_demeton_o_demeton_s  = models.FloatField(
        verbose_name='Demeton (Demeton-O + Demeton-S) - µg/L',
        blank=False,
        null=True,
    )

    dibenzo_antraceno  = models.FloatField(
        verbose_name='Dibenzo (a,h) antraceno - µg/L',
        blank=False,
        null=True,
    )

    _1_2_dicloroetano = models.FloatField(
        verbose_name='1,2-Dicloroetano - mg/L',
        blank=False,
        null=True,
    )

    _1_1_dicloroeteno = models.FloatField(
        verbose_name='1,1-Dicloroeteno - mg/L',
        blank=False,
        null=True,
    )

    _2_4_diclorofenol  = models.FloatField(
        verbose_name='2,4-Diclorofenol - µg/L',
        blank=False,
        null=True,
    )

    _3_3_diclorobenzidina  = models.FloatField(
        verbose_name='3,3-Diclorobenzidina - µg/L',
        blank=False,
        null=True,
    )

    diclorometano = models.FloatField(
        verbose_name='Diclorometano - mg/L',
        blank=False,
        null=True,
    )
         
    ddt_p_p_ddt_p_p_dde_p_p_ddd = models.FloatField(
        verbose_name="DDT (p,p'-DDT + p,p'-DDE + p,p'-DDD) - µg/L",
        blank=False,
        null=True,
    )

    dodecacloro_pentaciclodecano = models.FloatField(
        verbose_name="Dodecacloro pentaciclodecano - µg/L",
        blank=False,
        null=True,
    )

    endossulfan_a_b_sulfato = models.FloatField(
        verbose_name="Endossulfan (a + b + sulfato) - µg/L",
        blank=False,
        null=True,
    )

    endrin = models.FloatField(
        verbose_name="Endrin - µg/L",
        blank=False,
        null=True,
    )

    estireno = models.FloatField(
        verbose_name="Estireno - mg/L",
        blank=False,
        null=True,
    )

    eilbenzeno = models.FloatField(
        verbose_name="Etilbenzeno - µg/L",
        blank=False,
        null=True,
    )

    fenois_totais_4_aminoantipirina = models.FloatField(
        verbose_name="EFenóis totais (substâncias que reagem com 4-aminoantipirina) - mg/L C6H5OH",
        blank=False,
        null=True,
    )

    glifosato = models.FloatField(
        verbose_name="Glifosato - µg/L",
        blank=False,
        null=True,
    )

    gution = models.FloatField(
        verbose_name="Gution - µg/L",
        blank=False,
        null=True,
    )

    heptacloro_epoxido_heptacloro = models.FloatField(
        verbose_name="Heptacloro epóxido + Heptacloro - µg/L",
        blank=False,
        null=True,
    )

    hexaclorobenzeno = models.FloatField(
        verbose_name="Hexaclorobenzeno - µg/L",
        blank=False,
        null=True,
    )

    indeno_1_2_3_cd_pireno = models.FloatField(
        verbose_name="Indeno (1,2,3-cd) pireno - µg/L",
        blank=False,
        null=True,
    )

    lindano_g_HCH = models.FloatField(
        verbose_name="Lindano (g-HCH) - µg/L",
        blank=False,
        null=True,
    )

    malation = models.FloatField(
        verbose_name="Malation - µg/L",
        blank=False,
        null=True,
    )

    metolacloro = models.FloatField(
        verbose_name="Metolacloro - µg/L",
        blank=False,
        null=True,
    )

    metoxicloro = models.FloatField(
        verbose_name="metoxicloro - µg/L",
        blank=False,
        null=True,
    )

    monoclorobenzeno = models.FloatField(
        verbose_name="monoclorobenzeno - µg/L",
        blank=False,
        null=True,
    )

    paration = models.FloatField(
        verbose_name="Paration - µg/L",
        blank=False,
        null=True,
    )

    pcbs_ifenilas_policloradas = models.FloatField(
        verbose_name="PCBs - Bifenilas policloradas  - µg/L",
        blank=False,
        null=True,
    )

    pentaclorofenol = models.FloatField(
        verbose_name="Pentaclorofenol - mg/L",
        blank=False,
        null=True,
    )

    simazina = models.FloatField(
        verbose_name="Simazina - µg/L",
        blank=False,
        null=True,
    )

    substancias_tensoativas = models.FloatField(
        verbose_name="Substâncias tensoativas que reagem com o azul de metileno - mg/L LAS",
        blank=False,
        null=True,
    )

    _2_4_5_t = models.FloatField(
        verbose_name="2,4,5-T - µg/L",
        blank=False,
        null=True,
    )

    tetracloreto_carbono = models.FloatField(
        verbose_name="Tetracloreto de carbono - mg/L",
        blank=False,
        null=True,
    )

    tetracloroeteno = models.FloatField(
        verbose_name="Tetracloroeteno - mg/L",
        blank=False,
        null=True,
    )

    tolueno = models.FloatField(
        verbose_name="Tolueno - µg/L",
        blank=False,
        null=True,
    )

    toxafeno = models.FloatField(
        verbose_name="Toxafeno - µg/L",
        blank=False,
        null=True,
    )

    _2_4_5_tp = models.FloatField(
        verbose_name="2,4,5-TP - µg/L",
        blank=False,
        null=True,
    )

    tributilestanho = models.FloatField(
        verbose_name="Tributilestanho - µg/L TBT",
        blank=False,
        null=True,
    )

    triclorobenzeno = models.FloatField(
        verbose_name="Triclorobenzeno  (1,2,3-TCB  +  1,2,4-TCB) - mg/L",
        blank=False,
        null=True,
    )

    tricloroeteno = models.FloatField(
        verbose_name="Tricloroeteno - mg/L",
        blank=False,
        null=True,
    )

    _2_4_6_triclorofenol   = models.FloatField(
        verbose_name="2 , 4 , 6 - Triclorofenol   - mg/L",
        blank=False,
        null=True,
    )

    trifluralina = models.FloatField(
        verbose_name="Trifluralina - µg/L",
        blank=False,
        null=True,
    )

    Xileno = models.FloatField(
        verbose_name="Xileno - µg/L",
        blank=False,
        null=True,
    )

    ## Padrões em substituição ou adicionalmente


    ordem = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        '''Sub classe para definir meta atributos da classe principal.'''

        app_label = 'agua'
        verbose_name = 'Tabela de Água'
        verbose_name_plural = 'Tabelas de Água'
