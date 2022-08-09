
%define _unpackaged_files_terminate_build 1

Name:     Cardinal
Version:  22.07
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
Source111: DPF-0c0a4e401c2a552145720904b916da21846c8fc1.tar
# https://github.com/DISTRHO/pugl.git
Source112: pugl-856c759e1e360b0a766f61bb2b2cfffe15790368.tar
# https://github.com/DLTcollab/sse2neon.git
Source113: sse2neon-1dfa40113a03a682dc79ba42235c5b0d1c50aaf2.tar
# https://github.com/VCVRack/Befaco.git
Source114: Befaco-dcd9a59ea785d7efebd39ea5564823c72f2fdddf.tar
# https://github.com/CardinalModules/AudibleInstruments.git
Source115: AudibleInstruments-2a19bb25c0da725756390ad96dca55632800c74d.tar
# https://github.com/CardinalModules/eurorack.git
Source116: eurorack-8f8800304ccbcff37a01cedc59bdd8cf5a564cf1.tar
# https://github.com/pichenettes/avril.git
Source117: avril-276b2887e4110ca913294fcbb313163dfb28a448.tar
# https://github.com/pichenettes/avrilx.git
Source118: avrilx-868d6e74eb8555f9575b5149202256156e5c03fa.tar
# https://github.com/pichenettes/stmlib.git
Source119: stmlib-8998429236d6edd4934b6c9ae8e0f167e3d30aa7.tar
# https://github.com/pichenettes/stm-audio-bootloader.git
Source120: stm-audio-bootloader-1ec7d6374e2d305cb710170eb80de9b66e795792.tar
# https://github.com/pichenettes/avr-audio-bootloader.git
Source121: avr-audio-bootloader-0de2be5928afdf7fb3e5ada60544ed6c15ab808f.tar
# https://github.com/AnimatedCircuits/RackModules.git
Source122: RackModules-76c2912fd6ebdd7c3e33fca88096bea9c67209a1.tar
# https://github.com/mhampton/ZetaCarinaeModules.git
Source123: ZetaCarinaeModules-7fa3a59e71cf5f541a335e89bc45102923a3fd62.tar
# https://github.com/dbgrande/GrandeModular.git
Source124: GrandeModular-3d6524320ce33569e3553a53571c45425ba5d078.tar
# https://github.com/bogaudio/BogaudioModules.git
Source125: BogaudioModules-4af2e2d38004b98645deb8a25c7ec74c7c8f1a03.tar
# https://github.com/CardinalModules/Bidoo.git
Source126: Bidoo-7579f13bffc11548c857393408f3c2e030ee2483.tar
# https://github.com/VCVRack/ESeries.git
Source127: ESeries-cb665989f48db6c4fe96924b9e42c804ee15d5cf.tar
# https://github.com/jeremywen/JW-Modules.git
Source128: JW-Modules-f7399c473735c0a5bec95bb40953e781f9a47ca4.tar
# https://github.com/CardinalModules/rackwindows.git
Source129: rackwindows-60dfe5dff94b82fc42a43d971e41e64e296b0220.tar
# https://github.com/MarcBoule/ImpromptuModular.git
Source130: ImpromptuModular-eb514f1e867a5626918dd70b947908b3181f66b8.tar
# https://github.com/jhoar/AmalgamatedHarmonics.git
Source131: AmalgamatedHarmonics-97700c06af7df4d8fcf173ae3670b7907a682627.tar
# https://github.com/CardinalModules/cf.git
Source132: cf-b6c4a66ffc153d78c7efa00fa886657eb182b15d.tar
# https://github.com/MarcBoule/MindMeldModular.git
Source133: MindMeldModular-cd71f9a4c4a23bdec5666cc78c5bc8b3f936d175.tar
# https://github.com/ValleyAudio/ValleyRackFree.git
Source134: ValleyRackFree-4507aa7e1b0efc68e33e0ce1530ebd8ac7b7763c.tar
# https://github.com/SVModular/DrumKit.git
Source135: DrumKit-7681d30ac0b9246605d3d8d71dc7e25030748ec6.tar
# https://github.com/JerrySievert/SynthDevKit.git
Source136: SynthDevKit-0f322e58f00f1a04276ecc3eadb610b418f040d5.tar
# https://github.com/falkTX/Carla.git
Source137: Carla-f8d7d9afcea4c01aaf502b5af884dde31dfb28a7.tar
# https://github.com/falkTX/Carla-Plugins
Source138: Carla-Plugins-47380b7e7e4bd32685ecc0a36e719c330bc9c1b3.tar
# https://github.com/CardinalModules/mscHack.git
Source139: mscHack-80883512cc397c173e40e3bc014640b838ab343a.tar
# https://github.com/zezic/ZZC.git
Source140: ZZC-15364616da500d31f7545dcbfc01b4fda7f7c9d4.tar
# https://github.com/wiqid/repelzen.git
Source141: repelzen-428f76c3509e4d71489daf075c48ae4b995a0786.tar
# https://github.com/CardinalModules/AriaModules.git
Source142: AriaModules-269ab0f091b18f08ab253bd8af4866e78d770bc0.tar
# https://github.com/baconpaul/BaconPlugs.git
Source143: BaconPlugs-9d35b745af8569d6a9d6bc5c3f2c3e64c852d8e0.tar
# https://github.com/craigsapp/midifile.git
Source144: midifile-99e87b684f88ebff6417ef25f269f1a95b780ad2.tar
# https://github.com/RCameron93/FehlerFabrik.git
Source145: FehlerFabrik-9b5897828dc1b757f42cb707b5979488acb67401.tar
# https://gitlab.com/sonusdept/sonusmodular.git
Source146: sonusmodular-b63a685c6c68be188f5a3d5d9f6582eb94d62e53.tar
# https://github.com/JustMog/Mog-VCV.git
Source147: Mog-VCV-00a7e3b01f56da5cfc86720ae6951ecdf8953ee5.tar
# https://github.com/jatinchowdhury18/ChowDSP-VCV.git
Source148: ChowDSP-VCV-871f712f3eb95ada1c34bf3d8170690eb4aec8d0.tar
# https://github.com/Chowdhury-DSP/chowdsp_utils
Source149: chowdsp_utils-505052501fb64b38519101478628ec5ea32d6a43.tar
# https://github.com/gluethegiant/gtg-rack.git
Source150: gtg-rack-2c535bc38d61fd4d776aad7307c1dfbbed062b66.tar
# https://github.com/mhetrick/hetrickcv.git
Source151: hetrickcv-2fc83df75154c32b83addd3ed68b35eb6156ca0d.tar
# https://github.com/LancePutnam/Gamma.git
Source152: Gamma-70ba31c92db6afa160523940fd046a2bc249e8ad.tar
# https://github.com/VegaDeftwing/LyraeModules.git
Source153: LyraeModules-b21cbe8ee25ddf2a927e0b4ec9f2c97c115857af.tar
# https://github.com/mgunyho/Little-Utils.git
Source154: Little-Utils-b7ce2244835fa376201b21b2274937152dcd1121.tar
# https://github.com/SteveRussell33/Prism.git
Source155: Prism-4d95ace8b073e9e8e30b8671ecdb04101d943905.tar
# https://github.com/EaterOfSheep/Extratone.git
Source156: Extratone-9fb70500b17fe2495aba9f5f77ddf496d5c09f13.tar
# https://github.com/SteveRussell33/LifeFormModular.git
Source157: LifeFormModular-c7b8d096f618c421d7d45784b894c0ac2f3395b0.tar
# https://github.com/netboy3/21kHz-rack-plugins.git
Source158: 21kHz-rack-plugins-0bee82247151e2fe2885f1e15fbbd74ddb4f48d0.tar
# https://github.com/DISTRHO/PawPaw.git
Source159: PawPaw-ae5e26516596024a0268b5f8f1685050a248875a.tar
# https://github.com/LomasModules/LomasModules.git
Source160: LomasModules-b714cdb0c662503bc6cf60c06765b426a4caa17f.tar
# https://github.com/expertsleepersltd/vcvrack-encoders.git
Source161: vcvrack-encoders-95496e8a955407889bbab94cf404cf356802bb76.tar
# https://github.com/CardinalModules/ihtsyn.git
Source162: ihtsyn-1b77e3c3ba12734bbd29a4aa59dd408e679b5cf7.tar
# https://github.com/JerrySievert/QuickJS.git
Source163: QuickJS-f7bada076e2536fbc4ca46b81a34fa27990ffc30.tar
# https://github.com/NikolaiVChr/Autinn.git
Source164: Autinn-bc880d9d8fb59016de61e3253aff2b543d7bb665.tar
# https://github.com/MockbaTheBorg/MockbaModular.git
Source165: MockbaModular-479d2c8007b2087cdf557a491df25c5b85784a96.tar
# https://github.com/8Mode/8Mode-VCV_Modules.git
Source166: 8Mode-VCV_Modules-fe5a642ee0a455e882e105f422cf85f7e83fd31f.tar
# https://github.com/kauewerner/Axioma.git
Source167: Axioma-3e7e01e6a449dc1e6c523bd4487c0a3200b322cb.tar
# https://github.com/jensschulze/GoodSheperd.git
Source168: GoodSheperd-636351059f2eec629f3b8a537451dd3d0eb01c30.tar
# https://gitlab.com/hampton-harmonics/hampton-harmonics-modules.git
Source169: hampton-harmonics-modules-e5cf81f1c356fdc98fd08584146cda8af7e16b1f.tar
# https://github.com/martin-lueders/ML_modules.git
Source170: ML_modules-788ceb73cfabddaff7245b0df072b0e22a19b360.tar
# https://github.com/RareBreeds/Orbits.git
Source171: Orbits-ff0c007feb9ed1de57ea246f86e8b2b68572f5e6.tar
# https://github.com/aptrn/stocaudio-modules.git
Source172: stocaudio-modules-ed5c85b0d9391c37f4ec4d9de4ef8aa30d94bcd6.tar
# https://github.com/catronomix/catro-modulo.git
Source173: catro-modulo-bf6f969c5f7fff6a419a54197fb4318671281ad5.tar
# https://github.com/grough/lilac-loop-vcv.git
Source174: lilac-loop-vcv-cf9bb5cfa5fd41ecfc9976bb106c2f4a7667c9d7.tar
# https://github.com/janne808/kocmoc-rack-modules.git
Source175: kocmoc-rack-modules-f2a8c19f8aa81769e13d085d69a44de5afaacfaa.tar
# https://github.com/patheros/PathSetModules.git
Source176: PathSetModules-de53c78658c42638b7c356b78d1559634644f733.tar
# https://github.com/algoritmarte/AlgoritmarteVCVPlugin.git
Source177: AlgoritmarteVCVPlugin-9d41fe882ab5029100b55c98ba7f10172d452795.tar
# https://github.com/aaronstatic/AaronStatic_modules.git
Source178: AaronStatic_modules-4ace0a1789c577ee4eb12dc03da5271f80598d62.tar
# https://github.com/netboy3/MSM-vcvrack-plugin.git
Source179: MSM-vcvrack-plugin-abe3c24d40b11d31f9f38b2125eff9280c77ad1b.tar
# https://github.com/mhetrick/nonlinearcircuits.git
Source180: nonlinearcircuits-57eb090f233c21b2edee541ea17d800f22045d91.tar
# https://github.com/clone45/voxglitch.git
Source181: voxglitch-e856cfb4dbc255165d22294e80e13957241d2c80.tar
# https://github.com/CardinalModules/ArableInstruments.git
Source182: ArableInstruments-890448f087e3ab47eac391f9bcfe03f7bbd2123e.tar
# https://github.com/CardinalModules/eurorack.git
Source183: eurorack-87bf3b1da88147e3fcc8c57e3072eec67ccd380a.tar
# https://github.com/pichenettes/avril.git
Source184: avril-276b2887e4110ca913294fcbb313163dfb28a448.tar
# https://github.com/pichenettes/avrilx.git
Source185: avrilx-868d6e74eb8555f9575b5149202256156e5c03fa.tar
# https://github.com/pichenettes/stmlib.git
Source186: stmlib-8998429236d6edd4934b6c9ae8e0f167e3d30aa7.tar
# https://github.com/pichenettes/stm-audio-bootloader.git
Source187: stm-audio-bootloader-1ec7d6374e2d305cb710170eb80de9b66e795792.tar
# https://github.com/pichenettes/avr-audio-bootloader.git
Source188: avr-audio-bootloader-0de2be5928afdf7fb3e5ada60544ed6c15ab808f.tar
# https://github.com/pichenettes/avril.git
Source189: avril-36b988a851f8638adb9f53ff98939cb08ffce8cc.tar
# https://github.com/pichenettes/avrilx.git
Source190: avrilx-5c28367e91dfb036593e876c886241cf81f60a2d.tar
# https://github.com/pichenettes/stm-audio-bootloader.git
Source191: stm-audio-bootloader-6f20ead22a28967b0446546d2fcf0dfb9599ba93.tar
# https://github.com/pichenettes/avr-audio-bootloader.git
Source192: avr-audio-bootloader-52754f878b4883adf565bc3ddf691c5e1c4a9f6d.tar
# https://github.com/mqtthiqs/stmlib.git
Source193: stmlib-8ab2aaee77cbacb47b646d46d22ee5d358effe2d.tar
# https://github.com/CardinalModules/Fundamental.git
Source194: Fundamental-9ac0cdb93938c3f01aba58ec01fdd01257abf353.tar
# https://gitlab.com/unlessgames/unless_modules.git
Source195: unless_modules-3f895c7663e3e54c4e30c406c56d420ea407133e.tar
# https://github.com/VegaDeftwing/PinkTromboneVCV.git
Source196: PinkTromboneVCV-87ecd0ff5212a65b064444362e76c9bf94c01826.tar
# https://github.com/knchaffin/Meander.git
Source197: Meander-c095824708947630d9db6a6b7afcd51bdaa0a009.tar
# https://github.com/korfuri/WhatTheRack.git
Source198: WhatTheRack-e373378491d2cf3b8257137d154aef1d389c5204.tar
# https://github.com/AScustomWorks/AS.git
Source199: AS-2284e4a3befb097b42ae30032147fd61226f64ff.tar
# https://github.com/gosub/forsitan-modulare.git
Source200: forsitan-modulare-056cc2ec9186a4175d9214eee91e4ff5cc2e5fb1.tar
# https://github.com/Ahineya/vcv-myth-plugin.git
Source201: vcv-myth-plugin-e511dd95eca830ee74fef23bddc195696603125f.tar
# }}}

