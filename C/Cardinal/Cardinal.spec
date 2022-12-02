
%define _unpackaged_files_terminate_build 1

Name:     Cardinal
Version:  22.11
Release:  alt1

Summary:  Virtual modular synthesizer plugin
License:  GPL-3.0-or-later
Group:    Sound
Url:      https://github.com/DISTRHO/Cardinal

ExclusiveArch: x86_64 aarch64

Source:   %name-%version.tar

# Sources from sub-merge {{{
# https://github.com/VCVRack/Rack.git
Source100: Rack-5551617afff182925940908eaf73a7d7361303cc.tar
# https://github.com/VCVRack/nanovg.git
Source101: nanovg-0bebdb314aff9cfa28fde4744bcb037a2b3fd756.tar
# https://github.com/memononen/nanosvg.git
Source102: nanosvg-25241c5a8f8451d41ab1b02ab2d865b01600d949.tar
# https://github.com/AndrewBelt/osdialog.git
Source103: osdialog-21b9dcc2a1bbdacb9b46da477ffd82a4ce9204b9.tar
# https://github.com/VCVRack/oui-blendish.git
Source104: oui-blendish-2fc6405883f8451944ed080547d073c8f9f31898.tar
# https://github.com/VCVRack/rtaudio.git
Source105: rtaudio-ece277bd839603648c80c8a5f145678e13bc23f3.tar
# https://github.com/VCVRack/glfw.git
Source106: glfw-d46b57cdb16e521c8cf4290c9022278863a84022.tar
# https://bitbucket.org/j_norberg/fuzzysearchdatabase.git
Source107: fuzzysearchdatabase-fe62479811e503ef3c091f5a859d27bfcf0a44da.tar
# https://github.com/gulrak/filesystem.git
Source108: filesystem-7e37433f318488ae4bc80f80e12df12a01579874.tar
# https://bitbucket.org/jpommier/pffft.git
Source109: pffft-74d7261be17cf659d5930d4830609406bd7553e3.tar
# https://github.com/VCVRack/rtmidi.git
Source110: rtmidi-2c5b0778e38b5030afc80c8e9d7adc9b58ef650e.tar
# https://github.com/DISTRHO/DPF.git
Source111: DPF-5ee7fab819433f1338e5290a0e03b358c59c44f3.tar
# https://github.com/DISTRHO/pugl.git
Source112: pugl-3e03459a5a0b0f118b04e9e0b0a32f42ccd04a5c.tar
# https://github.com/VCVRack/Befaco.git
Source113: Befaco-dcd9a59ea785d7efebd39ea5564823c72f2fdddf.tar
# https://github.com/CardinalModules/AudibleInstruments.git
Source114: AudibleInstruments-1f279a02d955667341d08f74ddf2054d10e82c65.tar
# https://github.com/CardinalModules/eurorack.git
Source115: eurorack-8f8800304ccbcff37a01cedc59bdd8cf5a564cf1.tar
# https://github.com/pichenettes/avril.git
Source116: avril-276b2887e4110ca913294fcbb313163dfb28a448.tar
# https://github.com/pichenettes/avrilx.git
Source117: avrilx-868d6e74eb8555f9575b5149202256156e5c03fa.tar
# https://github.com/pichenettes/stmlib.git
Source118: stmlib-8998429236d6edd4934b6c9ae8e0f167e3d30aa7.tar
# https://github.com/pichenettes/stm-audio-bootloader.git
Source119: stm-audio-bootloader-1ec7d6374e2d305cb710170eb80de9b66e795792.tar
# https://github.com/pichenettes/avr-audio-bootloader.git
Source120: avr-audio-bootloader-0de2be5928afdf7fb3e5ada60544ed6c15ab808f.tar
# https://github.com/AnimatedCircuits/RackModules.git
Source121: RackModules-bf78cd8ed22970fe9dc5ebff8e3907898904c747.tar
# https://github.com/mhampton/ZetaCarinaeModules.git
Source122: ZetaCarinaeModules-7fa3a59e71cf5f541a335e89bc45102923a3fd62.tar
# https://github.com/dbgrande/GrandeModular.git
Source123: GrandeModular-3d6524320ce33569e3553a53571c45425ba5d078.tar
# https://github.com/bogaudio/BogaudioModules.git
Source124: BogaudioModules-4af2e2d38004b98645deb8a25c7ec74c7c8f1a03.tar
# https://github.com/CardinalModules/Bidoo.git
Source125: Bidoo-8610d4c86740d9d67ebfa4ded70279df7aeb95be.tar
# https://github.com/VCVRack/ESeries.git
Source126: ESeries-cb665989f48db6c4fe96924b9e42c804ee15d5cf.tar
# https://github.com/jeremywen/JW-Modules.git
Source127: JW-Modules-356588ddb142dab99837af58681bc0d8afb88e4c.tar
# https://github.com/CardinalModules/rackwindows.git
Source128: rackwindows-60dfe5dff94b82fc42a43d971e41e64e296b0220.tar
# https://github.com/MarcBoule/ImpromptuModular.git
Source129: ImpromptuModular-eb514f1e867a5626918dd70b947908b3181f66b8.tar
# https://github.com/jhoar/AmalgamatedHarmonics.git
Source130: AmalgamatedHarmonics-97700c06af7df4d8fcf173ae3670b7907a682627.tar
# https://github.com/CardinalModules/cf.git
Source131: cf-b6c4a66ffc153d78c7efa00fa886657eb182b15d.tar
# https://github.com/MarcBoule/MindMeldModular.git
Source132: MindMeldModular-8e413a445c1c307f356ee96633b7f6f2b4c4749e.tar
# https://github.com/ValleyAudio/ValleyRackFree.git
Source133: ValleyRackFree-b2ed19ad46e91c650d0ba3e18eae9a1bbecb1f3c.tar
# https://github.com/SVModular/DrumKit.git
Source134: DrumKit-f2a7d717e2ae066ba0127fa5ffade775baba1512.tar
# https://github.com/JerrySievert/SynthDevKit.git
Source135: SynthDevKit-0f322e58f00f1a04276ecc3eadb610b418f040d5.tar
# https://github.com/falkTX/Carla.git
Source136: Carla-aa400535b31c67f4b6c1b28e6e20e4d4f82111a3.tar
# https://github.com/falkTX/Carla-Plugins
Source137: Carla-Plugins-e32f21fe9947740592f29401ff2b3f1f951c1d56.tar
# https://github.com/CardinalModules/mscHack.git
Source138: mscHack-80883512cc397c173e40e3bc014640b838ab343a.tar
# https://github.com/zezic/ZZC.git
Source139: ZZC-15364616da500d31f7545dcbfc01b4fda7f7c9d4.tar
# https://github.com/wiqid/repelzen.git
Source140: repelzen-428f76c3509e4d71489daf075c48ae4b995a0786.tar
# https://github.com/CardinalModules/AriaModules.git
Source141: AriaModules-269ab0f091b18f08ab253bd8af4866e78d770bc0.tar
# https://github.com/baconpaul/BaconPlugs.git
Source142: BaconPlugs-adf84fc00a953f8e8a1b378531a08ee68b9a68d7.tar
# https://github.com/craigsapp/midifile.git
Source143: midifile-99e87b684f88ebff6417ef25f269f1a95b780ad2.tar
# https://github.com/RCameron93/FehlerFabrik.git
Source144: FehlerFabrik-9b5897828dc1b757f42cb707b5979488acb67401.tar
# https://gitlab.com/sonusdept/sonusmodular.git
Source145: sonusmodular-407829b0341dc04aa8530bd14a739c9f222930ed.tar
# https://github.com/JustMog/Mog-VCV.git
Source146: Mog-VCV-00a7e3b01f56da5cfc86720ae6951ecdf8953ee5.tar
# https://github.com/jatinchowdhury18/ChowDSP-VCV.git
Source147: ChowDSP-VCV-871f712f3eb95ada1c34bf3d8170690eb4aec8d0.tar
# https://github.com/Chowdhury-DSP/chowdsp_utils
Source148: chowdsp_utils-505052501fb64b38519101478628ec5ea32d6a43.tar
# https://github.com/gluethegiant/gtg-rack.git
Source149: gtg-rack-5f05d62ddc2773098daf1044eb6698581acd4eb6.tar
# https://github.com/mhetrick/hetrickcv.git
Source150: hetrickcv-2fc83df75154c32b83addd3ed68b35eb6156ca0d.tar
# https://github.com/LancePutnam/Gamma.git
Source151: Gamma-70ba31c92db6afa160523940fd046a2bc249e8ad.tar
# https://github.com/VegaDeftwing/LyraeModules.git
Source152: LyraeModules-b21cbe8ee25ddf2a927e0b4ec9f2c97c115857af.tar
# https://github.com/mgunyho/Little-Utils.git
Source153: Little-Utils-b7ce2244835fa376201b21b2274937152dcd1121.tar
# https://github.com/SteveRussell33/Prism.git
Source154: Prism-8d2796da76e5d7f79bbf461c95a7858035bb0736.tar
# https://github.com/EaterOfSheep/Extratone.git
Source155: Extratone-9fb70500b17fe2495aba9f5f77ddf496d5c09f13.tar
# https://github.com/SteveRussell33/LifeFormModular.git
Source156: LifeFormModular-c7b8d096f618c421d7d45784b894c0ac2f3395b0.tar
# https://github.com/netboy3/21kHz-rack-plugins.git
Source157: 21kHz-rack-plugins-0bee82247151e2fe2885f1e15fbbd74ddb4f48d0.tar
# https://github.com/DISTRHO/PawPaw.git
Source158: PawPaw-1fcfa969e98624dd3d98a30a0925eb1c3991e4d2.tar
# https://github.com/LomasModules/LomasModules.git
Source159: LomasModules-b714cdb0c662503bc6cf60c06765b426a4caa17f.tar
# https://github.com/expertsleepersltd/vcvrack-encoders.git
Source160: vcvrack-encoders-95496e8a955407889bbab94cf404cf356802bb76.tar
# https://github.com/CardinalModules/ihtsyn.git
Source161: ihtsyn-1b77e3c3ba12734bbd29a4aa59dd408e679b5cf7.tar
# https://github.com/JerrySievert/QuickJS.git
Source162: QuickJS-f7bada076e2536fbc4ca46b81a34fa27990ffc30.tar
# https://github.com/NikolaiVChr/Autinn.git
Source163: Autinn-bc880d9d8fb59016de61e3253aff2b543d7bb665.tar
# https://github.com/MockbaTheBorg/MockbaModular.git
Source164: MockbaModular-479d2c8007b2087cdf557a491df25c5b85784a96.tar
# https://github.com/8Mode/8Mode-VCV_Modules.git
Source165: 8Mode-VCV_Modules-fe5a642ee0a455e882e105f422cf85f7e83fd31f.tar
# https://github.com/kauewerner/Axioma.git
Source166: Axioma-3e7e01e6a449dc1e6c523bd4487c0a3200b322cb.tar
# https://github.com/jensschulze/GoodSheperd.git
Source167: GoodSheperd-636351059f2eec629f3b8a537451dd3d0eb01c30.tar
# https://gitlab.com/hampton-harmonics/hampton-harmonics-modules.git
Source168: hampton-harmonics-modules-e5cf81f1c356fdc98fd08584146cda8af7e16b1f.tar
# https://github.com/martin-lueders/ML_modules.git
Source169: ML_modules-311042275900650c0b0cc57fcd2b57333820adde.tar
# https://github.com/RareBreeds/Orbits.git
Source170: Orbits-ff0c007feb9ed1de57ea246f86e8b2b68572f5e6.tar
# https://github.com/aptrn/stocaudio-modules.git
Source171: stocaudio-modules-ed5c85b0d9391c37f4ec4d9de4ef8aa30d94bcd6.tar
# https://github.com/catronomix/catro-modulo.git
Source172: catro-modulo-bf6f969c5f7fff6a419a54197fb4318671281ad5.tar
# https://github.com/grough/lilac-loop-vcv.git
Source173: lilac-loop-vcv-cf9bb5cfa5fd41ecfc9976bb106c2f4a7667c9d7.tar
# https://github.com/janne808/kocmoc-rack-modules.git
Source174: kocmoc-rack-modules-eb46ce3a8b5795d61c2e3eb60f6ca58799a8cee2.tar
# https://github.com/patheros/PathSetModules.git
Source175: PathSetModules-30e35f9414329ed6545ef328fd5951d4cf583362.tar
# https://github.com/algoritmarte/AlgoritmarteVCVPlugin.git
Source176: AlgoritmarteVCVPlugin-9d41fe882ab5029100b55c98ba7f10172d452795.tar
# https://github.com/aaronstatic/AaronStatic_modules.git
Source177: AaronStatic_modules-4ace0a1789c577ee4eb12dc03da5271f80598d62.tar
# https://github.com/netboy3/MSM-vcvrack-plugin.git
Source178: MSM-vcvrack-plugin-3315c11e8506c28cece304fe4b772383a2820f86.tar
# https://github.com/mhetrick/nonlinearcircuits.git
Source179: nonlinearcircuits-57eb090f233c21b2edee541ea17d800f22045d91.tar
# https://github.com/clone45/voxglitch.git
Source180: voxglitch-55186974eeb6c068f2687d7bb4f5c5e1884bf7da.tar
# https://github.com/CardinalModules/ArableInstruments.git
Source181: ArableInstruments-a2de62d0c3b9f764ce6b42441366788d1e52bfcc.tar
# https://github.com/CardinalModules/eurorack.git
Source182: eurorack-87bf3b1da88147e3fcc8c57e3072eec67ccd380a.tar
# https://github.com/pichenettes/avril.git
Source183: avril-276b2887e4110ca913294fcbb313163dfb28a448.tar
# https://github.com/pichenettes/avrilx.git
Source184: avrilx-868d6e74eb8555f9575b5149202256156e5c03fa.tar
# https://github.com/pichenettes/stmlib.git
Source185: stmlib-8998429236d6edd4934b6c9ae8e0f167e3d30aa7.tar
# https://github.com/pichenettes/stm-audio-bootloader.git
Source186: stm-audio-bootloader-1ec7d6374e2d305cb710170eb80de9b66e795792.tar
# https://github.com/pichenettes/avr-audio-bootloader.git
Source187: avr-audio-bootloader-0de2be5928afdf7fb3e5ada60544ed6c15ab808f.tar
# https://github.com/pichenettes/avril.git
Source188: avril-36b988a851f8638adb9f53ff98939cb08ffce8cc.tar
# https://github.com/pichenettes/avrilx.git
Source189: avrilx-5c28367e91dfb036593e876c886241cf81f60a2d.tar
# https://github.com/pichenettes/stm-audio-bootloader.git
Source190: stm-audio-bootloader-6f20ead22a28967b0446546d2fcf0dfb9599ba93.tar
# https://github.com/pichenettes/avr-audio-bootloader.git
Source191: avr-audio-bootloader-52754f878b4883adf565bc3ddf691c5e1c4a9f6d.tar
# https://github.com/mqtthiqs/stmlib.git
Source192: stmlib-8ab2aaee77cbacb47b646d46d22ee5d358effe2d.tar
# https://github.com/CardinalModules/Fundamental.git
Source193: Fundamental-63d54b6575657c8bd8d221178253c750baf0ed3b.tar
# https://gitlab.com/unlessgames/unless_modules.git
Source194: unless_modules-7c15142c4e7adb174f92d7ad54c819970ac4bda4.tar
# https://github.com/VegaDeftwing/PinkTromboneVCV.git
Source195: PinkTromboneVCV-1e96d7b898eca6101f438dfd8224d713985486e2.tar
# https://github.com/knchaffin/Meander.git
Source196: Meander-b36865978358ffdbeb80ad603c4c54f5a535107a.tar
# https://github.com/korfuri/WhatTheRack.git
Source197: WhatTheRack-e373378491d2cf3b8257137d154aef1d389c5204.tar
# https://github.com/AScustomWorks/AS.git
Source198: AS-b5fdb76c79688207e56bd5b07b01e9c63a102797.tar
# https://github.com/gosub/forsitan-modulare.git
Source199: forsitan-modulare-056cc2ec9186a4175d9214eee91e4ff5cc2e5fb1.tar
# https://github.com/Ahineya/vcv-myth-plugin.git
Source200: vcv-myth-plugin-e511dd95eca830ee74fef23bddc195696603125f.tar
# https://github.com/alefnull/alefsbits.git
Source201: alefsbits-af534ff487db6689c3be527f5acb34ea90efc195.tar
# https://github.com/hannakoppelaar/h4n4-modules.git
Source202: h4n4-modules-bb1b15870d9dad4dd8a562957f45c2383506795d.tar
# https://github.com/dBiz/dBiz.git
Source203: dBiz-88f1bd64cff6e96a1a48566a1692de86b9a7de2a.tar
# https://github.com/simd-everywhere/simde.git
Source204: simde-12069d720f43830ae9791e8b0f4c4fa3c88012a0.tar
# https://github.com/nemequ/munit.git
Source205: munit-da8f73412998e4f1adf1100dc187533a51af77fd.tar
# https://github.com/hemmer/rebel-tech-vcv.git
Source206: rebel-tech-vcv-6ac79f59c5b95433d82bcc759c4cd0642ec35098.tar
# }}}

