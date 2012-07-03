Name: pbx-music-signate
Summary: Free classical music
Version: 0.1
Release: alt1
License: Public Domain
Group: System/Servers
BuildArch: noarch
Provides: pbx-music
Requires(post): pbx-music-base
Obsoletes: freemusic-signate
Obsoletes: asterisk-freemusic
Url: http://www.signate.com/products/?page=moh
Source: %name-%version.tar

%package mozart-mp3
Summary: Free classical music
Group: System/Servers
BuildArch: noarch

%description mozart-mp3
Elena Kuschnerova, pianist, and Lev Guelbard, violinist, playing public domain
classical music on hold with your PBX such as Asterisk/CallWeaver.


%package mozart
Summary: Free classical music
Group: System/Servers
Obsoletes: freemusic-signate
Requires(post): pbx-music-base
Provides: pbx-music
Obsoletes: asterisk-freemusic-mozart

%description mozart
Elena Kuschnerova, pianist, and Lev Guelbard, violinist, playing public domain
classical music on hold with your PBX such as Asterisk/CallWeaver.


%package mp3
Summary: Free classical music
Group: System/Servers

%description mp3
Elena Kuschnerova, pianist, and Lev Guelbard, violinist, playing public domain
classical music on hold with your PBX such as Asterisk/CallWeaver.


%description
Elena Kuschnerova, pianist, and Lev Guelbard, violinist, playing public domain
classical music on hold with your PBX such as Asterisk/CallWeaver.


%prep
%setup

%build
%make_build

%install
mkdir -p  %buildroot/%_datadir/sounds/signate
cp -a *.wav %buildroot/%_datadir/sounds/signate/
cp -a *.mp3 %buildroot/%_datadir/sounds/signate/

%post
for s in %_datadir/sounds/signate/*.wav; do
	ln -sf "$s" /var/lib/pbx/music/
done

%post mozart
for s in %_datadir/sounds/signate/*.wav; do
    ln -sf "$s" /var/lib/pbx/music/
done

%files
%_datadir/sounds/signate/beethoven_violin_sonata_n7.wav
%_datadir/sounds/signate/beethoven__violin_sonata_n.wav
%_datadir/sounds/signate/brahms_piano_quartet_n3_24.wav
%_datadir/sounds/signate/brahms_piano_quartet_n3_34.wav
%_datadir/sounds/signate/brahms_piano_quartet_n3_44.wav
%_datadir/sounds/signate/brahms_scherzo.wav
%_datadir/sounds/signate/brahms__violin_sonata__2_1.wav
%_datadir/sounds/signate/brahms__violin_sonata__2_2.wav
%_datadir/sounds/signate/brahms__violin_sonata__2__.wav
%_datadir/sounds/signate/brahms_violin_sonata_n3_14.wav
%_datadir/sounds/signate/brahms_violin_sonata_n3_24.wav
%_datadir/sounds/signate/brahms_violin_sonata_n3_44.wav
%_datadir/sounds/signate/mahler__piano_quartet.wav
%_datadir/sounds/signate/mendelssohn__piano_trio_i1.wav
%_datadir/sounds/signate/mendelssohn__piano_trio_i2.wav
%_datadir/sounds/signate/mendelssohn__piano_trio_i3.wav
%_datadir/sounds/signate/mendelssohn__piano_trio_in.wav
%_datadir/sounds/signate/mendelssohn_violinpiano_1.wav
%_datadir/sounds/signate/mendelssohn_violinpiano_2.wav
%_datadir/sounds/signate/mendelssohn_violinpiano_c.wav
%_datadir/sounds/signate/piazzolla__verano_porteno.wav
%_datadir/sounds/signate/schubert_violin_sonatina_3.wav
%_datadir/sounds/signate/schubert_violin_sonatina_4.wav
%_datadir/sounds/signate/schubert_violin_sonatina_o.wav

%files mozart-mp3
%_datadir/sounds/signate/mozart__violin_sonata_e_m1.mp3
%_datadir/sounds/signate/mozart__violin_sonata_e_mi.mp3
%_datadir/sounds/signate/mozart__violin_sonata_g_m1.mp3
%_datadir/sounds/signate/mozart__violin_sonata_g_ma.mp3

%files mozart
%_datadir/sounds/signate/mozart__violin_sonata_e_m1.wav
%_datadir/sounds/signate/mozart__violin_sonata_e_mi.wav
%_datadir/sounds/signate/mozart__violin_sonata_g_m1.wav
%_datadir/sounds/signate/mozart__violin_sonata_g_ma.wav

%files mp3
%_datadir/sounds/signate/beethoven_violin_sonata_n7.mp3
%_datadir/sounds/signate/beethoven__violin_sonata_n.mp3
%_datadir/sounds/signate/brahms_piano_quartet_n3_24.mp3
%_datadir/sounds/signate/brahms_piano_quartet_n3_34.mp3
%_datadir/sounds/signate/brahms_piano_quartet_n3_44.mp3
%_datadir/sounds/signate/brahms_scherzo.mp3
%_datadir/sounds/signate/brahms__violin_sonata__2_1.mp3
%_datadir/sounds/signate/brahms__violin_sonata__2_2.mp3
%_datadir/sounds/signate/brahms__violin_sonata__2__.mp3
%_datadir/sounds/signate/brahms_violin_sonata_n3_14.mp3
%_datadir/sounds/signate/brahms_violin_sonata_n3_24.mp3
%_datadir/sounds/signate/brahms_violin_sonata_n3_44.mp3
%_datadir/sounds/signate/mahler__piano_quartet.mp3
%_datadir/sounds/signate/mendelssohn__piano_trio_i1.mp3
%_datadir/sounds/signate/mendelssohn__piano_trio_i2.mp3
%_datadir/sounds/signate/mendelssohn__piano_trio_i3.mp3
%_datadir/sounds/signate/mendelssohn__piano_trio_in.mp3
%_datadir/sounds/signate/mendelssohn_violinpiano_1.mp3
%_datadir/sounds/signate/mendelssohn_violinpiano_2.mp3
%_datadir/sounds/signate/mendelssohn_violinpiano_c.mp3
%_datadir/sounds/signate/piazzolla__verano_porteno.mp3
%_datadir/sounds/signate/schubert_violin_sonatina_3.mp3
%_datadir/sounds/signate/schubert_violin_sonatina_4.mp3
%_datadir/sounds/signate/schubert_violin_sonatina_o.mp3

%changelog
* Sat Sep 19 2009 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

