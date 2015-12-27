Group: System/Fonts/True type
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname fontawesome-fonts
%global fontname fontawesome
%global fontconf 60-%{fontname}.conf

Name:		fonts-ttf-fontawesome
Version:	4.4.0
Release:	alt1_2

Summary:	Iconic font set
License:	OFL
URL:		http://fontawesome.io/
Source0:	http://fontawesome.io/assets/font-awesome-%{version}.zip
Source1:	%{oldname}-fontconfig.conf
Source2:	README-Trademarks.txt
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	ttembed
Source44: import.info


%description
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains OpenType and TrueType font files which are typically used
locally.

%package web
Group: System/Fonts/True type
License:	OFL and MIT
Requires:	fonts-ttf-fontawesome = %{version}-%{release}
Summary:	Iconic font set, web files

%description web
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format versions 1 and 2, Embedded OpenType and SVG font files which are
typically used on the web.

%prep
%setup -q -n font-awesome-%{version}
cp -p %SOURCE2 .

%build
ttembed fonts/*.ttf fonts/*.otf

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*.ttf fonts/*.otf fonts/*.woff fonts/*.svg fonts/*.woff2 fonts/*.eot %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

mkdir -p %{buildroot}%{_datadir}/font-awesome-web/
cp -a css less scss %{buildroot}%{_datadir}/font-awesome-web/
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

# files:
%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.ttf
%{_fontbasedir}/*/%{_fontstem}/*.otf
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.svg
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2
%exclude %{_datadir}/fonts/fontawesome/fontawesome-webfont.eot

%doc README-Trademarks.txt

%files web
%{_datadir}/font-awesome-web/
%{_datadir}/fonts/fontawesome/fontawesome-webfont.svg
%{_datadir}/fonts/fontawesome/fontawesome-webfont.woff
%{_datadir}/fonts/fontawesome/fontawesome-webfont.woff2
%{_datadir}/fonts/fontawesome/fontawesome-webfont.eot

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.4.0-alt1_1
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- update to new release by fcimport

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.3-alt1_2
- converted for ALT Linux by srpmconvert tools

