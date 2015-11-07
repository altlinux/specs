Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname paratype-pt-mono-fonts
%global fontname paratype-pt-mono
%global fontconf 57-%{fontname}

%global common_desc \
Font PT Monoa.. is the last addition to the pan-Cyrillic font superfamily \
including PT Sans and PT Serif developed for the project a.'Public Types \
of Russian Federationa.'. \
\
PT Mono was developed for the special needs a.. for use in forms, tables, \
work sheets etc. Equal widths of characters are very helpful in setting \
complex documents, with such font you may easily calculate size of entry \
fields, column widths in tables and so on. One of the most important area \
of use is Web sites of a.'electronic governmentsa.' where visitors have to fill \
different request forms. PT Mono consists of Regular and Bold styles. \
\
PT Mono was designed by Alexandra Korolkova with participation of \
Isabella Chaeva and with financial support of Google.\


Name:           fonts-ttf-paratype-pt-mono
Version:        20141121
Release:        alt1_2
Summary:        A pan-Cyrillic monospace typeface

License:        OFL
URL:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTMonoOFL.zip
Source10:       %{oldname}-fontconfig.conf
Source11:       %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc

This package consists of Regular and Bold styles.

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/PTM*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%prep
%setup -n %{oldname}-%{version} -q -c
sed -i "s|\r||g" *.txt

%build
echo "Nothing to build"

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

for fconf in %{fontconf}.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE11} \
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


%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 20141121-alt1_2
- new version

