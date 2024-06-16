# Generated by Django 5.0.6 on 2024-06-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TiposAgua",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100, verbose_name="Título")),
                (
                    "Clorofila_a",
                    models.FloatField(null=True, verbose_name="Clorofila a - µg/L"),
                ),
                (
                    "densidade_cianobactérias",
                    models.FloatField(
                        null=True, verbose_name="Densidade de cianobactérias - cel/mL"
                    ),
                ),
                (
                    "solidos_dissolvidos_totais",
                    models.FloatField(
                        null=True, verbose_name="Sólidos dissolvidos totais - mg/L"
                    ),
                ),
                (
                    "aluminio_dissolvido",
                    models.FloatField(
                        null=True, verbose_name="Alumínio dissolvido - mg/L Al"
                    ),
                ),
                (
                    "antimonio",
                    models.FloatField(null=True, verbose_name="Antimônio - mg/L Sb"),
                ),
                (
                    "arsenio_total",
                    models.FloatField(
                        null=True, verbose_name="Arsênio total - mg/L As"
                    ),
                ),
                (
                    "bario_total",
                    models.FloatField(null=True, verbose_name="Bário total - mg/L Ba"),
                ),
                (
                    "berilio_total",
                    models.FloatField(
                        null=True, verbose_name="Berílio total - mg/L Be"
                    ),
                ),
                (
                    "boro_total",
                    models.FloatField(null=True, verbose_name="Boro total - mg/L B"),
                ),
                (
                    "cadmio_total",
                    models.FloatField(null=True, verbose_name="Cádmio total - mg/L Cd"),
                ),
                (
                    "chumbo_total",
                    models.FloatField(null=True, verbose_name="Chumbo total - mg/L Pb"),
                ),
                (
                    "cloreto_total",
                    models.FloatField(
                        null=True, verbose_name="Cloreto total - mg/L Cl"
                    ),
                ),
                (
                    "cloro_residual_total",
                    models.FloatField(
                        null=True,
                        verbose_name="Cloro residual total (combinado + livre) - mg/L Cl",
                    ),
                ),
                (
                    "cobalto_total",
                    models.FloatField(
                        null=True, verbose_name="Cobalto total - mg/L Co"
                    ),
                ),
                (
                    "cobre_dissolvido",
                    models.FloatField(
                        null=True, verbose_name="Cobre dissolvido - mg/L Cu"
                    ),
                ),
                (
                    "cromo_total",
                    models.FloatField(null=True, verbose_name="Cromo total - mg/L Cr"),
                ),
                (
                    "ferro_dissolvido",
                    models.FloatField(
                        null=True, verbose_name="Ferro dissolvido - mg/L Fe"
                    ),
                ),
                (
                    "fluoreto_total",
                    models.FloatField(
                        null=True, verbose_name="Fluoreto total - mg/L F"
                    ),
                ),
                (
                    "fosforo_total_lentico",
                    models.FloatField(
                        null=True,
                        verbose_name="Fósforo total (ambiente lêntico) - mg/L P",
                    ),
                ),
                (
                    "litio_total",
                    models.FloatField(null=True, verbose_name="Lítio total - mg/L Li"),
                ),
                (
                    "manganes_total",
                    models.FloatField(
                        null=True, verbose_name="Manganês total - mg/L Mn"
                    ),
                ),
                (
                    "mercurio_total",
                    models.FloatField(
                        null=True, verbose_name="Mercúrio total - mg/L Hg"
                    ),
                ),
                (
                    "niquel_total",
                    models.FloatField(null=True, verbose_name="Níquel total - mg/L Ni"),
                ),
                (
                    "nitrato",
                    models.FloatField(null=True, verbose_name="Nitrato - mg/L N"),
                ),
                (
                    "nitrito",
                    models.FloatField(null=True, verbose_name="Nitrito - mg/L N"),
                ),
                (
                    "nitrogenio_amoniacal_total",
                    models.FloatField(
                        null=True, verbose_name="Nitrogênio amoniacal total - mg/L N"
                    ),
                ),
                (
                    "prata_total",
                    models.FloatField(null=True, verbose_name="Prata total - mg/L Ag"),
                ),
                (
                    "selenio_total",
                    models.FloatField(
                        null=True, verbose_name="Selênio total - mg/L Se"
                    ),
                ),
                (
                    "sulfato_total",
                    models.FloatField(
                        null=True, verbose_name="Sulfato total - mg/L SO4"
                    ),
                ),
                (
                    "sulfeto",
                    models.FloatField(
                        null=True, verbose_name="Sulfeto (H2S não dissociado) - mg/L S"
                    ),
                ),
                (
                    "uranio_total",
                    models.FloatField(null=True, verbose_name="Urânio total - mg/L U"),
                ),
                (
                    "vanadio_total",
                    models.FloatField(null=True, verbose_name="Vanádio total - mg/L V"),
                ),
                (
                    "zinco_total",
                    models.FloatField(null=True, verbose_name="Zinco total - mg/L Zn"),
                ),
                (
                    "acrilamida",
                    models.FloatField(null=True, verbose_name="Acrilamida - µg/L"),
                ),
                (
                    "alacloro",
                    models.FloatField(null=True, verbose_name="Alacloro - µg/L"),
                ),
                (
                    "aldrin_dieldrin",
                    models.FloatField(
                        null=True, verbose_name="Aldrin + Dieldrin - µg/L"
                    ),
                ),
                (
                    "atrazina",
                    models.FloatField(null=True, verbose_name="Atrazina - µg/L"),
                ),
                (
                    "benzeno",
                    models.FloatField(null=True, verbose_name="Benzeno - µg/L"),
                ),
                (
                    "benzidina",
                    models.FloatField(null=True, verbose_name="Benzidina - µg/L"),
                ),
                (
                    "benzo_a_antraceno",
                    models.FloatField(
                        null=True, verbose_name="Benzo (a) antraceno - µg/L"
                    ),
                ),
                (
                    "benzo_a_pireno",
                    models.FloatField(
                        null=True, verbose_name="Benzo (a) pireno - µg/L"
                    ),
                ),
                (
                    "benzo_b_fluoranteno",
                    models.FloatField(
                        null=True, verbose_name="Benzo (b) fluoranteno - µg/L"
                    ),
                ),
                (
                    "benzo_k_fluoranteno",
                    models.FloatField(
                        null=True, verbose_name="Benzo (k) fluoranteno - µg/L"
                    ),
                ),
                (
                    "carbaril",
                    models.FloatField(null=True, verbose_name="Carbaril - µg/L"),
                ),
                (
                    "clordano",
                    models.FloatField(
                        null=True, verbose_name="Clordano (cis + trans) - µg/L"
                    ),
                ),
                (
                    "clorofenol",
                    models.FloatField(null=True, verbose_name="2-Clorofenol - µg/L"),
                ),
                (
                    "criseno",
                    models.FloatField(null=True, verbose_name="Criseno - µg/L"),
                ),
                ("d_2_4", models.FloatField(null=True, verbose_name="2,4-D - µg/L")),
                (
                    "demeton",
                    models.FloatField(
                        null=True, verbose_name="Demeton (Demeton-O + Demeton-S) - µg/L"
                    ),
                ),
                (
                    "dibenzo_a_h_antraceno",
                    models.FloatField(
                        null=True, verbose_name="Dibenzo (a,h) antraceno - µg/L"
                    ),
                ),
                (
                    "dicloroetano_1_2",
                    models.FloatField(
                        null=True, verbose_name="1,2-Dicloroetano - mg/L"
                    ),
                ),
                (
                    "diclorofenol_2_4",
                    models.FloatField(
                        null=True, verbose_name="2,4-Diclorofenol - µg/L"
                    ),
                ),
                (
                    "diclorometano",
                    models.FloatField(null=True, verbose_name="Diclorometano - mg/L"),
                ),
                (
                    "ddt",
                    models.FloatField(
                        null=True,
                        verbose_name="DDT (p,p'-DDT + p,p'-DDE + p,p'-DDD) - µg/L",
                    ),
                ),
                (
                    "dodecacloro_pentaciclodecano",
                    models.FloatField(
                        null=True, verbose_name="Dodecacloro pentaciclodecano - µg/L"
                    ),
                ),
                (
                    "endossulfan",
                    models.FloatField(
                        null=True, verbose_name="Endossulfan (a + b + sulfato) - µg/L"
                    ),
                ),
                ("endrin", models.FloatField(null=True, verbose_name="Endrin - µg/L")),
                (
                    "estireno",
                    models.FloatField(null=True, verbose_name="Estireno - mg/L"),
                ),
                (
                    "etilbenzeno",
                    models.FloatField(null=True, verbose_name="Etilbenzeno - µg/L"),
                ),
                (
                    "fenois_totais",
                    models.FloatField(
                        null=True,
                        verbose_name="Fenóis totais (substâncias que reagem com 4-aminoantipirina) - mg/L C6H5OH",
                    ),
                ),
                (
                    "glifosato",
                    models.FloatField(null=True, verbose_name="Glifosato - µg/L"),
                ),
                ("gution", models.FloatField(null=True, verbose_name="Gution - µg/L")),
                (
                    "heptacloro_epoxido_heptacloro",
                    models.FloatField(
                        null=True, verbose_name="Heptacloro epóxido + Heptacloro - µg/L"
                    ),
                ),
                (
                    "hexaclorobenzeno",
                    models.FloatField(
                        null=True, verbose_name="Hexaclorobenzeno - µg/L"
                    ),
                ),
                (
                    "indeno_pireno",
                    models.FloatField(
                        null=True, verbose_name="Indeno (1,2,3-cd) pireno - µg/L"
                    ),
                ),
                (
                    "lindano",
                    models.FloatField(null=True, verbose_name="Lindano (g-HCH) - µg/L"),
                ),
                (
                    "malation",
                    models.FloatField(null=True, verbose_name="Malation - µg/L"),
                ),
                (
                    "metolacloro",
                    models.FloatField(null=True, verbose_name="Metolacloro - µg/L"),
                ),
                (
                    "metoxicloro",
                    models.FloatField(null=True, verbose_name="Metoxicloro - µg/L"),
                ),
                (
                    "paration",
                    models.FloatField(null=True, verbose_name="Paration - µg/L"),
                ),
                (
                    "pcbs",
                    models.FloatField(
                        null=True, verbose_name="PCBs - Bifenilas policloradas - µg/L"
                    ),
                ),
                (
                    "pentaclorofenol",
                    models.FloatField(null=True, verbose_name="Pentaclorofenol - mg/L"),
                ),
                (
                    "simazina",
                    models.FloatField(null=True, verbose_name="Simazina - µg/L"),
                ),
                (
                    "substancias_tensoativas",
                    models.FloatField(
                        null=True,
                        verbose_name="Substâncias tensoativas que reagem com o azul de metileno - mg/L LAS",
                    ),
                ),
                (
                    "_2_4_5_T",
                    models.FloatField(null=True, verbose_name="2,4,5-T - µg/L"),
                ),
                (
                    "tetracloreto_carbono",
                    models.FloatField(
                        null=True, verbose_name="Tetracloreto de carbono - mg/L"
                    ),
                ),
                (
                    "tetracloroeteno",
                    models.FloatField(null=True, verbose_name="Tetracloroeteno - mg/L"),
                ),
                (
                    "tolueno",
                    models.FloatField(null=True, verbose_name="Tolueno - µg/L"),
                ),
                (
                    "toxafeno",
                    models.FloatField(null=True, verbose_name="Toxafeno - µg/L"),
                ),
                (
                    "_2_4_5_TP",
                    models.FloatField(null=True, verbose_name="2,4,5-TP - µg/L"),
                ),
                (
                    "tributilestanho",
                    models.FloatField(
                        null=True, verbose_name="Tributilestanho - µg/L TBT"
                    ),
                ),
                (
                    "triclorobenzeno",
                    models.FloatField(
                        null=True,
                        verbose_name="Triclorobenzeno (1,2,3-TCB + 1,2,4-TCB) - mg/L",
                    ),
                ),
                (
                    "tricloroeteno",
                    models.FloatField(null=True, verbose_name="Tricloroeteno - mg/L"),
                ),
                (
                    "_2_4_6_triclorofenol",
                    models.FloatField(
                        null=True, verbose_name="2,4,6-Triclorofenol - mg/L"
                    ),
                ),
                (
                    "trifluralina",
                    models.FloatField(null=True, verbose_name="Trifluralina - µg/L"),
                ),
                ("xileno", models.FloatField(null=True, verbose_name="Xileno - µg/L")),
                (
                    "_3_3_diclorobenzidina",
                    models.FloatField(
                        null=True, verbose_name="3,3-Diclorobenzidina - µg/L"
                    ),
                ),
                (
                    "polifosfatos",
                    models.FloatField(null=True, verbose_name="Polifosfatos - mg/L P"),
                ),
                (
                    "talio_total",
                    models.FloatField(null=True, verbose_name="Tálio total - mg/L Tl"),
                ),
                (
                    "monoclorobenzeno",
                    models.FloatField(
                        null=True, verbose_name="Monoclorobenzeno - µg/L"
                    ),
                ),
                (
                    "cianeto_total",
                    models.FloatField(
                        null=True, verbose_name="Cianeto total - mg/L CN"
                    ),
                ),
                (
                    "estanho_total",
                    models.FloatField(
                        null=True, verbose_name="Estanho total - mg/L Sn"
                    ),
                ),
                (
                    "manganes_dissolvido",
                    models.FloatField(
                        null=True, verbose_name="Manganês dissolvido - mg/L Mn"
                    ),
                ),
                (
                    "cloroformio",
                    models.FloatField(null=True, verbose_name="Clorofórmio - mg/L"),
                ),
                (
                    "dicloroeteno",
                    models.FloatField(null=True, verbose_name="Dicloroeteno - mg/L"),
                ),
            ],
            options={
                "verbose_name": "Tipo de Água",
                "verbose_name_plural": "Tipos de Água",
            },
        ),
    ]
