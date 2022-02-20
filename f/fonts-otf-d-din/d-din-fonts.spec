Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname d-din-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname d-din
%global fontconf 64-%{fontname}
%global asfontname com.datto.%{fontname}

%global desc \
D-DIN is a sans-serif typeface family derived from German DIN \
(Deutsches Institut fuer Normung / German Institute for Standardization) \
font style. \
 \
This font was commissioned by Datto, Inc. from Monotype and is used for \
the company's primary corporate typography.

Name:           fonts-otf-d-din
Version:        1.0
Release:        alt1_10
Summary:        Datto D-DIN fonts
# Only the metainfo files are CC-BY-SA
License:        OFL and CC-BY-SA
URL:            https://www.datto.com/fonts/d-din

Source0:        https://www.datto.com/fonts/d-din}/D-DIN_complete-v%{version}.zip
Source1:        %{fontconf}-fontconfig.conf
Source2:        %{fontconf}-condensed-fontconfig.conf
Source3:        %{fontconf}-exp-fontconfig.conf

BuildArch:      noarch
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  fontpackages-devel

# Eliminate nonsense Provides from fc-query (rhbz#1509790)

Source44: import.info
%filter_from_provides /^0$/d

%description 
%{desc}


%package -n fonts-otf-d-din-condensed
Group: System/Fonts/True type
Summary:        Datto D-DIN condensed fonts

%description -n fonts-otf-d-din-condensed 
%{desc}

This package provides the condensed fonts variant.

%package -n fonts-otf-d-din-exp
Group: System/Fonts/True type
Summary:        Datto D-DIN expanded fonts

%description -n fonts-otf-d-din-exp 
%{desc}

This package provides the expanded fonts variant.

%prep
%setup -n %{oldname}-%{version} -q -c



%build
# Nothing to build

%install

# Install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

# Install fontconfig data
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-exp.conf

for fconf in %{fontconf}.conf %{fontconf}-condensed.conf %{fontconf}-exp.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Install AppStream metadata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p *.metainfo.xml %{buildroot}%{_datadir}/metainfo
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc woff woff2 WOFF WOFF2 otb OTB pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*|otb|OTB) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
	woff|WOFF) type=woff;;
	woff2|WOFF2) type=woff2;;
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
# Validate AppStream metadata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/D-DIN.otf
%{_fontsdir}/*/%{_fontstem}/D-DIN-*.otf
%doc --no-dereference OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}.metainfo.xml

%files -n fonts-otf-d-din-condensed
%{_fontconfig_templatedir}/%{fontconf}-condensed.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-condensed.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/D-DINCondensed*.otf
%doc --no-dereference OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}-condensed.metainfo.xml

%files -n fonts-otf-d-din-exp
%{_fontconfig_templatedir}/%{fontconf}-exp.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-exp.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/D-DINExp*.otf
%doc --no-dereference OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}-exp.metainfo.xml


%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.0-alt1_10
- new version

