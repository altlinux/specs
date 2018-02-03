Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gdouros-aegean-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname gdouros-aegean
%global fontconf 65-%{fontname}.conf

Name:           fonts-otf-gdouros-aegean
Version:        9.81
Release:        alt1_1
Summary:        A font for ancient scripts in the greater Aegean vicinity
License:        Public Domain
URL:            http://users.teilar.gr/~g1951d/
Source0:        http://users.teilar.gr/~g1951d/Aegean.zip
Source1:        %{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Source44: import.info

%description
Aegean covers the following scripts and symbols: Basic Latin, Greek and Coptic,
Greek Extended, some Punctuation and other Symbols, Linear B Syllabary, Linear
B Ideograms, Aegean Numbers, Ancient Greek Numbers, Ancient Symbols, Phaistos
Disc, Lycian, Carian, Old Italic, Ugaritic, Old Persian, Cypriot Syllabary,
Phoenician, Lydian, Archaic Greek Musical Notation, Cretan Hieroglyphs,
Cypro-Minoan, Linear A, the Arkalochori Axe, Ancient Greek and Old Italic
variant alphabets. Those of the above that are not supported by the Unicode
Standard 8.0, they are allocated in the Supplementary Private Use Plane 15.

It was created by George Douros.

%prep
%setup -n %{oldname}-%{version} -q -c

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Aegean.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml
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

%check
appstream-util validate-relax --nonet \
      %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml


%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/Aegean.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml
%doc Aegean.pdf Aegean.odt

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 9.81-alt1_1
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 9.17-alt1_3
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 8.91-alt1_1
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 8.01-alt1_1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 8.00-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 8.00-alt1_2
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 3.02-alt3_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.02-alt3_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.02-alt3_5
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.02-alt3_4
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.02-alt3_3
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.02-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 3.02-alt2_2
- rebuild with new rpm-build-fonts

* Tue Aug 02 2011 Igor Vlasenko <viy@altlinux.ru> 3.02-alt1_2
- initial release by fcimport

