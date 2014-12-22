# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname sil-padauk-fonts
%global fontname sil-padauk
%global fontconf 65-%{fontname}
%global archivename padauk-2.8

%global common_desc \
Padauk is a Myanmar font covering all currently used characters \
in the Myanmar block. The font aims to cover all minority language needs. \
At the moment, these do not extend to stylistic variation needs. \
The font is a smart font using a Graphite description.

Name:    fonts-ttf-sil-padauk
Version: 2.8
Release: alt2_7
Summary: A font for Burmese and the Myanmar script

Group:   System/Fonts/True type
License: OFL
URL:     http://scripts.sil.org/Padauk
# The source link is a redirect and is not directly accessible
Source0: %{archivename}.zip
Source1: %{oldname}-fontconfig.conf
Source2: %{oldname}-book-fontconfig.conf
Source3: %{fontname}.metainfo.xml
Source4: %{fontname}-book.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: python-module-fonttools
Source44: import.info

%description
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/Padauk.ttf
%{_fontbasedir}/*/%{_fontstem}/Padauk-bold.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%package -n fonts-ttf-sil-padauk-book
Group: System/Fonts/True type
Summary:  A font for Burmese and the Myanmar script

%description -n fonts-ttf-sil-padauk-book
Padauk Book family font.

%common_desc

%files -n fonts-ttf-sil-padauk-book
%{_fontconfig_templatedir}/%{fontconf}-book.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-book.conf
%{_fontbasedir}/*/%{_fontstem}/Padauk-book*.ttf
%{_datadir}/appdata/%{fontname}-book.metainfo.xml
%doc *.txt

%prep
%setup -q -n padauk-2.80
sed -i 's/\r//' OFL.txt

%build
# Following is needed to fix the postscript font name
ttx *.ttf
sed -i 's|&#225;&#128;&#149;&#225;&#128;&#173;&#225;&#128;&#144;&#225;&#128;&#177;&#225;&#128;&#172;&#225;&#128;&#128;&#225;&#128;&#186;|Padauk|g' Padauk*.ttx

sed -i 's|&#225;&#128;&#133;&#225;&#128;&#172;&#225;&#128;&#156;&#225;&#128;&#175;&#225;&#128;&#182;&#225;&#128;&#184;&#225;&#128;&#153;&#225;&#128;&#178;|Bold|g' Padauk*.ttx

sed -i 's|&#225;&#128;&#133;&#225;&#128;&#172;&#225;&#128;&#161;&#225;&#128;&#175;&#225;&#128;&#149;&#225;&#128;&#186;|Book|g' Padauk-book*.ttx
rm *.ttf
ttx Padauk*.ttx

rm *.ttx


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-book.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-book.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}-book.conf

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-book.metainfo.xml
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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

%changelog
* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.8-alt2_7
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.8-alt2_6
- bugfix: fixed subpackage name

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_6
- update to new release by fcimport

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_3
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.8-alt1_2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt3_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt3_8
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_8
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt2_7
- rebuild with new rpm-build-fonts

* Thu Aug 04 2011 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_7
- initial release by fcimport

