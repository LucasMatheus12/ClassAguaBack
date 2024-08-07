from django.db import models


class TiposAgua(models.Model):
    titulo = models.CharField(
        verbose_name='Título',
        max_length=100,
    )

    Clorofila_a = models.FloatField(
        verbose_name='Clorofila a - µg/L',
        blank=False,null=True,
    )

    densidade_cianobactérias = models.FloatField(
        verbose_name='Densidade de cianobactérias - cel/mL',
        blank=False,null=True,
    )

    solidos_dissolvidos_totais = models.FloatField(
        verbose_name='Sólidos dissolvidos totais - mg/L',
        blank=False,
        null=True,
    )

    aluminio_dissolvido = models.FloatField(
        verbose_name='Alumínio dissolvido - mg/L Al',
        blank=False,
        null=True,
    )

    antimonio = models.FloatField(
        verbose_name='Antimônio - mg/L Sb',
        blank=False,
        null=True,
    )

    arsenio_total = models.FloatField(
        verbose_name='Arsênio total - mg/L As',
        blank=False,
        null=True,
    )

    bario_total = models.FloatField(
        verbose_name='Bário total - mg/L Ba',
        blank=False,
        null=True,
    )

    berilio_total = models.FloatField(
        verbose_name='Berílio total - mg/L Be',
        blank=False,
        null=True,
    )

    boro_total = models.FloatField(
        verbose_name='Boro total - mg/L B',
        blank=False,
        null=True,
    )

    cadmio_total = models.FloatField(
        verbose_name='Cádmio total - mg/L Cd',
        blank=False,
        null=True,
    )

    chumbo_total = models.FloatField(
        verbose_name='Chumbo total - mg/L Pb',
        blank=False,
        null=True,
    )

    cloreto_total = models.FloatField(
        verbose_name='Cloreto total - mg/L Cl',
        blank=False,
        null=True,
    )

    cloro_residual_total = models.FloatField(
        verbose_name='Cloro residual total (combinado + livre) - mg/L Cl',
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
        verbose_name='Fluoreto total - mg/L F',
        blank=False,
        null=True,
    )

    fosforo_total_lentico = models.FloatField(
        verbose_name='Fósforo total (ambiente lêntico) - mg/L P',
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

    niquel_total = models.FloatField(
        verbose_name='Níquel total - mg/L Ni',
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

    sulfeto = models.FloatField(
        verbose_name='Sulfeto (H2S não dissociado) - mg/L S',
        blank=False,
        null=True,
    )

    uranio_total = models.FloatField(
        verbose_name='Urânio total - mg/L U',
        blank=False,
        null=True,
    )

    vanadio_total = models.FloatField(
        verbose_name='Vanádio total - mg/L V',
        blank=False,
        null=True,
    )

    zinco_total = models.FloatField(
        verbose_name='Zinco total - mg/L Zn',
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
        verbose_name='Benzidina - µg/L',
        blank=False,
        null=True,
    )

    benzo_a_antraceno = models.FloatField(
        verbose_name='Benzo (a) antraceno - µg/L',
        blank=False,
        null=True,
    )

    benzo_a_pireno = models.FloatField(
        verbose_name='Benzo (a) pireno - µg/L',
        blank=False,
        null=True,
    )

    benzo_b_fluoranteno = models.FloatField(
        verbose_name='Benzo (b) fluoranteno - µg/L',
        blank=False,
        null=True,
    )

    benzo_k_fluoranteno = models.FloatField(
        verbose_name='Benzo (k) fluoranteno - µg/L',
        blank=False,
        null=True,
    )

    carbaril = models.FloatField(
        verbose_name='Carbaril - µg/L',
        blank=False,
        null=True,
    )

    clordano = models.FloatField(
        verbose_name='Clordano (cis + trans) - µg/L',
        blank=False,
        null=True,
    )

    clorofenol = models.FloatField(
        verbose_name='2-Clorofenol - µg/L',
        blank=False,
        null=True,
    )

    criseno = models.FloatField(
        verbose_name='Criseno - µg/L',
        blank=False,
        null=True,
    )

    d_2_4 = models.FloatField(
        verbose_name='2,4-D - µg/L',
        blank=False,
        null=True,
    )

    demeton = models.FloatField(
        verbose_name='Demeton (Demeton-O + Demeton-S) - µg/L',
        blank=False,
        null=True,
    )

    dibenzo_a_h_antraceno = models.FloatField(
        verbose_name='Dibenzo (a,h) antraceno - µg/L',
        blank=False,
        null=True,
    )

    dicloroetano_1_2 = models.FloatField(
        verbose_name='1,2-Dicloroetano - mg/L',
        blank=False,
        null=True,
    )

    diclorofenol_2_4 = models.FloatField(
        verbose_name='2,4-Diclorofenol - µg/L',
        blank=False,
        null=True,
    )

    diclorometano = models.FloatField(
        verbose_name='Diclorometano - mg/L',
        blank=False,
        null=True,
    )

    ddt = models.FloatField(
        verbose_name="DDT (p,p'-DDT + p,p'-DDE + p,p'-DDD) - µg/L",
        blank=False,
        null=True,
    )

    dodecacloro_pentaciclodecano = models.FloatField(
        verbose_name='Dodecacloro pentaciclodecano - µg/L',
        blank=False,
        null=True,
    )

    endossulfan = models.FloatField(
        verbose_name='Endossulfan (a + b + sulfato) - µg/L',
        blank=False,
        null=True,
    )

    endrin = models.FloatField(
        verbose_name='Endrin - µg/L',
        blank=False,
        null=True,
    )

    estireno = models.FloatField(
        verbose_name='Estireno - mg/L',
        blank=False,
        null=True,
    )

    etilbenzeno = models.FloatField(
        verbose_name='Etilbenzeno - µg/L',
        blank=False,
        null=True,
    )

    fenois_totais = models.FloatField(
        verbose_name='Fenóis totais (substâncias que reagem com 4-aminoantipirina) - mg/L C6H5OH',
        blank=False,
        null=True,
    )

    glifosato = models.FloatField(
        verbose_name='Glifosato - µg/L',
        blank=False,
        null=True,
    )

    gution = models.FloatField(
        verbose_name='Gution - µg/L',
        blank=False,
        null=True,
    )

    heptacloro_epoxido_heptacloro = models.FloatField(
        verbose_name='Heptacloro epóxido + Heptacloro - µg/L',
        blank=False,
        null=True,
    )

    hexaclorobenzeno = models.FloatField(
        verbose_name='Hexaclorobenzeno - µg/L',
        blank=False,
        null=True,
    )

    indeno_pireno = models.FloatField(
        verbose_name='Indeno (1,2,3-cd) pireno - µg/L',
        blank=False,
        null=True,
    )

    lindano = models.FloatField(
        verbose_name='Lindano (g-HCH) - µg/L',
        blank=False,
        null=True,
    )

    malation = models.FloatField(
        verbose_name='Malation - µg/L',
        blank=False,
        null=True,
    )

    metolacloro = models.FloatField(
        verbose_name='Metolacloro - µg/L',
        blank=False,
        null=True,
    )

    metoxicloro = models.FloatField(
        verbose_name='Metoxicloro - µg/L',
        blank=False,
        null=True,
    )

    paration = models.FloatField(
        verbose_name='Paration - µg/L',
        blank=False,
        null=True,
    )

    pcbs = models.FloatField(
        verbose_name='PCBs - Bifenilas policloradas - µg/L',
        blank=False,
        null=True,
    )

    pentaclorofenol = models.FloatField(
        verbose_name='Pentaclorofenol - mg/L',
        blank=False,
        null=True,
    )

    simazina = models.FloatField(
        verbose_name='Simazina - µg/L',
        blank=False,
        null=True,
    )

    substancias_tensoativas = models.FloatField(
        verbose_name='Substâncias tensoativas que reagem com o azul de metileno - mg/L LAS',
        blank=False,
        null=True,
    )

    _2_4_5_T = models.FloatField(
        verbose_name='2,4,5-T - µg/L',
        blank=False,
        null=True,
    )

    tetracloreto_carbono = models.FloatField(
        verbose_name='Tetracloreto de carbono - mg/L',
        blank=False,
        null=True,
    )

    tetracloroeteno = models.FloatField(
        verbose_name='Tetracloroeteno - mg/L',
        blank=False,
        null=True,
    )

    tolueno = models.FloatField(
        verbose_name='Tolueno - µg/L',
        blank=False,
        null=True,
    )

    toxafeno = models.FloatField(
        verbose_name='Toxafeno - µg/L',
        blank=False,
        null=True,
    )

    _2_4_5_TP = models.FloatField(
        verbose_name='2,4,5-TP - µg/L',
        blank=False,
        null=True,
    )

    tributilestanho = models.FloatField(
        verbose_name='Tributilestanho - µg/L TBT',
        blank=False,
        null=True,
    )

    triclorobenzeno = models.FloatField(
        verbose_name='Triclorobenzeno (1,2,3-TCB + 1,2,4-TCB) - mg/L',
        blank=False,
        null=True,
    )

    tricloroeteno = models.FloatField(
        verbose_name='Tricloroeteno - mg/L',
        blank=False,
        null=True,
    )

    _2_4_6_triclorofenol = models.FloatField(
        verbose_name='2,4,6-Triclorofenol - mg/L',
        blank=False,
        null=True,
    )

    trifluralina = models.FloatField(
        verbose_name='Trifluralina - µg/L',
        blank=False,
        null=True,
    )

    xileno = models.FloatField(
        verbose_name='Xileno - µg/L',
        blank=False,
        null=True,
    )

    _3_3_diclorobenzidina = models.FloatField(
        verbose_name='3,3-Diclorobenzidina - µg/L',
        blank=False,
        null=True,
    )

    polifosfatos = models.FloatField(
        verbose_name='Polifosfatos - mg/L P',
        blank=False,
        null=True,
    )

    talio_total = models.FloatField(
        verbose_name='Tálio total - mg/L Tl',
        blank=False,
        null=True,
    )

    monoclorobenzeno = models.FloatField(
        verbose_name='Monoclorobenzeno - µg/L',
        blank=False,
        null=True,
    )

    cianeto_total = models.FloatField(
        verbose_name='Cianeto total - mg/L CN',
        blank=False,
        null=True,
    )

    estanho_total = models.FloatField(
        verbose_name='Estanho total - mg/L Sn',
        blank=False,
        null=True,
    )

    manganes_dissolvido = models.FloatField(
        verbose_name='Manganês dissolvido - mg/L Mn',
        blank=False,
        null=True,
    )

    cloroformio = models.FloatField(
        verbose_name='Clorofórmio - mg/L',
        blank=False,
        null=True,
    )

    dicloroeteno = models.FloatField(
        verbose_name='Dicloroeteno - mg/L',
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.titulo

    class Meta:

        app_label = 'agua'
        verbose_name = 'Tipo de Água'
        verbose_name_plural = 'Tipos de Água'
