# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname oflb-riordonfancy-fonts
%define fontname        riordonfancy
%define fontconf        69-%{fontname}.conf

Name:           fonts-ttf-oflb-riordonfancy
Version:        4
Release:        alt3_5
Summary:        A stylized font

Group:          System/Fonts/True type
License:        OFL
URL:            http://openfontlibrary.org/media/files/tthurman/354
Source0:        http://openfontlibrary.org/people/tthurman/tthurman_-_Riordon_Fancy.zip
Source1:        %{fontname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel fontforge
Source44: import.info

%description
RiordonFancy is a highly-stylized font designed by ten-year-old Riordon
Thurman. It includes all ASCII glyphs, most Latin-1 glyphs, a number of Latin
Extended glyphs, the interrobang (a..), and the snowman (a'.).

%prep
%setup -qc

%build
rm RiordonFancy.ttf
FONTFORGE_LANGUAGE=ff fontforge -script "-" *.sfd <<EOF
i = 1
while (i < \$argc)
  Open(\$argv[i], 1)
  fontname = StrJoin(StrSplit(\$fontname, "O"), "")
  familyname = StrJoin(StrSplit(\$familyname, " O"), "")
  fullname = StrJoin(StrSplit(\$fullname, " O"), "")
  SetFontNames(fontname, familyname, fullname)
  ScaleToEm(2048)
  RoundToInt()
  SetFontOrder(2)
  SelectAll()
  AutoInstr()
  Generate(\$fontname + ".ttf")
  Close()
  i++
endloop
EOF

%install

install -dm 755 $RPM_BUILD_ROOT%{_fontdir}
install -pm 644 RiordonFancy.ttf $RPM_BUILD_ROOT%{_fontdir}/

install -dm 755 $RPM_BUILD_ROOT%{_fontconfig_templatedir}
install -dm 755 $RPM_BUILD_ROOT%{_fontconfig_confdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
  $RPM_BUILD_ROOT%{_fontconfig_confdir}/%{fontconf}
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
%doc readme.txt fontlog.txt
%dir %{_fontbasedir}/*/%{_fontstem}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt3_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4-alt2_5
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4-alt2_4
- initial release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 4-alt1_4
- rebuild with new rpm-build-fonts

