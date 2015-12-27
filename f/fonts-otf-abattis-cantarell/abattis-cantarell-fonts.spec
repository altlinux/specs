%define oldname abattis-cantarell-fonts
%global actualname cantarell

%global fontname abattis-%{actualname}
%global fontconf 31-cantarell.conf

%global archivename1 Cantarell-Bold
%global archivename2 Cantarell-Regular

Name: fonts-otf-abattis-cantarell
Version: 0.0.18
Release: alt1_1
Summary: Cantarell, a Humanist sans-serif font family

Group: System/Fonts/True type
License: OFL
URL: https://git.gnome.org/browse/cantarell-fonts/
Source0: http://download.gnome.org/sources/%{actualname}-fonts/0.0/%{actualname}-fonts-%{version}.tar.xz
Source1: %{fontname}.metainfo.xml

BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Source44: import.info

%description
Cantarell is a set of fonts designed by Dave Crossland.
It is a sans-serif humanist typeface family.

%prep
%setup -q -n %{actualname}-fonts-%{version}

# Force regeneration
rm otf/*.otf

%build
%configure --enable-source-rebuild
make %{?_smp_mflags}

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/*.otf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p fontconfig/%{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
       %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf
%doc COPYING
%doc NEWS README
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.18-alt1_1
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.17.2-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.16-alt1_2
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.16-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1_2
- update to new release by fcimport

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.15-alt1_0
- new version

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.14-alt1_1
- fc import

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1_2
- update to new release by fcimport

* Mon Jun 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.13-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1_2
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1_1
- update to new release by fcimport

* Sat Nov 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.11-alt1_1
- update to new release by fcimport

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.10.1-alt1_1
- update to new release by fcimport

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.9-alt1_2
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.9-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1_1
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_2
- update to new release by fcimport

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.7-alt1_1
- update to new release by fcimport

* Tue Oct 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt2_2
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt2_1
- rebuild with new rpm-build-fonts

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1_1
- initial release by fcimport

