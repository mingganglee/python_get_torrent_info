#-*- coding:utf-8 -*-
import time
from bencode import bdecode
from aaa import passwd
class Parser(object):
    
    def __init__(self,filePath):
        self.path = filePath
        metainfo_file = open(str(self.path), 'rb')
        self.metainfo = bdecode(metainfo_file.read())
       
        metainfo_file.close()
    def getStruct(self):
        print(self.metainfo.keys())
 
    #如果是单文件就返回：0
    #如果是多文件就返回:1
    def checkType(self):
        if 'files' in self.metainfo['info']:
            return 1
        else:
            return 0
        
    def getCreationDate(self):
        if 'creation date' in self.metainfo:
            return self.metainfo['creation date']
        else:
            return ''
    
    def getInfo(self):
        return self.metainfo['info'].keys()
 
     #获得文件名
    def getName(self):
      
        info = self.metainfo['info']
 
        if 'name.utf-8' in info:
            filename=info['name.utf-8']
        else:
            filename = info['name']
 
        for c in filename:
            if c=="'":
                filename=filename.replace(c,"\\\'")
        return filename
 
    
    #多文件的情况下，获得所有文件，返回为:dic 
    def getInfoFiles(self):
        if 'files' in self.metainfo['info']:
            return self.metainfo['info']['files']
        else:
            if '.mkv' in self.metainfo['info']['name']:
                file_name = self.metainfo['info']['name']
                file_size = self.metainfo['info']['length']
                write_content(file_name, file_size)
            return []
    
    #返回创建时间
    def getCreatedBy(self):
        if 'created by' in self.metainfo:
            return self.metainfo['created by']
        else:
            return ''
    
    #获得编码方式
    def getEncoding(self):
        if 'encoding' in self.metainfo:
            return self.metainfo['encoding']
        return ""
    
    def getComments(self):
        info = self.metainfo['info']
 
        if 'comment.utf-8' in self.metainfo:
            comment=self.metainfo['comment.utf-8']
            return comment
        else:
            return ''

    def getSize(self):
        if 'length' in self.metainfo:
            return self.metainfo['length']
        return ""

def run(file_path):
    parser=Parser(file_path)

    files = parser.getInfoFiles()
    for file in files:
        if 'files' in file:
            for f in file:
                if '.mkv' in file['path'][0]:
                    file_name = file['path'][0]
                    file_size = file['length']
                    write_content(file_name, file_size)
        else:
            if '.mkv' in file['path'][0]:
                file_name = file['path'][0]
                file_size = file['length']
                write_content(file_name, file_size)

def write_content(name, size):
    content = '{}={}\n'.format(name, size)
    with open('torrent_info', 'a') as file:
        file.write(content)


 
