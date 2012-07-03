# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname nafees-nastaleeq-fonts
%global fontname        nafees-nastaleeq
%global fontconf        67-%{fontname}.conf
%global archivename     Nafees_Nastaleeq_v1.02

Name:           fonts-ttf-nafees-nastaleeq
Version:        1.02
Release:        alt2_3
Summary:        Nafees nastaleeq font for writing Urdu in the Nastaleeq script

Group:          System/Fonts/True type
License:        Bitstream Vera
URL:            http://www.crulp.org/index.htm

Source0:        http://www.crulp.org/Downloads/localization/fonts/NafeesNastaleeq/%{archivename}.zip

Source1:        %{fontname}-update-preferred-family.pe
Source2:        %{fontconf}

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Source44: import.info

%description

Nafees Nastaleeq is developed according to calligraphic rules,\ 
following the style of Syed Nafees Al-Hussaini (Nafees Raqam)\
one of the finest calligraphers of Pakistan. Nafees Nastaa.'leeq\
OTF contains approximately 1,000 glyphs, including about 26 ligatures. 

%prep
%setup -q -c

%build
#Fix RHBZ#490830 while not fixed upstream
%{_bindir}/fontforge %{SOURCE1} Nafees\ Nastaleeq\ v1.02.ttf
rm  Nafees\ Nastaleeq\ v1.02.ttf

%install

#fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE2} \
                %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}
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
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf

%doc  Nafees_Nastaleeq_v1.02.pdf


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_3
- update to new release by fcimport

* Mon Oct 31 2011 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_2
- initial fedora import