Patch1:   Cardinal-22.07-alt-lv2-in-lib64.patch

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

Requires: %name-common

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
Requires: %name-common

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
tar -xf %SOURCE113 -C 'include/sse2neon' --strip-components 1
tar -xf %SOURCE114 -C 'plugins/Befaco' --strip-components 1
tar -xf %SOURCE115 -C 'plugins/AudibleInstruments' --strip-components 1
tar -xf %SOURCE116 -C 'plugins/AudibleInstruments/eurorack' --strip-components 1
tar -xf %SOURCE117 -C 'plugins/AudibleInstruments/eurorack/avrlib' --strip-components 1
tar -xf %SOURCE118 -C 'plugins/AudibleInstruments/eurorack/avrlibx' --strip-components 1
tar -xf %SOURCE119 -C 'plugins/AudibleInstruments/eurorack/stmlib' --strip-components 1
tar -xf %SOURCE120 -C 'plugins/AudibleInstruments/eurorack/stm_audio_bootloader' --strip-components 1
tar -xf %SOURCE121 -C 'plugins/AudibleInstruments/eurorack/avr_audio_bootloader' --strip-components 1
tar -xf %SOURCE122 -C 'plugins/AnimatedCircuits' --strip-components 1
tar -xf %SOURCE123 -C 'plugins/ZetaCarinaeModules' --strip-components 1
tar -xf %SOURCE124 -C 'plugins/GrandeModular' --strip-components 1
tar -xf %SOURCE125 -C 'plugins/BogaudioModules' --strip-components 1
tar -xf %SOURCE126 -C 'plugins/Bidoo' --strip-components 1
tar -xf %SOURCE127 -C 'plugins/ESeries' --strip-components 1
tar -xf %SOURCE128 -C 'plugins/JW-Modules' --strip-components 1
tar -xf %SOURCE129 -C 'plugins/rackwindows' --strip-components 1
tar -xf %SOURCE130 -C 'plugins/ImpromptuModular' --strip-components 1
tar -xf %SOURCE131 -C 'plugins/AmalgamatedHarmonics' --strip-components 1
tar -xf %SOURCE132 -C 'plugins/cf' --strip-components 1
tar -xf %SOURCE133 -C 'plugins/MindMeldModular' --strip-components 1
tar -xf %SOURCE134 -C 'plugins/ValleyAudio' --strip-components 1
tar -xf %SOURCE135 -C 'plugins/DrumKit' --strip-components 1
tar -xf %SOURCE136 -C 'plugins/DrumKit/deps/SynthDevKit' --strip-components 1
tar -xf %SOURCE137 -C 'carla' --strip-components 1
tar -xf %SOURCE138 -C 'carla/source/native-plugins/external' --strip-components 1
tar -xf %SOURCE139 -C 'plugins/mscHack' --strip-components 1
tar -xf %SOURCE140 -C 'plugins/ZZC' --strip-components 1
tar -xf %SOURCE141 -C 'plugins/repelzen' --strip-components 1
tar -xf %SOURCE142 -C 'plugins/AriaModules' --strip-components 1
tar -xf %SOURCE143 -C 'plugins/BaconPlugs' --strip-components 1
tar -xf %SOURCE144 -C 'plugins/BaconPlugs/libs/midifile' --strip-components 1
tar -xf %SOURCE145 -C 'plugins/FehlerFabrik' --strip-components 1
tar -xf %SOURCE146 -C 'plugins/sonusmodular' --strip-components 1
tar -xf %SOURCE147 -C 'plugins/Mog' --strip-components 1
tar -xf %SOURCE148 -C 'plugins/ChowDSP' --strip-components 1
tar -xf %SOURCE149 -C 'plugins/ChowDSP/lib/chowdsp_utils' --strip-components 1
tar -xf %SOURCE150 -C 'plugins/GlueTheGiant' --strip-components 1
tar -xf %SOURCE151 -C 'plugins/HetrickCV' --strip-components 1
tar -xf %SOURCE152 -C 'plugins/HetrickCV/Gamma' --strip-components 1
tar -xf %SOURCE153 -C 'plugins/LyraeModules' --strip-components 1
tar -xf %SOURCE154 -C 'plugins/LittleUtils' --strip-components 1
tar -xf %SOURCE155 -C 'plugins/Prism' --strip-components 1
tar -xf %SOURCE156 -C 'plugins/Extratone' --strip-components 1
tar -xf %SOURCE157 -C 'plugins/LifeFormModular' --strip-components 1
tar -xf %SOURCE158 -C 'plugins/21kHz' --strip-components 1
tar -xf %SOURCE159 -C 'deps/PawPaw' --strip-components 1
tar -xf %SOURCE160 -C 'plugins/LomasModules' --strip-components 1
tar -xf %SOURCE161 -C 'plugins/ExpertSleepers-Encoders' --strip-components 1
tar -xf %SOURCE162 -C 'plugins/ihtsyn' --strip-components 1
tar -xf %SOURCE163 -C 'deps/QuickJS' --strip-components 1
tar -xf %SOURCE164 -C 'plugins/Autinn' --strip-components 1
tar -xf %SOURCE165 -C 'plugins/MockbaModular' --strip-components 1
tar -xf %SOURCE166 -C 'plugins/8Mode' --strip-components 1
tar -xf %SOURCE167 -C 'plugins/Axioma' --strip-components 1
tar -xf %SOURCE168 -C 'plugins/GoodSheperd' --strip-components 1
tar -xf %SOURCE169 -C 'plugins/HamptonHarmonics' --strip-components 1
tar -xf %SOURCE170 -C 'plugins/ML_modules' --strip-components 1
tar -xf %SOURCE171 -C 'plugins/Orbits' --strip-components 1
tar -xf %SOURCE172 -C 'plugins/stocaudio' --strip-components 1
tar -xf %SOURCE173 -C 'plugins/CatroModulo' --strip-components 1
tar -xf %SOURCE174 -C 'plugins/LilacLoop' --strip-components 1
tar -xf %SOURCE175 -C 'plugins/kocmoc' --strip-components 1
tar -xf %SOURCE176 -C 'plugins/PathSet' --strip-components 1
tar -xf %SOURCE177 -C 'plugins/Algoritmarte' --strip-components 1
tar -xf %SOURCE178 -C 'plugins/AaronStatic' --strip-components 1
tar -xf %SOURCE179 -C 'plugins/MSM' --strip-components 1
tar -xf %SOURCE180 -C 'plugins/nonlinearcircuits' --strip-components 1
tar -xf %SOURCE181 -C 'plugins/voxglitch' --strip-components 1
tar -xf %SOURCE182 -C 'plugins/ArableInstruments' --strip-components 1
tar -xf %SOURCE183 -C 'plugins/ArableInstruments/eurorack' --strip-components 1
tar -xf %SOURCE184 -C 'plugins/ArableInstruments/eurorack/avrlib' --strip-components 1
tar -xf %SOURCE185 -C 'plugins/ArableInstruments/eurorack/avrlibx' --strip-components 1
tar -xf %SOURCE186 -C 'plugins/ArableInstruments/eurorack/stmlib' --strip-components 1
tar -xf %SOURCE187 -C 'plugins/ArableInstruments/eurorack/stm_audio_bootloader' --strip-components 1
tar -xf %SOURCE188 -C 'plugins/ArableInstruments/eurorack/avr_audio_bootloader' --strip-components 1
tar -xf %SOURCE189 -C 'plugins/ArableInstruments/parasites/avrlib' --strip-components 1
tar -xf %SOURCE190 -C 'plugins/ArableInstruments/parasites/avrlibx' --strip-components 1
tar -xf %SOURCE191 -C 'plugins/ArableInstruments/parasites/stm_audio_bootloader' --strip-components 1
tar -xf %SOURCE192 -C 'plugins/ArableInstruments/parasites/avr_audio_bootloader' --strip-components 1
tar -xf %SOURCE193 -C 'plugins/ArableInstruments/parasites/stmlib' --strip-components 1
tar -xf %SOURCE194 -C 'plugins/Fundamental' --strip-components 1
tar -xf %SOURCE195 -C 'plugins/unless_modules' --strip-components 1
tar -xf %SOURCE196 -C 'plugins/PinkTrombone' --strip-components 1
tar -xf %SOURCE197 -C 'plugins/Meander' --strip-components 1
tar -xf %SOURCE198 -C 'plugins/WhatTheRack' --strip-components 1
tar -xf %SOURCE199 -C 'plugins/AS' --strip-components 1
tar -xf %SOURCE200 -C 'plugins/forsitan-modulare' --strip-components 1
tar -xf %SOURCE201 -C 'plugins/myth-modules' --strip-components 1
# }}}

# don't build VST plugin variants
sed -i '/^all:/ s/vst[23]//g' src/Makefile.cardinal.mk

%patch1 -p0

%build
%make_build \
    NOOPT=true \
    SKIP_STRIPPING=true \
    PREFIX=/usr \
    SYSDEPS=true \
    WITH_LTO=true \
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
* Mon Aug 08 2022 Ivan A. Melnikov <iv@altlinux.org> 22.07-alt1
- Initial build for Sisyphus