if __name__ == "__main__":
    torrents = [".00af33fdb9a047e73d62c590340fd16d2fa932dd.torrent",
                ".02cc2cf8193e12bfad1441c87c97d97528cf7721.torrent",
                ".03033cc72616e267a443e74c105985f60da8f16b.torrent",
                ".05950396edabb1c0279e032622c2cf17a560a071.torrent",
                ".0b1f4f1b8b8acd37147271f583f2f0b3bedf983e.torrent",
                ".0ca8aeae167998da07039bcf9568d132faa7aa8f.torrent",
                ".0d87c802f0702f3fc66770c50003130123993107.torrent",
                ".10f25d1446e40d67fd6e9419a756967b9dc81663.torrent",
                ".11b50d570a1d6debac82ec90484e6fcc248cced1.torrent",
                ".128482a599529182d1f1223a78da3cde0a1cc70b.torrent",
                ".1313d654497bcfb9ea30716bf1ec8926b2ce5440.torrent",
                ".14e2ce396cadad9526f4e1200da680c09d28f796.torrent",
                ".1875fe9c05be9199e9f9ac6fcb53db21d528643b.torrent",
                ".1c727f6e5f52bac3795796ad7e9977d60369e8f8.torrent",
                ".1dbb5699547e3d54de7130868ea4e01e2903b735.torrent",
                ".1e129f339ffb20a6a9bab78ad3a3deae7a12bd15.torrent",
                ".1fdf0c9bbf8bc22b5971d840dd80245b4806dff9.torrent",
                ".1ff4e2e502a7e80fa0f04e1f8785111f062fad36.torrent",
                ".21e5f1e0dd216e4e66e832eaf46ab058890c92fa.torrent",
                ".2231cd42bd0b078c675c7365acbaa5ee0b5943da.torrent",
                ".23159e1e8138823f2c31133920a6f01f7237447b.torrent",
                ".236b0a072ad277f484a311b69de3637fefc254b9.torrent",
                ".239f37fac5123a310254cb12357878e7b40a9ff9.torrent",
                ".2615b96900a2fd1f27794620e84673eb10a8bcc7.torrent",
                ".2b78c5904f7bd82a2f85e4765dd2924cf6367dca.torrent",
                ".34b0d7a7a559d74afe6fd724f3e690469118bf63.torrent",
                ".35703874207522baf7df446c592405c9bb355b68.torrent",
                ".38de1038ce993869c065e8587bebf3d38dc0817f.torrent",
                ".3981a38e09a652c12880c5b6f15e19c9a338f731.torrent",
                ".39f6c50d6497b81e5b1747ea6a28dabf038ba82e.torrent",
                ".3a0e513d937e5cfcbfd2c8dc30f99e7ad7406d3e.torrent",
                ".3d34284832dc92d4b7589ed40bba4506e0abed84.torrent",
                ".3f8f845e3bdc571154e03267c5c37ab14e4a37af.torrent",
                ".3f93fc876169f76c378958698c945ae2f65206cf.torrent",
                ".445fb979a040b51783b193bf8bf217207b94e343.torrent",
                ".450400be78fb810d100095b30c65ae8d7ebd3955.torrent",
                ".46880d10e6d192ab41e1ebefdd9af7b778752c6b.torrent",
                ".4930744c3a931e04e2e7b4871c94d3ecc312fb77.torrent",
                ".49f0b43f26f6c2965628a83acd245362e5976260.torrent",
                ".4a5f02f027c59bd79fe95bf44a3c049a021e78de.torrent",
                ".4dafa65de80c38271053cd749e89e41e7efa3c96.torrent",
                ".4e65ae1360caec57114d2e2fe595038d700aa8e9.torrent",
                ".5504678ec9b296e9c277fabc57ccaa5a46bf446c.torrent",
                ".555f070a17b0e5f813d014a40dfe6df6558718ab.torrent",
                ".57860c17e67a46f98926e86a82de2e56a8d6fc71.torrent",
                ".5a1a400c963241bb604c9d262ba60c4d1d53dd8c.torrent",
                ".5aee8a8ac438549a516644f7839ee89b7a38c93d.torrent",
                ".5f49b6c6354fa5920557459b97189ebe8b9df1d0.torrent",
                ".600b16e27c744f26e2841494cd3436ef712ca5ca.torrent",
                ".60948936294d707ff2b7b828911ac18ef5b68213.torrent",
                ".60c324ffa7c09aff8dbb504e17c6597aef9b37cb.torrent",
                ".6286cf53999e2cd238c8a58dc67ebc8933480890.torrent",
                ".647f8d2ec22e2f527f398f7f607161cc5680f92f.torrent",
                ".64c0b18a75612232cff86b2a3baeb88d2bce3ee8.torrent",
                ".670ec0aac4c8b6d39f2cb8e464afd8720845ea3d.torrent",
                ".676a9459d94081e13675da2a0472c20014e21a8f.torrent",
                ".68f180a066e6e0a2753bfcc81c4697eb8558124b.torrent",
                ".690174964188ab44a9f4974a184ad0df1c5d63dd.torrent",
                ".69127f1b62ef0bb07aae89f62521e0185d29ae46.torrent",
                ".696e59761b05453b5cc095455177efd0d7d6dd32.torrent",
                ".6b7c9f4bfc86d7458d2f67028017681d148f8198.torrent",
                ".6bfd2437840dcebd476da15cb790932ba14071d2.torrent",
                ".71b21ea9ca418e19e84feb0f68f1e15ab9b6791e.torrent",
                ".72990320b72b8aa8e55b9d8e41e5e95326694117.torrent",
                ".736888c11e5345060f941f7e1dca8f2a32f33eb2.torrent",
                ".7606dec155a4f753225b1a827203589ecc17367c.torrent",
                ".7642bb81d2b2e4b0f92750fe31860d816ca8f38d.torrent",
                ".7ed4dd111db9f4c5db88aabe6731940032ddfd4c.torrent",
                ".7f11505a1e08d00c196dfc996b0c7ed63d1c8e7f.torrent",
                ".7faea0b963737a21a4d37945d1daa3228073d584.torrent",
                ".8016ca5b98dc871729626f818286a120b37314f4.torrent",
                ".818acc5e40fd406f86ac9d492ddd96f9285b0ec1.torrent",
                ".83b48e261a4ecffe3371c1667e91a5a865d345a7.torrent",
                ".84b2d970e7037db97592259517cb2adff3fd941e.torrent",
                ".84c836185e064b6c78252362da0e984dc7375427.torrent",
                ".84dd659310f90da53a577347fbc51de4adb493a6.torrent",
                ".85d150d085bf5d2daa151fb7fa2f81c97730b0c6.torrent",
                ".86b6913c5f6f7cda78103a8eed34b02e1578bd77.torrent",
                ".86e5730a7c41b9d2b81c17de10dd5ca708eb487a.torrent",
                ".87273ff2909503023c0aed224ca28d20fc5d00b6.torrent",
                ".87b2334fb934486347c4ba97010130e91a3d462c.torrent",
                ".88203c24cb0a4a3cf77c78d64bf02e013246c7a3.torrent",
                ".8c5171ee91b877a1246c2e207cd7acc0034fc315.torrent",
                ".8d25c72eb90370d0c57f0df61dd15934852917eb.torrent",
                ".8e9826b1e591413788b7c35107f5ffb11996ac4f.torrent",
                ".8f46e3909be616c898862534bcc0770607697499.torrent",
                ".92b36d7fdd627208f073cd18af1a64f0bc7e14f5.torrent",
                ".9428a1416a4b7fcc5fbacf2dfe60c97360bbcfbe.torrent",
                ".944dcf3fdf6a2828dcb62f003a3aab6534d42d6b.torrent",
                ".9470943fbae9dc433e2fddfe804bcd6ef3fbad64.torrent",
                ".9825ab454ced45551962abb7d7f1e463b4115731.torrent",
                ".9919f9f2fea6bcb1c466564e00954a49a156a26e.torrent",
                ".9d03cf2e649c4964fda58053c00b5412f82afad0.torrent",
                ".9d53298fc0d9d9f13a1e57dedc508e9c83ad38c9.torrent",
                ".9f3150a191b302c9ebd59d7dd28955b7caf475c4.torrent",
                ".9f6e815d3414881282b8de19d1c1a836da70b8de.torrent",
                ".9f9fa2ab9374bebb225715941f581fe93a35db9e.torrent",
                ".a2c31f886cb08e63fcb67556bdad9870cbb78184.torrent",
                ".a4b466fa6804ce761d92df767db2dca71647da8a.torrent",
                ".a509b662d048e571ecef20339663ba9a4207e728.torrent",
                ".a5912a09169fadda0239d97e440a0cc45cd64815.torrent",
                ".a634addd98a7a653b94b210206c1961cf9c0e19e.torrent",
                ".a9198a0c8e0c2b352e86fb8d6d15210b79511a68.torrent",
                ".aa720288cc4382635770e501a819857a617af638.torrent",
                ".ac233f0d2429be6792389e4f332c584eb2b83e89.torrent",
                ".ac953bb85401ad601186153815f705ac8eaf9dea.torrent",
                ".acf61c760f8a13eba75638e0b1eb59a26542370f.torrent",
                ".ad0d54bd65cf231495ae90c4c0ca73185e038152.torrent",
                ".af75b2bd66d4cd22325adf35ac40b3d6a453f57a.torrent",
                ".b35113ac75e4728e8b9f0db9be38b9e1afcb05d4.torrent",
                ".b46a186925fca6d14e1aff5747548c428d712746.torrent",
                ".b494afeba19831558061a5c7cfeb767e4a2ce854.torrent",
                ".b57c34afdfa9d7fcb9d543c6437c51cb710570d0.torrent",
                ".b83e62e8f004bafba18271dc1574fef253a10a95.torrent",
                ".ba445b26ea507da1dca7e67f77d09c7b6d426e82.torrent",
                ".bb71ce4b369b7190dc43980dc8c8a98a5c561e7c.torrent",
                ".bc081a7fc6d03c8a7953d035ec5eb199158592bf.torrent",
                ".bcfc45166869df14b2021befbcc057a41f8131d0.torrent",
                ".bee43d2b3732bda8d50d3aeac4c92c3e237bbe9d.torrent",
                ".c950d1200a76f7b6a7bd1a780c6bc78d2cb5ef04.torrent",
                ".cb72ccdc069d7653b1aceb699f87ed262cf3d463.torrent",
                ".ccc0d039f7cd23e0070244828da19ba49fab9e76.torrent",
                ".d0ff9fe49c47995b07fdb59ad4accde86cfe577a.torrent",
                ".d1170be43a4a0b6577eec1bfa672b932b0b152aa.torrent",
                ".d43b6285936cc79a7e944e0c5fbc178661a3dbf2.torrent",
                ".d6c4a9967443723877b1ca1add3bf7f1c9dd27b5.torrent",
                ".d7b9a6c6dc385655df2b62dfd3ed69dfbf492d7f.torrent",
                ".db26f9ce27d346a890d221822c7fefdb7694f189.torrent",
                ".db434fa09dac8a9373250dea39fe3e1f8be21973.torrent",
                ".dbdcfb93bae077f7b7aed8027381a92dd5ebdc48.torrent",
                ".dffca03f0fc7c47fede1632e30a3bc21663ff816.torrent",
                ".e0765c89d6e03a5d5c4eecac2316eed6bf53d7e6.torrent",
                ".e16dd63d3367640150b81c6da336910e0871a68e.torrent",
                ".e4d8b7639b9478fc0ca0852e7e3c73d01ce6b0d8.torrent",
                ".e5021821ba4b5816563202eb24dfd012e53ff1a7.torrent",
                ".e6ed5d68133726707e02065e1900f92ee258d0fd.torrent",
                ".e6f7245ea29208fc70553299aeb4f2c0391ec11b.torrent",
                ".eab582a62cdfdbe8aebffc8c9b89123f004c5b0a.torrent",
                ".ec36ef151f5c426d51931da4db40a93c3fdfd0a4.torrent",
                ".eeb2ad5a426f4036bdc04b19d2dd01d8f60313c5.torrent",
                ".f257bed0f37188bdb7c2743ce0c1f4347ca1b49d.torrent",
                ".f3222ca70f58c17ea81b432d2d2abfe71590a3e1.torrent",
                ".f3d895712172b72789f44368470df29838751f1a.torrent",
                ".f703a5dcbfdd4536c908dd2bc6392d2a47f93658.torrent",
                ".f7e2390e4170ae6cd157369bc75eff6905d12475.torrent",
                ".fcba02824e91e14d2c91bd53a2c20e4a1caa55af.torrent",
                ".fcfb8b284b34156c80e5ca7e52fe49e57f317681.torrent",
                ".fe65ca031c48c15fbcf1371b9cf47d8980cbe497.torrent"]

    # for torrent in torrents:
    #     run(torrent)
    
    print(passwd)
    # parser=Parser('.fe65ca031c48c15fbcf1371b9cf47d8980cbe497.torrent')

    # print(parser.getInfoFiles()[0]['path'][0])
    # print(parser.getInfoFiles()[0]['length'])

#https://blog.csdn.net/iloster/article/details/24363935