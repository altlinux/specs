Group: System/Fonts/True type
%define oldname overpass-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname overpass
%global fontconf 60-%{fontname}.conf
%global monofontconf 60-%{fontname}-mono.conf

Name:		fonts-ttf-overpass
Version:	3.0.4
Release:	alt1_1
Summary:	Typeface based on the U.S. interstate highway road signage type system
License:	OFL or LGPLv2+
URL:		https://github.com/RedHatBrand/overpass/
Source0:	https://github.com/RedHatBrand/Overpass/archive/%{version}.tar.gz
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
Source3:	%{fontname}-mono-fonts-fontconfig.conf
Source4:	%{fontname}-mono.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info
# rename
Conflicts: fonts-ttf-overpass-fonts <= 1.01-alt1_7
Obsoletes: fonts-ttf-overpass-fonts <= 1.01-alt1_7

%description
Free and open source typeface based on the U.S. interstate highway road signage
type system; it is sans-serif and suitable for both body and titling text.

%package -n fonts-ttf-overpass-mono
Group: System/Fonts/True type
Summary:	Monospace version of overpass fonts

%description -n fonts-ttf-overpass-mono
Free and open source typeface based on the U.S. interstate highway road signage
type system. This is the monospace family variant.

%prep
%setup -q -n Overpass-%{version}

%build
# Nothing to do here.

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p desktop-fonts/overpass*/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -m 0644 -p %{SOURCE3} \
		%{buildroot}%{_fontconfig_templatedir}/%{monofontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{monofontconf} \
                %{buildroot}%{_fontconfig_confdir}/%{monofontconf}

# I do not think this is useful to package, but if it is...
%if 0
mkdir -p %{buildroot}/usr/lib/node_modules/overpass/
cp -a bower.json package.json %{buildroot}/usr/lib/node_modules/overpass/
%endif

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

install -Dm 0644 -p %{SOURCE4} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
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
%{_fontbasedir}/*/%{_fontstem}/overpass-bold*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-extra*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-heavy*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-italic*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-light*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-regular*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-semibold*.otf
%{_fontbasedir}/*/%{_fontstem}/overpass-thin*.otf
%doc README.md overpass-specimen.pdf
%doc --no-dereference LICENSE.md
%{_datadir}/appdata/%{fontname}.metainfo.xml
%if 0
/usr/lib/node_modules/overpass/
%endif

%files -n fonts-ttf-overpass-mono
%{_fontconfig_templatedir}/%{monofontconf}
%config(noreplace) %{_fontconfig_confdir}/%{monofontconf}
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/overpass-mono-*.otf
%doc README.md overpass-mono-specimen.pdf
%doc --no-dereference LICENSE.md
%{_datadir}/appdata/%{fontname}-mono.metainfo.xml

%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 3.0.4-alt1_1
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.3-alt1_1
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.2-alt1_2
- update to new release by fcimport

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_9
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_7
- bugfix: fixed subpackage name

