#!/usr/bin/python
#-*- coding:UTF-8 -*-

import sys
import re
import time

if(4 != len(sys.argv)):
	sys.exit('Usage:\nPython ' + sys.argv[0] +' [input addr info file] [output blacklist file] [log file]')


illegalchars = 'ˉ|ˇ|¨|〃|々|‖|…|〔|〕|〈|〉|「|」|『|』|±|×|÷|∧|∨|∑|∏|∪|∩|∈|∷|√|⊥|∥|∠|⌒|⊙|∫|∮|≡|≌|≈|∽|∝|≠|≮|≯|≤|≥|∞|∵|∴|♂|♀|′|″|℃|＄|¤|￠|￡|‰|§|№|☆|★|○|●|◎|◇|◆|□|■|△|▲|※|→|←|↑|↓|〓|ⅰ|ⅱ|ⅲ|ⅳ|ⅴ|ⅵ|ⅶ|ⅷ|ⅸ|ⅹ||⒈|⒉|⒊|⒋|⒌|⒍|⒎|⒏|⒐|⒑|⒒|⒓|⒔|⒕|⒖|⒗|⒘|⒙|⒚|⒛|⑴|⑵|⑶|⑷|⑸|⑹|⑺|⑻|⑼|⑽|⑾|⑿|⒀|⒁|⒂|⒃|⒄|⒅|⒆|⒇|①|②|③|④|⑤|⑥|⑦|⑧|⑨|⑩|||㈠|㈡|㈢|㈣|㈤|㈥|㈦|㈧|㈨|㈩|||Ⅰ|Ⅱ|Ⅲ|Ⅳ|Ⅴ|Ⅵ|Ⅶ|Ⅷ|Ⅸ|Ⅹ|Ⅺ|Ⅻ|％|＆|＋|／|＜|＝|＞|？|＠|Ｈ|Ｉ|Ｊ|Ｋ|Ｌ|Ｍ|Ｎ|Ｏ|Ｐ|Ｑ|Ｒ|Ｓ|Ｔ|Ｕ|Ｖ|Ｗ|Ｘ|Ｙ|Ｚ|＼|＾|＿|｀|ａ|ｂ|ｃ|ｄ|ｅ|ｆ|ｇ|ｈ|ｉ|ｊ|ｋ|ｌ|ｍ|ｎ|ｏ|ｐ|ｑ|ｒ|ｓ|ｔ|ｕ|ｖ|ｗ|ｘ|ｙ|ｚ|｛|｜|｝|ぁ|あ|ぃ|い|ぅ|う|ぇ|え|ぉ|お|か|が|き|ぎ|く|ぐ|け|げ|こ|ご|さ|ざ|し|じ|す|ず|せ|ぜ|そ|ぞ|た|だ|ち|ぢ|っ|つ|づ|て|で|と|ど|な|に|ぬ|ね|の|は|ば|ぱ|ひ|び|ぴ|ふ|ぶ|ぷ|へ|べ|ぺ|ほ|ぼ|ぽ|ま|み|む|め|も|ゃ|や|ゅ|ゆ|ょ|よ|ら|り|る|れ|ろ|ゎ|わ|ゐ|ゑ|を|ん|ァ|ア|ィ|イ|ゥ|ウ|ェ|エ|ォ|オ|カ|ガ|キ|ギ|ク|グ|ケ|ゲ|コ|ゴ|サ|ザ|シ|ジ|ス|ズ|セ|ゼ|ソ|ゾ|タ|ダ|チ|ヂ|ッ|ツ|ヅ|テ|デ|ト|ド|ナ|ニ|ヌ|ネ|ノ|ハ|バ|パ|ヒ|ビ|ピ|フ|ブ|プ|ヘ|ベ|ペ|ホ|ボ|ポ|マ|ミ|ム|メ|モ|ャ|ヤ|ュ|ユ|ョ|ヨ|ラ|リ|ル|レ|ロ|ヮ|ワ|ヰ|ヱ|ヲ|ン|ヴ|ヵ|ヶ|Β|Γ|Δ|Ε|Ζ|Η|Θ|Ι|Κ|Λ|Μ|Ν|Ξ|Ο|Π|Ρ|Σ|Τ|Υ|Φ|Χ|Ψ|Ω|||||||||α|β|γ|δ|ε|ζ|η|θ|ι|κ|λ|μ|ν|ξ|ο|π|ρ|σ|τ|υ|φ|χ|ψ|ω|︵|︶|︹|︺|︿|﹀|︽|︾|﹁|﹂|﹃|﹄|||︻|︼|︷|︸|︱||︳|︴|Б|В|Г|Д|Е|Ё|Ж|З|И|Й|К|Л|М|Н|О|П|Р|С|Т|У|Ф|Х|Ц|Ч|Ш|Щ|Ъ|Ы|Ь|Э|Ю|Я||а|б|в|г|д|е|ё|ж|з|и|й|к|л|м|н|о|п|р|с|т|у|ф|х|ц|ч|ш|щ|ъ|ы|ь|э|ю|я|ā|á|ǎ|à|ē|é|ě|è|ī|í|ǐ|ì|ō|ó|ǒ|ò|ū|ú|ǔ|ù|ǖ|ǘ|ǚ|ǜ|ü|ê|ɑ||ń|ň||ɡ|||||ㄅ|ㄆ|ㄇ|ㄈ|ㄉ|ㄊ|ㄋ|ㄌ|ㄍ|ㄎ|ㄏ|ㄐ|ㄑ|ㄒ|ㄓ|ㄔ|ㄕ|ㄖ|ㄗ|ㄘ|ㄙ|ㄚ|ㄛ|ㄜ|ㄝ|ㄞ|ㄟ|ㄠ|ㄡ|ㄢ|ㄣ|ㄤ|ㄥ|ㄦ|ㄧ|ㄨ|ㄩ|━|│|┃|┄|┅|┆|┇|┈|┉|┊|┋|┌|┍|┎|┏|┐|┑|┒|┓|└|┕|┖|┗|┘|┙|┚|┛|├|┝|┞|┟|┠|┡|┢|┣|┤|┥|┦|┧|┨|┩|┪|┫|┬|┭|┮|┯|┰|┱|┲|┳|┴|┵|┶|┷|┸|┹|┺|┻|┼|┽|┾|┿|╀|╁|╂|╃|╄|╅|╆|╇|╈|╉|╊|╋'

