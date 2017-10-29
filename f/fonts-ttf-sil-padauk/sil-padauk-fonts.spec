Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname sil-padauk-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname sil-padauk
%global fontconf 65-%{fontname}
%global archivename padauk-3.002

%global common_desc \
Padauk is a pan Burma font designed to support all Myanmar script based \
languages. It covers all of the Unicode Myanmar script blocks and works \
on all OpenType and Graphite based systems.

Name:    fonts-ttf-sil-padauk
Version: 3.002
Release: alt1_2
Summary: A font for Burmese and the Myanmar script

License: OFL
URL:     http://scripts.sil.org/Padauk
Source0: http://software.sil.org/downloads/d/padauk/%{archivename}.zip
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
%{_fontbasedir}/*/%{_fontstem}/Padauk-Regular.ttf
%{_fontbasedir}/*/%{_fontstem}/Padauk-Bold.ttf
%doc *.txt documentation
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
%{_fontbasedir}/*/%{_fontstem}/PadaukBook*.ttf
%{_datadir}/appdata/%{fontname}-book.metainfo.xml
%doc *.txt documentation

%prep
%setup -q -n %{archivename}

sed -i 's/\r//' *.txt documentation/DOCUMENTATION.txt

%build
# nothing to do here

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
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.002-alt1_2
- update to new release by fcimport

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

