Group: System/Fonts/True type
%define oldname mozilla-zilla-slab-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname        mozilla-zilla-slab
%global fontconf        60-%{fontname}

# Common description
%global common_desc \
Zilla Slab is a casual and contemporary slab serif with a good amount of quirk. \
It is the official brand typeface for Mozilla. \
%{nil}

Name:      fonts-otf-mozilla-zilla-slab
Version:   1.002
Release:   alt1_4
Summary:   Mozilla's Zilla Slab fonts
License:   OFL
URL:       https://mozilla.design/mozilla/typography/
Source0:   https://github.com/mozilla/zilla-slab/releases/download/v%{version}/Zilla-Slab-Fonts-v%{version}.zip
Source1:   %{fontname}.conf
Source2:   %{fontname}-highlight.conf
BuildArch: noarch
BuildRequires: fontpackages-devel
BuildRequires: unzip
Requires:  %{name}-common = %{version}-%{release}
Source44: import.info

%description
%common_desc

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/ZillaSlab-*.otf


%package -n fonts-otf-mozilla-zilla-slab-common
Group: System/Fonts/True type
Summary:  Common files for Mozilla's Zilla Slab font set
%description -n fonts-otf-mozilla-zilla-slab-common
%common_desc
This package consists of files used by other %{oldname} packages.



%package -n fonts-otf-mozilla-zilla-slab-highlight
Group: System/Fonts/True type
Summary:   Highlighted version of Mozilla's Zilla Slab font
Requires:  %{name}-common = %{version}-%{release}
%description -n fonts-otf-mozilla-zilla-slab-highlight
%common_desc
This package contains the highlighted version of Mozilla's Zilla Slab font.

%files -n fonts-otf-mozilla-zilla-slab-highlight
%{_fontconfig_templatedir}/%{fontconf}-highlight.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-highlight.conf
%dir %{_fontsdir}/*/%{_fontstem}/
%{_fontsdir}/*/%{_fontstem}/ZillaSlabHighlight-*.otf


%prep
%setup -q -n zilla-slab
cp -p %{SOURCE1} %{SOURCE2} .

# Fix permissions for license file
chmod 644 LICENSE

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p otf/*.otf  %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontname}.conf \
  %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{fontname}-highlight.conf \
  %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-highlight.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-highlight.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fontconf
done
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


%files -n fonts-otf-mozilla-zilla-slab-common
%doc --no-dereference LICENSE
%dir %{_fontsdir}/*/%{_fontstem}


%changelog
* Sun Feb 20 2022 Igor Vlasenko <viy@altlinux.org> 1.002-alt1_4
- new version

