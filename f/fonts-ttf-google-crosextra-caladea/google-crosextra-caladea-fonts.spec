%define oldname google-crosextra-caladea-fonts
%global fontname google-crosextra-caladea
%global fontconf62 62-%{fontname}
%global fontconf30 30-0-%{fontname}

%global archivename crosextrafonts-20130214

Name:           fonts-ttf-google-crosextra-caladea
Version:        1.002
Release:        alt1_0.4.20130214
Summary:        Serif font metric-compatible with Cambria font

Group:          System/Fonts/True type
# License added in font as "otfinfo -i Caladea-Regular.ttf | grep License"
# also from http://code.google.com/p/chromium/issues/detail?id=280557
License:        ASL 2.0
URL:            http://code.google.com/p/chromium/issues/detail?id=168879
Source0:        http://gsdview.appspot.com/chromeos-localmirror/distfiles/%{archivename}.tar.gz
Source1:        30-0-%{fontname}-fontconfig.conf
Source2:        62-%{fontname}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Source44: import.info

%description
Caladea is metric-compatible with Cambria font. This font is a serif
typeface family based on Lato.

%prep
%setup -q -n %{archivename}


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf30}-fontconfig.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf62}-fontconfig.conf

ln -s %{_fontconfig_templatedir}/%{fontconf30}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf30}-fontconfig.conf
ln -s %{_fontconfig_templatedir}/%{fontconf62}-fontconfig.conf \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf62}-fontconfig.conf
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
%{_fontconfig_templatedir}/*-%{fontname}-fontconfig.conf
%config(noreplace) %{_fontconfig_confdir}/*-%{fontname}-fontconfig.conf
%{_fontbasedir}/*/%{_fontstem}/*.ttf

%doc


%changelog
* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1_0.4.20130214
- converted for ALT Linux by srpmconvert tools

