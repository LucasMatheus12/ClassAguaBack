from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import TabelaAgua
from ..serializers import TabelaAguaSerializer


class TabelaAguaViewSet(viewsets.ModelViewSet):
    queryset = TabelaAgua.objects.all()
    serializer_class = TabelaAguaSerializer

    filter_backends = [filters.SearchFilter]

    search_fields = [
        
    ]

    @action(detail=False, methods=['post'])
    def tipo_agua(self, request):
        tabelas = TabelaAgua.objects.all()

        ## I - condições de qualidade de água - valores

        salinidade_agua = request.data.get('salinidade_agua', None)
        if salinidade_agua:
            tipo = tabelas.filter(salinidade_agua__lte=salinidade_agua)

        dbo_5_dias_a_20_C = request.data.get('dbo_5_dias_a_20_C', None)
        if dbo_5_dias_a_20_C:
            tipo = tabelas.filter(dbo_5_dias_a_20_C__lte=dbo_5_dias_a_20_C)
        
        od_qualquer_amostra = request.data.get('od_qualquer_amostra', None)
        if od_qualquer_amostra:
            tipo = tabelas.filter(od_qualquer_amostra__lte=od_qualquer_amostra)
        
        turbidez_unidades_nefelometrica_turbidez = request.data.get('turbidez_unidades_nefelometrica_turbidez', None)
        if turbidez_unidades_nefelometrica_turbidez:
            tipo = tabelas.filter(turbidez_unidades_nefelometrica_turbidez__lte=turbidez_unidades_nefelometrica_turbidez)

        ph = request.data.get('ph', None)
        if ph:
            tipo = tabelas.filter(ph__lte=ph)
        
        cor_verdadeira = request.data.get('cor_verdadeira', None)
        if cor_verdadeira:
            tipo = tabelas.filter(cor_verdadeira__lte=cor_verdadeira)
        
        clorofila_a = request.data.get('clorofila_a', None)
        if clorofila_a:
            tipo = tabelas.filter(clorofila_a__lte=clorofila_a)
        
        densidade_cianobacterias = request.data.get('densidade_cianobacterias', None)
        if densidade_cianobacterias:
            tipo = tabelas.filter(densidade_cianobacterias__lte=densidade_cianobacterias)
        
        carbono_organico_total = request.data.get('carbono_organico_total', None)
        if carbono_organico_total:
            tipo = tabelas.filter(carbono_organico_total__lte=carbono_organico_total)

        ##

        arsenio_total = request.data.get('arsenio_total', None)
        if arsenio_total:
            tipo = tabelas.filter(arsenio_total__lte=arsenio_total)
        
        corofila_a = request.data.get('corofila_a', None)
        if corofila_a:
            tipo = tabelas.filter(corofila_a__lte=corofila_a)

        densidade_de_cianobactérias = request.data.get('densidade_de_cianobactérias', None)
        if densidade_de_cianobactérias:
            tipo = tabelas.filter(densidade_de_cianobactérias__lte=densidade_de_cianobactérias)

        solidos_dissolvidos_totais = request.data.get('solidos_dissolvidos_totais', None)
        if solidos_dissolvidos_totais:
            tipo = tabelas.filter(solidos_dissolvidos_totais__lte=solidos_dissolvidos_totais)

        aluminio_dissolvido = request.data.get('aluminio_dissolvido', None)
        if aluminio_dissolvido:
            tipo = tabelas.filter(aluminio_dissolvido__lte=aluminio_dissolvido)

        antimonio = request.data.get('antimonio', None)
        if antimonio:
            tipo = tabelas.filter(antimonio__lte=antimonio)
        
        bario_total = request.data.get('bario_total', None)
        if bario_total:
            tipo = tabelas.filter(bario_total__lte=bario_total)
        
        berilio_total = request.data.get('berilio_total', None)
        if berilio_total:
            tipo = tabelas.filter(berilio_total__lte=berilio_total)
        
        boro_total = request.data.get('boro_total', None)
        if boro_total:
            tipo = tabelas.filter(boro_total__lte=boro_total)

        cadmio_total = request.data.get('cadmio_total', None)
        if cadmio_total:
            tipo = tabelas.filter(cadmio_total__lte=cadmio_total)

        chumbo_total = request.data.get('chumbo_total', None)
        if chumbo_total:
            tipo = tabelas.filter(chumbo_total__lte=chumbo_total)

        cianeto_livre = request.data.get('cianeto_livre', None)
        if cianeto_livre:
            tipo = tabelas.filter(cianeto_livre__lte=cianeto_livre)
        
        cloreto_total = request.data.get('cloreto_total', None)
        if cloreto_total:
            tipo = tabelas.filter(cloreto_total__lte=cloreto_total)

        cloro_residual_total_combinado_livre = request.data.get('cloro_residual_total_combinado_livre', None)
        if cloro_residual_total_combinado_livre:
            tipo = tabelas.filter(cloro_residual_total_combinado_livre__lte=cloro_residual_total_combinado_livre)

        cobalto_total = request.data.get('cobalto_total', None)
        if cobalto_total:
            tipo = tabelas.filter(cobalto_total__lte=cobalto_total)
        
        cobre_dissolvido = request.data.get('cobre_dissolvido', None)
        if cobre_dissolvido:
            tipo = tabelas.filter(cobre_dissolvido__lte=cobre_dissolvido)
        
        cromo_total = request.data.get('cromo_total', None)
        if cromo_total:
            tipo = tabelas.filter(cromo_total__lte=cromo_total)

        ferro_dissolvido = request.data.get('ferro_dissolvido', None)
        if ferro_dissolvido:
            tipo = tabelas.filter(ferro_dissolvido__lte=ferro_dissolvido)
        
        fluoreto_total = request.data.get('fluoreto_total', None)
        if fluoreto_total:
            tipo = tabelas.filter(fluoreto_total__lte=fluoreto_total)
        
        fosforo_total_ambiente_lentico = request.data.get('fosforo_total_ambiente_lentico', None)
        if fosforo_total_ambiente_lentico:
            tipo = tabelas.filter(fosforo_total_ambiente_lentico__lte=fosforo_total_ambiente_lentico)
        
        fosforo_total_ambiente_intermediario = request.data.get('fosforo_total_ambiente_intermediario', None)
        if fosforo_total_ambiente_intermediario:
            tipo = tabelas.filter(fosforo_total_ambiente_intermediario__lte=fosforo_total_ambiente_intermediario)

        fosforo_total_ambiente_lotico = request.data.get('fosforo_total_ambiente_lotico', None)
        if fosforo_total_ambiente_lotico:
            tipo = tabelas.filter(fosforo_total_ambiente_lotico__lte=fosforo_total_ambiente_lotico)
        
        litio_total = request.data.get('litio_total', None)
        if litio_total:
            tipo = tabelas.filter(litio_total__lte=litio_total)
        
        manganes_total = request.data.get('manganes_total', None)
        if manganes_total:
            tipo = tabelas.filter(manganes_total__lte=manganes_total)
        
        mercurio_total = request.data.get('mercurio_total', None)
        if mercurio_total:
            tipo = tabelas.filter(mercurio_total__lte=mercurio_total)
        
        niqueltotal = request.data.get('niqueltotal', None)
        if niqueltotal:
            tipo = tabelas.filter(niqueltotal__lte=niqueltotal)

        nitrato = request.data.get('nitrato', None)
        if nitrato:
            tipo = tabelas.filter(nitrato__lte=nitrato)
        
        nitrito = request.data.get('nitrito', None)
        if nitrito:
            tipo = tabelas.filter(nitrito__lte=nitrito)
        
        nitrogenio_amoniacal_total = request.data.get('nitrogenio_amoniacal_total', None)
        if nitrogenio_amoniacal_total:
            tipo = tabelas.filter(nitrogenio_amoniacal_total__lte=nitrogenio_amoniacal_total)
        
        polifosfatos = request.data.get('polifosfatos', None)
        if polifosfatos:
            tipo = tabelas.filter(polifosfatos__lte=polifosfatos)
        
        prata_total = request.data.get('prata_total', None)
        if prata_total:
            tipo = tabelas.filter(prata_total__lte=prata_total)
        
        selenio_total = request.data.get('selenio_total', None)
        if selenio_total:
            tipo = tabelas.filter(selenio_total__lte=selenio_total)
        
        sulfato_total = request.data.get('sulfato_total', None)
        if sulfato_total:
            tipo = tabelas.filter(sulfato_total__lte=sulfato_total)
        
        sulfeto_H2S_nao_dissociado = request.data.get('sulfeto_H2S_nao_dissociado', None)
        if sulfeto_H2S_nao_dissociado:
            tipo = tabelas.filter(sulfeto_H2S_nao_dissociado__lte=sulfeto_H2S_nao_dissociado)
        
        taliototal = request.data.get('taliototal', None)
        if taliototal:
            tipo = tabelas.filter(taliototal__lte=taliototal)
        
        uranio_total = request.data.get('uranio_total', None)
        if uranio_total:
            tipo = tabelas.filter(uranio_total__lte=uranio_total)
        
        vanadio_total = request.data.get('vanadio_total', None)
        if vanadio_total:
            tipo = tabelas.filter(vanadio_total__lte=vanadio_total)
        
        zinco_total = request.data.get('zinco_total', None)
        if zinco_total:
            tipo = tabelas.filter(zinco_total__lte=zinco_total)
        
        acrilamida = request.data.get('acrilamida', None)
        if acrilamida:
            tipo = tabelas.filter(acrilamida__lte=acrilamida)
        
        alacloro = request.data.get('alacloro', None)
        if alacloro:
            tipo = tabelas.filter(alacloro__lte=alacloro)

        aldrin_dieldrin = request.data.get('aldrin_dieldrin', None)
        if aldrin_dieldrin:
            tipo = tabelas.filter(aldrin_dieldrin__lte=aldrin_dieldrin)
        
        atrazina = request.data.get('atrazina', None)
        if atrazina:
            tipo = tabelas.filter(atrazina__lte=atrazina)
        
        benzeno = request.data.get('benzeno', None)
        if benzeno:
            tipo = tabelas.filter(benzeno__lte=benzeno)
        
        benzidina = request.data.get('benzidina', None)
        if benzidina:
            tipo = tabelas.filter(benzidina__lte=benzidina)
        
        benzo_antraceno = request.data.get('benzo_antraceno', None)
        if benzo_antraceno:
            tipo = tabelas.filter(benzo_antraceno__lte=benzo_antraceno)
        
        benzo_pireno = request.data.get('benzo_pireno', None)
        if benzo_pireno:
            tipo = tabelas.filter(benzo_pireno__lte=benzo_pireno)
        
        benzo_b_fluoranteno = request.data.get('benzo_b_fluoranteno', None)
        if benzo_b_fluoranteno:
            tipo = tabelas.filter(benzo_b_fluoranteno__lte=benzo_b_fluoranteno)
        
        benzo_k_fluoranteno = request.data.get('benzo_k_fluoranteno', None)
        if benzo_k_fluoranteno:
            tipo = tabelas.filter(benzo_k_fluoranteno__lte=benzo_k_fluoranteno)
        
        carbaril = request.data.get('carbaril', None)
        if carbaril:
            tipo = tabelas.filter(carbaril__lte=carbaril)
        
        clordano_cis_trans = request.data.get('clordano_cis_trans', None)
        if clordano_cis_trans:
            tipo = tabelas.filter(clordano_cis_trans__lte=clordano_cis_trans)
        
        _2_clorofenol = request.data.get('_2_clorofenol', None)
        if _2_clorofenol:
            tipo = tabelas.filter(_2_clorofenol__lte=_2_clorofenol)
        
        criseno = request.data.get('criseno', None)
        if criseno:
            tipo = tabelas.filter(criseno__lte=criseno)
        
        _2_4_d = request.data.get('_2_4_d', None)
        if _2_4_d:
            tipo = tabelas.filter(_2_4_d__lte=_2_4_d)
        
        demeton_demeton_o_demeton_s = request.data.get('demeton_demeton_o_demeton_s', None)
        if demeton_demeton_o_demeton_s:
            tipo = tabelas.filter(demeton_demeton_o_demeton_s__lte=demeton_demeton_o_demeton_s)
        
        dibenzo_antraceno = request.data.get('dibenzo_antraceno', None)
        if dibenzo_antraceno:
            tipo = tabelas.filter(dibenzo_antraceno__lte=dibenzo_antraceno)
        
        _1_2_dicloroetano = request.data.get('_1_2_dicloroetano', None)
        if _1_2_dicloroetano:
            tipo = tabelas.filter(_1_2_dicloroetano__lte=_1_2_dicloroetano)
        
        _1_1_dicloroeteno = request.data.get('_1_1_dicloroeteno', None)
        if _1_1_dicloroeteno:
            tipo = tabelas.filter(_1_1_dicloroeteno__lte=_1_1_dicloroeteno)
        
        _2_4_diclorofenol = request.data.get('_2_4_diclorofenol', None)
        if _2_4_diclorofenol:
            tipo = tabelas.filter(_2_4_diclorofenol__lte=_2_4_diclorofenol)
        
        _3_3_diclorobenzidina = request.data.get('_3_3_diclorobenzidina', None)
        if _3_3_diclorobenzidina:
            tipo = tabelas.filter(_3_3_diclorobenzidina__lte=_3_3_diclorobenzidina)
        
        diclorometano = request.data.get('diclorometano', None)
        if diclorometano:
            tipo = tabelas.filter(diclorometano__lte=diclorometano)
        
        ddt_p_p_ddt_p_p_dde_p_p_ddd = request.data.get('ddt_p_p_ddt_p_p_dde_p_p_ddd', None)
        if ddt_p_p_ddt_p_p_dde_p_p_ddd:
            tipo = tabelas.filter(ddt_p_p_ddt_p_p_dde_p_p_ddd__lte=ddt_p_p_ddt_p_p_dde_p_p_ddd)
        
        dodecacloro_pentaciclodecano = request.data.get('dodecacloro_pentaciclodecano', None)
        if dodecacloro_pentaciclodecano:
            tipo = tabelas.filter(dodecacloro_pentaciclodecano__lte=dodecacloro_pentaciclodecano)
        
        endossulfan_a_b_sulfato = request.data.get('endossulfan_a_b_sulfato', None)
        if endossulfan_a_b_sulfato:
            tipo = tabelas.filter(endossulfan_a_b_sulfato__lte=endossulfan_a_b_sulfato)
        
        endrin = request.data.get('endrin', None)
        if endrin:
            tipo = tabelas.filter(endrin__lte=endrin)

        estireno = request.data.get('estireno', None)
        if estireno:
            tipo = tabelas.filter(estireno__lte=estireno)
        
        eilbenzeno = request.data.get('eilbenzeno', None)
        if eilbenzeno:
            tipo = tabelas.filter(eilbenzeno__lte=eilbenzeno)
        
        fenois_totais_4_aminoantipirina = request.data.get('fenois_totais_4_aminoantipirina', None)
        if fenois_totais_4_aminoantipirina:
            tipo = tabelas.filter(fenois_totais_4_aminoantipirina__lte=fenois_totais_4_aminoantipirina)
        
        glifosato = request.data.get('glifosato', None)
        if glifosato:
            tipo = tabelas.filter(glifosato__lte=glifosato)
        
        gution = request.data.get('gution', None)
        if gution:
            tipo = tabelas.filter(gution__lte=gution)
        
        heptacloro_epoxido_heptacloro = request.data.get('heptacloro_epoxido_heptacloro', None)
        if heptacloro_epoxido_heptacloro:
            tipo = tabelas.filter(heptacloro_epoxido_heptacloro__lte=heptacloro_epoxido_heptacloro)

        hexaclorobenzeno = request.data.get('hexaclorobenzeno', None)
        if hexaclorobenzeno:
            tipo = tabelas.filter(hexaclorobenzeno__lte=hexaclorobenzeno)

        indeno_1_2_3_cd_pireno = request.data.get('indeno_1_2_3_cd_pireno', None)
        if indeno_1_2_3_cd_pireno:
            tipo = tabelas.filter(indeno_1_2_3_cd_pireno__lte=indeno_1_2_3_cd_pireno)

        lindano_g_HCH = request.data.get('lindano_g_HCH', None)
        if lindano_g_HCH:
            tipo = tabelas.filter(lindano_g_HCH__lte=lindano_g_HCH)
        
        malation = request.data.get('malation', None)
        if malation:
            tipo = tabelas.filter(malation__lte=malation)
        
        metolacloro = request.data.get('metolacloro', None)
        if metolacloro:
            tipo = tabelas.filter(metolacloro__lte=metolacloro)
        
        metoxicloro = request.data.get('metoxicloro', None)
        if metoxicloro:
            tipo = tabelas.filter(metoxicloro__lte=metoxicloro)
        
        monoclorobenzeno = request.data.get('monoclorobenzeno', None)
        if monoclorobenzeno:
            tipo = tabelas.filter(monoclorobenzeno__lte=monoclorobenzeno)
        
        paration = request.data.get('paration', None)
        if paration:
            tipo = tabelas.filter(paration__lte=paration)
        
        pcbs_ifenilas_policloradas = request.data.get('pcbs_ifenilas_policloradas', None)
        if pcbs_ifenilas_policloradas:
            tipo = tabelas.filter(pcbs_ifenilas_policloradas__lte=pcbs_ifenilas_policloradas)
        
        pentaclorofenol = request.data.get('pentaclorofenol', None)
        if pentaclorofenol:
            tipo = tabelas.filter(pentaclorofenol__lte=pentaclorofenol)
        
        simazina = request.data.get('simazina', None)
        if simazina:
            tipo = tabelas.filter(simazina__lte=simazina)
        
        substancias_tensoativas = request.data.get('substancias_tensoativas', None)
        if substancias_tensoativas:
            tipo = tabelas.filter(substancias_tensoativas__lte=substancias_tensoativas)
        
        _2_4_5_t = request.data.get('_2_4_5_t', None)
        if _2_4_5_t:
            tipo = tabelas.filter(_2_4_5_t__lte=_2_4_5_t)
        
        tetracloreto_carbono = request.data.get('tetracloreto_carbono', None)
        if tetracloreto_carbono:
            tipo = tabelas.filter(tetracloreto_carbono__lte=tetracloreto_carbono)
        
        tetracloroeteno = request.data.get('tetracloroeteno', None)
        if tetracloroeteno:
            tipo = tabelas.filter(tetracloroeteno__lte=tetracloroeteno)
        
        tolueno = request.data.get('tolueno', None)
        if tolueno:
            tipo = tabelas.filter(tolueno__lte=tolueno)
        
        toxafeno = request.data.get('toxafeno', None)
        if toxafeno:
            tipo = tabelas.filter(toxafeno__lte=toxafeno)
        
        _2_4_5_tp = request.data.get('_2_4_5_tp', None)
        if _2_4_5_tp:
            tipo = tabelas.filter(_2_4_5_tp__lte=_2_4_5_tp)
        
        tributilestanho = request.data.get('tributilestanho', None)
        if tributilestanho:
            tipo = tabelas.filter(tributilestanho__lte=tributilestanho)
        
        triclorobenzeno = request.data.get('triclorobenzeno', None)
        if triclorobenzeno:
            tipo = tabelas.filter(triclorobenzeno__lte=triclorobenzeno)
        
        tricloroeteno = request.data.get('tricloroeteno', None)
        if tricloroeteno:
            tipo = tabelas.filter(tricloroeteno__lte=tricloroeteno)
        
        _2_4_6_triclorofenol = request.data.get('_2_4_6_triclorofenol', None)
        if _2_4_6_triclorofenol:
            tipo = tabelas.filter(_2_4_6_triclorofenol__lte=_2_4_6_triclorofenol)
        
        trifluralina = request.data.get('trifluralina', None)
        if trifluralina:
            tipo = tabelas.filter(trifluralina__lte=trifluralina)
        
        Xileno = request.data.get('Xileno', None)
        if Xileno:
            tipo = tabelas.filter(Xileno__lte=Xileno)
        

        if tipo:
            resposta = tipo.order_by("-ordem").first()
            return Response({'Sucesso': f'Seu tipo de água é: {resposta.nome}'}, status=status.HTTP_200_OK)
        
        else:
            return Response({'error': 'Name parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

    