Patch1:   Cardinal-22.07-alt-lv2-in-lib64.patch
Patch2:   Cardinal-22.11-rebeltech-fix-compilation.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(liblo)
BuildRequires: pkgconfig(libpulse-simple)
BuildRequires: pkgconfig(lv2)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xrandr)

Requires: %name-common = %EVR

%description
Cardinal is a free and open-source virtual modular synthesizer
plugin. It is based on the popular VCV Rack but with a focus on
being a fully self-contained plugin version. More specifically,
this is a DPF-based plugin wrapper around VCV Rack, using its code
directly instead of forking the project, with the target of having
a proper, self-contained, fully free and open-source plugin version
of Rack.

Cardinal contains Rack, some 3rd-party modules and a few internal
utilities all in a single binary.

This package provides Cardinal as standalone jack client.


%package -n lv2-Cardinal-plugins
Group:    Sound
Summary:  Virtual modular synthesizer -- LV2 plugin
Requires: %name-common = %EVR

%description -n lv2-Cardinal-plugins
Cardinal is a free and open-source virtual modular synthesizer
plugin. It is based on the popular VCV Rack but with a focus on
being a fully self-contained plugin version. More specifically,
this is a DPF-based plugin wrapper around VCV Rack, using its code
directly instead of forking the project, with the target of having
a proper, self-contained, fully free and open-source plugin version
of Rack.