hybriddigital = '((?:0|零|玲|菱|龄|铃|伶|羚|凌|灵|陵|岭|领|另|令|1|衣|依|一|壹|医|揖|铱|伊|颐|夷|遗|移|仪|胰|疑|沂|宜|姨|彝|椅|蚁|倚|已|乙|矣|以|艺|抑|易|邑|屹|亿|役|臆|逸|肄|疫|亦|裔|意|毅|忆|义|益|溢|诣|议|谊|译|异|翼|翌|绎|2|而|儿|耳|尔|饵|洱|二|贰|3|三|叁|伞|散|4|斯|撕|嘶|思|私|司|丝|死|肆|寺嗣|四|伺|似|饲|巳|5|巫|呜|钨|乌|污|诬|屋|无|芜|梧|吾|吴|毋|武|五|捂|午|舞|伍|侮|坞|戊|雾|晤|物|勿|务|悟|误|6|琉|榴|硫|馏|留|刘|瘤|流|柳|六|7|妻 期|欺|栖|戚|七|凄|漆|柒|沏|其|棋|奇|歧|畦|崎 脐 齐 旗 祈|祁|骑|起|岂|乞|企|启|契|砌|器|气|迄|弃|汽|泣|讫|8|巴|芭|捌|扒|叭|吧|笆|八|疤|拔|跋|靶|把|坝|霸|罢|爸|9|揪|究|纠|玖|韭|久|灸|九|酒|厩|救|旧|臼|舅|咎|就|疚|[0-9a-zA-Z]){4,})'


def filter_sclaper_with_illegalChars():
    rcm_illegal = re.compile(illegalchars)
    rcm_digital = re.compile(hybriddigital)
    
    start_time = time.time()
    fin	= open(file_addr_info, 'r')
    fres	= open(file_filtered, 'w')
    flog	= open(file_log, 'w')
    
    for line in fin:
    	line = line.strip()
    	try:
    		#mid, phone, addr, ip = re.split('\t+', line)
    		yy_fields = re.split('\t+', line)
    		mid, phone, addr, ip = yy_fields[0], yy_fields[1], yy_fields[2], yy_fields[3]
    
    		if (mid == None or phone == None or addr == None or ip == None):
    			fres.write("%s</code>%s\n" % (mid, '00000001'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    		#match = re.search(regexp, addr)
    		#if(match):
    		if(rcm_illegal.search(addr)):
    			fres.write("%s</code>%s\n" % (mid, '00000002'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    
    		match = re.search('([\xe3-\xe9][\x80-\xbf][\x80-\xbf]){3,}', addr)
    		if(not match):	
    			fres.write("%s</code>%s\n" % (mid, '00000003'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    		temp, n = re.subn('[0-9a-zA-Z]+', '', addr)
    		match = re.match('(?:[\xe3-\xe9][\x80-\xbf][\x80-\xbf]){1,2}\-[\xe3-\xe9]', temp)
    		if match :
    			fres.write("%s</code>%s\n" % (mid, '00000005'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    
    		match = re.match('[0-9]*[_,;`\^\"\|\{\}\'\@\=\#\.\-\/\+\*\$\%\\\\]', addr)
    		if match :
    			fres.write("%s</code>%s\n" % (mid, '00000006'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    		
    		match = re.search('雷军|自提|提货|自取|取货|收货|冯', addr)
    		if match :
    			fres.write("%s</code>%s\n" % (mid, '00000008'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    		
    		reg1 = '(?i)^[0-9]+\]|@|\([0-9]+\)|\(dgh\)|\W0+\W|ED亚|\s往|\WTT\W'
    		reg2 = '亿[a-zA-Z0-9\@\#\$\%\*\+\-\=\&;!]+通|a飞|美.*?双$'
    		reg3 = '^\W{3,6}\s|\s\W{3,6}\s|\s\W{3,6}$|巷-[0-9]+$'
    		reg4 = '[a-zA-Z]+(层|室|门|号)|\d+[a-zA-Z]\d+|号[0-9]+号'
    		reg5 = '\d+(?!(教|寝|科)室)[^0-9]{3}室'
    		reg  = '|'.join([reg1, reg2, reg3, reg4, reg5])
    		
    		match = re.search(reg, addr)
    		if match :
    			fres.write("%s</code>%s\n" % (mid, '00000007'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    
    		if re.search('(?:商务|公司)[0-9]{3,}|[0-9]{3,}(?:医院)', addr) :	
    			continue

    		match = rcm_digital.search(addr) 
    		if match and re.search('[\xe3-\xe9][\x80-\xbf][\x80-\xbf]', match.group(1)):
    			fres.write("%s</code>%s\n" % (mid, '00000009'))
    			flog.write("%s</addr>%s\n" % (mid, addr))
    			continue
    			
    	except Exception as e:
    		print "\t" + str(e)
    		fres.write("%s</code>%s\n" % (mid, '00000004'))
    		flog.write("%s</addr>%s\n" % (mid, addr))
    
    fres.close()
    flog.close()
    fin.close()
    
    print "\tUstime:%.3f seconds" % (time.time() - start_time)
