Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname comic-neue-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname comic-neue
%global fontconf 63-%{fontname}

%global common_desc \
Comic Neue is a font created by Craig Rozynski that takes inspiration\
from Comic Sans. It is perfect as a display face, for marking up comments,\
and writing passive aggressive office memos.


Name:           fonts-otf-comic-neue
Version:        2.51
Release:        alt1_4
Summary:        A typeface family inspired by Comic Sans

License:        OFL
URL:            http://comicneue.com/
Source0:        http://comicneue.com/%{fontname}-%{version}.zip
Source1:        %{fontname}-fontconfig.conf
Source2:        %{fontname}-angular-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       fonts-otf-comic-neue-common = %{version}-%{release}
Source44: import.info


%description
%common_desc


%package -n fonts-otf-comic-neue-common
Group: System/Fonts/True type
Summary:        Common files of %{oldname}

%description -n fonts-otf-comic-neue-common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-otf-comic-neue-angular
Group: System/Fonts/True type
Summary:        A typeface family inspired by Comic Sans, angular variant
Requires:       fonts-otf-comic-neue-common = %{version}-%{release}

%description -n fonts-otf-comic-neue-angular
%common_desc

The Comic Neue Angular variant features angular terminals rather than round.


%package -n fonts-web-comic-neue
Group: System/Fonts/True type
Summary:        A typeface family inspired by Comic Sans, web files
Requires:       fonts-otf-comic-neue-common = %{version}-%{release}

%description -n fonts-web-comic-neue
%common_desc

This package contains Web Open Font Format versions 1 and 2 files.


%prep
%setup -n %{oldname}-%{version} -q -c


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/OTF/*/*.otf %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/WebFonts/*.woff %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/WebFonts/*.woff2 %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-angular.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-angular.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc woff woff2 WOFF WOFF2 pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
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

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/ComicNeue-*.otf
%files -n fonts-otf-comic-neue-angular
%{_fontconfig_templatedir}/%{fontconf}-angular.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-angular.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/ComicNeueAngular-*.otf
%files -n fonts-web-comic-neue
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/ComicNeue*.woff
%{_fontsdir}/*/%{_fontstem}/ComicNeue*.woff2


%files -n fonts-otf-comic-neue-common
%doc %{fontname}-%{version}/Booklet-ComicNeue.pdf %{fontname}-%{version}/FONTLOG.txt
%doc --no-dereference %{fontname}-%{version}/OFL.txt %{fontname}-%{version}/OFL-FAQ.txt


%changelog
* Sat Feb 19 2022 Igor Vlasenko <viy@altlinux.org> 2.51-alt1_4
- new version

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 2.5-alt1_1
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_1
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5
- update to new release by fcimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_3
- converted for ALT Linux by srpmconvert tools

