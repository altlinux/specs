Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname fontsquirrel-crete-round-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname fontsquirrel-crete-round
%global fontconf 63-%{fontname}.conf

Name:          fonts-otf-fontsquirrel-crete-round
Version:       0
Release:       alt1_0.2.20111222
Summary:       General purpose warm slab serif font
License:       OFL
URL:           https://www.fontsquirrel.com/fonts/crete-round
Source0:       https://www.fontsquirrel.com/fonts/download/crete-round#/crete-round.zip
Source1:       %{oldname}.conf
BuildArch:     noarch
BuildRequires: fontpackages-devel
Source44: import.info

%description
Crete Round is a warm slab serif providing a hint of softness to texts. It
started as a tailored version of the original Crete fonts -
www.type-together.com/Crete - created specially to serve as corporate typeface
for the type design competition Letter2 - www.letter2.org. Crete Round is more
independent from the original with modified terminals and serifs to create two
new fonts that deliver a more contemporary and functional appearance. The tall
x-height, low contrast and sturdy slabs prove to be surprisingly efficient for
web use. This font supports 128 languages and has 416 glyphs.

%prep
%setup -n %{oldname}-%{version} -qc

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p CreteRound-{Italic,Regular}.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
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
%{_fontbasedir}/*/%{_fontstem}/CreteRound-Italic.otf
%{_fontbasedir}/*/%{_fontstem}/CreteRound-Regular.otf

%doc *.txt

%changelog
* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.20111222
- new version

