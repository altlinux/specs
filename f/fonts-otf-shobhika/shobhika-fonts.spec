Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname shobhika-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname shobhika
%global fontconf 68-%{fontname}.conf

Name:		fonts-otf-shobhika
Version:	1.04
Release:	alt1_4
Summary:	Free Indian truetype/open type fonts
License:	OFL
URL:		https://github.com/Sandhi-IITBombay/Shobhika
Source0:	%{url}/releases/download/v%{version}/Shobhika-%{version}.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
Source44: import.info

%description
Shobhika is a free, open source, Unicode compliant, OpenType font with support \
for Devanagari, Latin, and Cyrillic scripts.\ 
It is available in two weightsa..regular and bold.\ 
The font is designed with over 1600 DevanA.garA. glyphs, including support \
for over 1100 conjunct consonants, as well as vedic accents.

%prep
%setup -q -n Shobhika-%{version}

chmod 644 *.txt

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}
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
%{_fontbasedir}/*/%{_fontstem}/*.otf
%doc AUTHORS.txt README.md CONTRIBUTORS.txt
%doc --no-dereference OFL.txt Copyright.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_4
- new version

