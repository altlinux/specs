Group: System/Fonts/True type
%define oldname levien-inconsolata-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname levien-inconsolata
%global fontconf 75-%{fontname}.conf

Name:           fonts-ttf-levien-inconsolata
Version:        3.000
Release:        alt1_1
Summary:        Inconsolata fonts

License:        OFL
URL:            http://www.levien.com/type/myfonts/inconsolata.html
Source0:        https://github.com/googlefonts/Inconsolata/archive/v%{version}/%{oldname}-%{version}.tar.gz
Source1:        %{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge libfontforge
BuildRequires:  git-core
Source44: import.info

%description
A monospace font, designed for code listings and the like, in print.


%prep
%setup -q -n Inconsolata-%{version}



%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
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

        
%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc documentation/*.pdf
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%changelog
* Fri Dec 27 2019 Igor Vlasenko <viy@altlinux.ru> 3.000-alt1_1
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.012-alt1_3
- new version

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_15
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_11
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_6
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_5
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_5
- initial release by fcimport