Cardinal contains Rack, some 3rd-party modules and a few internal
utilities all in a single binary.

This package provides Cardinal as LV2 plugin.


%package common
Group:    Sound
Summary:  Virtual modular synthesizer -- resources
BuildArch: noarch

%description common
Cardinal is a free and open-source virtual modular synthesizer
plugin. It is based on the popular VCV Rack but with a focus on
being a fully self-contained plugin version. More specifically,
this is a DPF-based plugin wrapper around VCV Rack, using its code
directly instead of forking the project, with the target of having
a proper, self-contained, fully free and open-source plugin version
of Rack.

Cardinal contains Rack, some 3rd-party modules and a few internal
utilities all in a single binary.

This package contains common resources for Cardinal.


%prep
%setup

# Tarballs from sub-merge {{{
tar -xf %SOURCE100 -C 'src/Rack' --strip-components 1
tar -xf %SOURCE101 -C 'src/Rack/dep/nanovg' --strip-components 1
tar -xf %SOURCE102 -C 'src/Rack/dep/nanosvg' --strip-components 1
tar -xf %SOURCE103 -C 'src/Rack/dep/osdialog' --strip-components 1
tar -xf %SOURCE104 -C 'src/Rack/dep/oui-blendish' --strip-components 1
tar -xf %SOURCE105 -C 'src/Rack/dep/rtaudio' --strip-components 1
tar -xf %SOURCE106 -C 'src/Rack/dep/glfw' --strip-components 1
tar -xf %SOURCE107 -C 'src/Rack/dep/fuzzysearchdatabase' --strip-components 1
tar -xf %SOURCE108 -C 'src/Rack/dep/filesystem' --strip-components 1
tar -xf %SOURCE109 -C 'src/Rack/dep/pffft' --strip-components 1
tar -xf %SOURCE110 -C 'src/Rack/dep/rtmidi' --strip-components 1
tar -xf %SOURCE111 -C 'dpf' --strip-components 1
tar -xf %SOURCE112 -C 'dpf/dgl/src/pugl-upstream' --strip-components 1
tar -xf %SOURCE113 -C 'plugins/Befaco' --strip-components 1
tar -xf %SOURCE114 -C 'plugins/AudibleInstruments' --strip-components 1
tar -xf %SOURCE115 -C 'plugins/AudibleInstruments/eurorack' --strip-components 1
tar -xf %SOURCE116 -C 'plugins/AudibleInstruments/eurorack/avrlib' --strip-components 1
tar -xf %SOURCE117 -C 'plugins/AudibleInstruments/eurorack/avrlibx' --strip-components 1
tar -xf %SOURCE118 -C 'plugins/AudibleInstruments/eurorack/stmlib' --strip-components 1
tar -xf %SOURCE119 -C 'plugins/AudibleInstruments/eurorack/stm_audio_bootloader' --strip-components 1
tar -xf %SOURCE120 -C 'plugins/AudibleInstruments/eurorack/avr_audio_bootloader' --strip-components 1
tar -xf %SOURCE121 -C 'plugins/AnimatedCircuits' --strip-components 1
tar -xf %SOURCE122 -C 'plugins/ZetaCarinaeModules' --strip-components 1
tar -xf %SOURCE123 -C 'plugins/GrandeModular' --strip-components 1
tar -xf %SOURCE124 -C 'plugins/BogaudioModules' --strip-components 1
tar -xf %SOURCE125 -C 'plugins/Bidoo' --strip-components 1
tar -xf %SOURCE126 -C 'plugins/ESeries' --strip-components 1
tar -xf %SOURCE127 -C 'plugins/JW-Modules' --strip-components 1
tar -xf %SOURCE128 -C 'plugins/rackwindows' --strip-components 1
tar -xf %SOURCE129 -C 'plugins/ImpromptuModular' --strip-components 1
tar -xf %SOURCE130 -C 'plugins/AmalgamatedHarmonics' --strip-components 1
tar -xf %SOURCE131 -C 'plugins/cf' --strip-components 1
tar -xf %SOURCE132 -C 'plugins/MindMeldModular' --strip-components 1
tar -xf %SOURCE133 -C 'plugins/ValleyAudio' --strip-components 1
tar -xf %SOURCE134 -C 'plugins/DrumKit' --strip-components 1
tar -xf %SOURCE135 -C 'plugins/DrumKit/deps/SynthDevKit' --strip-components 1
tar -xf %SOURCE136 -C 'carla' --strip-components 1
tar -xf %SOURCE137 -C 'carla/source/native-plugins/external' --strip-components 1
tar -xf %SOURCE138 -C 'plugins/mscHack' --strip-components 1
tar -xf %SOURCE139 -C 'plugins/ZZC' --strip-components 1
tar -xf %SOURCE140 -C 'plugins/repelzen' --strip-components 1
tar -xf %SOURCE141 -C 'plugins/AriaModules' --strip-components 1
tar -xf %SOURCE142 -C 'plugins/BaconPlugs' --strip-components 1
tar -xf %SOURCE143 -C 'plugins/BaconPlugs/libs/midifile' --strip-components 1
tar -xf %SOURCE144 -C 'plugins/FehlerFabrik' --strip-components 1
tar -xf %SOURCE145 -C 'plugins/sonusmodular' --strip-components 1
tar -xf %SOURCE146 -C 'plugins/Mog' --strip-components 1
tar -xf %SOURCE147 -C 'plugins/ChowDSP' --strip-components 1
tar -xf %SOURCE148 -C 'plugins/ChowDSP/lib/chowdsp_utils' --strip-components 1
tar -xf %SOURCE149 -C 'plugins/GlueTheGiant' --strip-components 1
tar -xf %SOURCE150 -C 'plugins/HetrickCV' --strip-components 1
tar -xf %SOURCE151 -C 'plugins/HetrickCV/Gamma' --strip-components 1
tar -xf %SOURCE152 -C 'plugins/LyraeModules' --strip-components 1
tar -xf %SOURCE153 -C 'plugins/LittleUtils' --strip-components 1
tar -xf %SOURCE154 -C 'plugins/Prism' --strip-components 1
tar -xf %SOURCE155 -C 'plugins/Extratone' --strip-components 1
tar -xf %SOURCE156 -C 'plugins/LifeFormModular' --strip-components 1
tar -xf %SOURCE157 -C 'plugins/21kHz' --strip-components 1
tar -xf %SOURCE158 -C 'deps/PawPaw' --strip-components 1
tar -xf %SOURCE159 -C 'plugins/LomasModules' --strip-components 1
tar -xf %SOURCE160 -C 'plugins/ExpertSleepers-Encoders' --strip-components 1
tar -xf %SOURCE161 -C 'plugins/ihtsyn' --strip-components 1
tar -xf %SOURCE162 -C 'deps/QuickJS' --strip-components 1
tar -xf %SOURCE163 -C 'plugins/Autinn' --strip-components 1
tar -xf %SOURCE164 -C 'plugins/MockbaModular' --strip-components 1
tar -xf %SOURCE165 -C 'plugins/8Mode' --strip-components 1
tar -xf %SOURCE166 -C 'plugins/Axioma' --strip-components 1
tar -xf %SOURCE167 -C 'plugins/GoodSheperd' --strip-components 1
tar -xf %SOURCE168 -C 'plugins/HamptonHarmonics' --strip-components 1
tar -xf %SOURCE169 -C 'plugins/ML_modules' --strip-components 1
tar -xf %SOURCE170 -C 'plugins/Orbits' --strip-components 1
tar -xf %SOURCE171 -C 'plugins/stocaudio' --strip-components 1
tar -xf %SOURCE172 -C 'plugins/CatroModulo' --strip-components 1
tar -xf %SOURCE173 -C 'plugins/LilacLoop' --strip-components 1
tar -xf %SOURCE174 -C 'plugins/kocmoc' --strip-components 1
tar -xf %SOURCE175 -C 'plugins/PathSet' --strip-components 1
tar -xf %SOURCE176 -C 'plugins/Algoritmarte' --strip-components 1
tar -xf %SOURCE177 -C 'plugins/AaronStatic' --strip-components 1
tar -xf %SOURCE178 -C 'plugins/MSM' --strip-components 1
tar -xf %SOURCE179 -C 'plugins/nonlinearcircuits' --strip-components 1
tar -xf %SOURCE180 -C 'plugins/voxglitch' --strip-components 1
tar -xf %SOURCE181 -C 'plugins/ArableInstruments' --strip-components 1
tar -xf %SOURCE182 -C 'plugins/ArableInstruments/eurorack' --strip-components 1
tar -xf %SOURCE183 -C 'plugins/ArableInstruments/eurorack/avrlib' --strip-components 1
tar -xf %SOURCE184 -C 'plugins/ArableInstruments/eurorack/avrlibx' --strip-components 1
tar -xf %SOURCE185 -C 'plugins/ArableInstruments/eurorack/stmlib' --strip-components 1
tar -xf %SOURCE186 -C 'plugins/ArableInstruments/eurorack/stm_audio_bootloader' --strip-components 1
tar -xf %SOURCE187 -C 'plugins/ArableInstruments/eurorack/avr_audio_bootloader' --strip-components 1
tar -xf %SOURCE188 -C 'plugins/ArableInstruments/parasites/avrlib' --strip-components 1
tar -xf %SOURCE189 -C 'plugins/ArableInstruments/parasites/avrlibx' --strip-components 1
tar -xf %SOURCE190 -C 'plugins/ArableInstruments/parasites/stm_audio_bootloader' --strip-components 1
tar -xf %SOURCE191 -C 'plugins/ArableInstruments/parasites/avr_audio_bootloader' --strip-components 1
tar -xf %SOURCE192 -C 'plugins/ArableInstruments/parasites/stmlib' --strip-components 1
tar -xf %SOURCE193 -C 'plugins/Fundamental' --strip-components 1
tar -xf %SOURCE194 -C 'plugins/unless_modules' --strip-components 1
tar -xf %SOURCE195 -C 'plugins/PinkTrombone' --strip-components 1
tar -xf %SOURCE196 -C 'plugins/Meander' --strip-components 1
tar -xf %SOURCE197 -C 'plugins/WhatTheRack' --strip-components 1
tar -xf %SOURCE198 -C 'plugins/AS' --strip-components 1
tar -xf %SOURCE199 -C 'plugins/forsitan-modulare' --strip-components 1
tar -xf %SOURCE200 -C 'plugins/myth-modules' --strip-components 1
tar -xf %SOURCE201 -C 'plugins/alefsbits' --strip-components 1
tar -xf %SOURCE202 -C 'plugins/h4n4-modules' --strip-components 1
tar -xf %SOURCE203 -C 'plugins/dBiz' --strip-components 1
tar -xf %SOURCE204 -C 'include/simde' --strip-components 1
tar -xf %SOURCE205 -C 'include/simde/test/munit' --strip-components 1
tar -xf %SOURCE206 -C 'plugins/RebelTech' --strip-components 1
# }}}

