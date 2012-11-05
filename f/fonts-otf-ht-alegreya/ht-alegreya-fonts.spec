# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Group: System/Fonts/True type
%define oldname ht-alegreya-fonts
%global fontname alegreya
%global fontconf 60-%{fontname}.conf
%global common_desc \
Alegreya was chosen as one of 53 "Fonts of the Decade" at the ATypI Letter2 \
competition in September 2011, and one of the top 14 text type systems. It \
was also selected in the 2nd Bienal Iberoamericana de DiseA.o, competition \
held in Madrid in 2010. Alegreya is a typeface originally intended for \
literature. Among its crowning characteristics, it conveys a dynamic and \
varied rhythm which facilitates the reading of long texts. Also, it \
provides freshness to the page while referring to the calligraphic letter, \
not as a literal interpretation, but rather in a contemporary typographic \
language. The italic has just as much care and attention to detail in the \
design as the roman. The bold weights are strong, and the Black weights are \
really experimental for the genre. Not only does Alegreya provide great \
performance, but also achieves a strong and harmonious text by means of \
elements designed in an atmosphere of diversity.

Name:		fonts-otf-ht-alegreya
Version:	1.004
Release:	alt1_1
Summary:	A Serif typeface originally intended for literature
License:	OFL
URL:		http://www.huertatipografica.com.ar/tipografias/alegreya/ejemplos.html
Source0:	http://www.huertatipografica.com.ar/descargas/Alegreya.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	ht-%{fontname}SC-fonts-fontconfig.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
%common_desc

%package -n fonts-otf-ht-alegreya-smallcaps
Group: System/Fonts/True type
Summary:	SmallCaps variant of the Alegreya font family

%description -n fonts-otf-ht-alegreya-smallcaps
%common_desc

This is the SmallCaps variant, in which the Capital letters are smaller.

%prep
%setup -q -c
sed -i 's/\r//' OFL.txt

%build
# Nothing to do here.

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/60-%{fontname}SC.conf

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/60-%{fontname}SC.conf \
	%{buildroot}%{_fontconfig_confdir}/60-%{fontname}SC.conf
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
%{_fontbasedir}/*/%{_fontstem}/Alegreya-*.otf
%doc OFL.txt

%files -n fonts-otf-ht-%{fontname}-smallcaps
%{_fontconfig_templatedir}/60-%{fontname}SC.conf
%config(noreplace) %{_fontconfig_confdir}/60-%{fontname}SC.conf
%{_fontbasedir}/*/%{_fontstem}/AlegreyaSC-*.otf
%doc OFL.txt

%changelog
* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1_1
- fc import

