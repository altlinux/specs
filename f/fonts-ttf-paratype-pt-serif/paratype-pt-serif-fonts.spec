Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname paratype-pt-serif-fonts
%global fontname paratype-pt-serif
%global fontconf 57-%{fontname}

%global common_desc \
The PT Serif family was developed as a second part of the project \
a.'Public Types of Russian Federationa.'. This project aims at enabling \
The project is dedicated to the 300-year anniversary of the Russian civil \
type invented by Peter the Great from 1708 to 1710, and was realized \
with financial support from the Russian Federal Agency for Press and \
Mass Communications. \
\
PT Serif is a transitional serif face with humanistic terminals designed \
for use together with PT Sans and harmonized with PT Sans on metrics, \
proportions, weights and design. PT Serif consists of six styles: regular \
and bold weights with corresponding italics form a standard computer font \
family for basic text setting; two caption styles (regular and italic) \
are for texts of small point sizes. \
\
PT Serif was designed by Alexandra Korolkova with participation \
of Olga Umpeleva and under supervision of Vladimir Yefimov. \

Name:           fonts-ttf-paratype-pt-serif
Version:        20141121
Release:        alt1_2
Summary:        A pan-Cyrillic typeface

License:        OFL
URL:            http://www.paratype.com/public/
Source0:        http://www.fontstock.com/public/PTSerifOFL.zip
Source10:       %{oldname}-fontconfig.conf
Source11:       %{oldname}-caption-fontconfig.conf
Source12:       %{fontname}.metainfo.xml
Source13:       %{fontname}-caption.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
%common_desc

This package includes regular, bold and their italic styles.

%files
%{_fontconfig_templatedir}/%{fontconf}.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}.conf
%{_fontbasedir}/*/%{_fontstem}/PTF*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%package -n fonts-ttf-paratype-pt-serif-caption
Group: System/Fonts/True type
Summary:        A pan-Cyrillic typeface (caption forms for small text)
BuildRequires:  fontpackages-devel

%description -n fonts-ttf-paratype-pt-serif-caption
%common_desc

This package includes 2 captions styles for small text sizes.

%files -n fonts-ttf-paratype-pt-serif-caption
%{_fontconfig_templatedir}/%{fontconf}-caption.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-caption.conf
%{_fontbasedir}/*/%{_fontstem}/PTZ*.ttf
%doc *.txt
%{_datadir}/appdata/%{fontname}-caption.metainfo.xml


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
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caption.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-caption.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-caption.metainfo.xml
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

