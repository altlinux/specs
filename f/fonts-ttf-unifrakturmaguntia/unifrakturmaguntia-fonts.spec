Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: python unzip
# END SourceDeps(oneline)
%define oldname unifrakturmaguntia-fonts
%global fontname unifrakturmaguntia
%global fontconf 61-%{fontname}-fonts.conf
%global source_date 20140706


Name:          fonts-ttf-unifrakturmaguntia
Version:       0
Release:       alt1_0.3.%{source_date}
Summary:       Font that provide a Fraktur typeface that may be embedded on websites
License:       OFL
URL:           http://unifraktur.sourceforge.net/maguntia.html
Source0:       http://sourceforge.net/projects/unifraktur/files/fonts/UnifrakturMaguntia.2014-07-06.zip
Source10:      %{fontconf}
BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge
Source44: import.info

%description
UnifrakturMaguntia is based on Peter Wiegela.'s font Berthold Mainzer Fraktur. The
main differences from Peter Wiegela.'s font are the following:

- UnifrakturMaguntia uses OpenType for displaying the fonta.'s ligatures.
- UnifrakturMaguntia is suitable for @font-face embedding on the internet. It
  has a permissive license, the OFL, that explicitly allows font embedding.
- G. Ansmann has carefully redrawn all glyphs and significantly expanded the
  font.


%prep
%setup -q -n UnifrakturMaguntia.2014-07-06
# Correct end of line encoding for OFL.txt
sed -i 's/\r$//' OFL.txt


%build
fontforge -lang=ff -script "-" *.sfdir <<_EOF
i = 1
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5)
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
_EOF

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE10} \
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
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%doc OFL.txt *.pdf


%changelog
* Sat Nov 07 2015 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.20140706
- new version