# don't build VST plugin variants
sed -i '/^TARGETS/ s/vst[23]\|clap//g' src/Makefile.cardinal.mk

%autopatch -p0

%build
%make_build \
    NOOPT=true \
    SKIP_STRIPPING=true \
    PREFIX=/usr \
    SYSDEPS=true \
    WITH_LTO=true \
    AR=gcc-ar \
    VERBOSE=1

%install
# standalone
install -Dm755 bin/Cardinal %buildroot%_bindir/Cardinal

# resources
install -d %buildroot%_datadir/cardinal/
cp -rL bin/Cardinal.lv2/resources/* %buildroot%_datadir/cardinal/

# lv2
for plugin in Cardinal CardinalFX CardinalSynth; do
    src="bin/$plugin.lv2"
    dst="%buildroot%_libdir/lv2/$plugin.lv2"

    install -d "$dst"
    install -m644 "$src"/*.so "$dst"
    install -m644 "$src"/*.ttl "$dst"
    ln -sr %buildroot%_datadir/cardinal/ "$dst"/resources
done

# docs
install -d %buildroot%_datadir/doc/cardinal/docs
install -m 644 README.md %buildroot%_datadir/doc/cardinal/
install -m 644 docs/*.md docs/*.png %buildroot%_datadir/doc/cardinal/docs/


%files
%_bindir/*

%files -n lv2-Cardinal-plugins
%_libdir/lv2/*

%files common
%_datadir/cardinal
%doc %_datadir/doc/cardinal

%changelog
* Mon Nov 28 2022 Ivan A. Melnikov <iv@altlinux.org> 22.11-alt1
- 22.11

* Sat Oct 15 2022 Ivan A. Melnikov <iv@altlinux.org> 22.10-alt1
- 22.10

* Mon Sep 19 2022 Ivan A. Melnikov <iv@altlinux.org> 22.09-alt1
- 22.09

* Wed Aug 10 2022 Ivan A. Melnikov <iv@altlinux.org> 22.07-alt2
- Fix build with LTO on certain systems

* Mon Aug 08 2022 Ivan A. Melnikov <iv@altlinux.org> 22.07-alt1
- Initial build for Sisyphus
