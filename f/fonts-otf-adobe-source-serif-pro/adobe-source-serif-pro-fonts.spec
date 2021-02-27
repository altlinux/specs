Group: System/Fonts/True type
%define oldname adobe-source-serif-pro-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname source-serif
%global fontconf 63-%{fontname}.conf

Name:           fonts-otf-adobe-source-serif-pro
Version:        4.004
Release:        alt1_1
Summary:        Typeface for setting text in many sizes, weights, and languages

License:        OFL
URL:            https://github.com/adobe-fonts/source-serif
Source0:        https://github.com/adobe-fonts/source-serif/archive/%{version}R.tar.gz#/%{oldname}-%{version}.tar.gz
Source1:        %{fontname}.fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Source44: import.info

%description
Source Serif is an open-source typeface to complement the Source Sans family.

%prep
%setup -q -n source-serif-%{version}R
sed -i 's/\r//' LICENSE.md

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
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

%check
appstream-util --nonet validate-relax \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/*.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc README.md
%doc --no-dereference LICENSE.md

%changelog
* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 4.004-alt1_1
- update to new release by fcimport

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 3.001-alt1_1
- update to new release by fcimport

* Wed Aug 07 2019 Igor Vlasenko <viy@altlinux.ru> 3.000-alt1_1
- update to new release by fcimport

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 2.010.1.010-alt1_1
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.007.1.007-alt1_1
- update to new release by fcimport

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_3
- new version

