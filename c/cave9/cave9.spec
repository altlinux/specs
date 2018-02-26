%define version 0.4
%define name cave9
%global fontconf 64-%{name}-mutante.conf

Name:           cave9
Version:        0.4
Release:        alt2_3
Summary:        3d game of cave exploration

Group:          Games/Other
License:        LGPLv3 and CC-BY-SA and Public Domain
URL:            http://code.google.com/p/cave9
Source0:        http://cave9.googlecode.com/files/cave9_src-%{version}.tgz
Source1:        http://cave9.googlecode.com/files/cave9_data-4.tgz
Source2:        cave9.desktop

BuildRequires:  libSDL_image-devel libSDL_net-devel libSDL_ttf-devel libGL-devel desktop-file-utils fontpackages-devel
Requires:       fonts-ttf-cave9-mutante
Source44: import.info
Patch33: cave9-0.4-alt-as-needed.patch


%description
Cave9 is a gravity cave-exploration game.

%package        -n fonts-ttf-cave9-mutante

Summary:        Mutante font used by the HUD in cave9 game
BuildArch:      noarch
Group:          System/Fonts/True type
License:        CC-BY
Source3:        %{name}-mutante-fontconfig.conf

%description -n fonts-ttf-cave9-mutante
Fantasy/display font used by the cave9 game, this font has only the basic
characters used in the Portuguese language was made as an experiment by the
designer Jonas KA.hner (http://www.criatipos.com/) the font was altered by
the game developer to also include numbers.

%files -n fonts-ttf-cave9-mutante
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/mutante.ttf
%doc data_README.txt

%prep
%setup -q -a1
sed -i src/GNUmakefile -e "s/-Wall -Werror -ggdb//"
%patch33 -p1

%build
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin %{buildroot}/usr/share/cave9
install -m 755 -p cave9 $RPM_BUILD_ROOT/usr/bin 
cp -p data/wall.jpg data/icon.png data/thrust.wav data/crash.wav data/hit.wav $RPM_BUILD_ROOT/usr/share/cave9

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p data/*.ttf %{buildroot}%{_fontdir}/mutante.ttf

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s ../fonts/ttf/cave9/mutante.ttf $RPM_BUILD_ROOT/usr/share/cave9/hud.ttf

mv data/README.txt data_README.txt
desktop-file-install                     \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  %{SOURCE2}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi

%files
%doc AUTHORS.txt README.txt COPYING.txt data_README.txt
%{_bindir}/cave9
%{_datadir}/cave9
%{_datadir}/applications/cave9.desktop

%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_3
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_3
- update to new release by fcimport

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2
- initial release by fcimport

