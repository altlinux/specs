Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname gust-antykwa-torunska-fonts
%global fontname gust-antykwa-torunska
%global shortname antt
%global fontconf 69-%{fontname}.conf

Name:           fonts-otf-gust-antykwa-torunska
Version:        2.08
%global versiontag %(echo %{version}|tr . _)
Release:        alt1_5
Summary:        Two-element typeface for typesetting of small prints
License:        LPPL
URL:            http://jmn.pl/en/antykwa-torunska/
Source0:        http://jmn.pl/pliki/AntykwaTorunska-otf-%{versiontag}.zip
Source1:        %{oldname}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
Antykwa ToruA.ska (meaning just "Antiqua of Torun") is a two-element
typeface designed by Zygfryd Gardzielewski in the 50a.'s.

The font is mainly used for typesetting of small prints. Its
characteristic features are the widening of vertical stems at the top
and the wave-like form of some of the horizontal and diagonal lines as
well as of the serifs.

The current version contains a greatly extended character set (e.g.,
cyrillic, greek, most often used mathematical symbols and currency
symbols, additional ligatures) compared to the original, as well as
additional typefaces (light, regular, medium and bold in normal and
condensed widths).

%prep
%setup -q -n %{shortname}-otf

%build

%install
mkdir -p %{buildroot}%{_fontdir}
cp -p *.otf %{buildroot}%{_fontdir}

mkdir -p %{buildroot}%{_fontconfig_templatedir} \
         %{buildroot}%{_fontconfig_confdir}
cp -p %{SOURCE1} \
         %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
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

%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf

%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1_5
- converted for ALT Linux by srpmconvert tools

