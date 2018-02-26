%define oldname wqy-zenhei-fonts
%global fontname wqy-zenhei
%global fontconf1 65-0-%{fontname}.conf
%global fontconf2 65-0-%{fontname}-sharp.conf
%define common_desc \
WenQuanYi Zen Hei is a Hei-Ti style (sans-serif type) Chinese \
outline font. It is designed for general purpose text formatting \
and on-screen display of Chinese characters and symbols from \
many other languages. The embolden strokes of the font glyphs \
produces enhanced screen contrast, making it easier to read \
recognize. The embedded bitmap glyphs further enhance on-screen \
performance, which can be enabled with the provided configuration \
files. WenQuanYi Zen Hei provides a rather complete coverage to \
Chinese Hanzi glyphs, including both simplified and traditional \
forms. The total glyph number in this font is over 35,000, including \
over 21,000 Chinese Hanzi. This font has full coverage to GBK(CP936) \
charset, CJK Unified Ideographs, as well as the code-points \
needed for zh_cn, zh_sg, zh_tw, zh_hk, zh_mo, ja (Japanese) \
and ko (Korean) locales for fontconfig. Starting from version \
0.8, this font package has contained two font families, i.e. \
the proportionally-spaced Zen Hei, and a mono-spaced face \
named "WenQuanYi Zen Hei Mono".

%define setscript zenheiset

Name:           fonts-ttf-wqy-zenhei
Version:        0.9.46
Release:        alt3_3
Summary:        WenQuanYi Zen Hei CJK Font

Group:          System/Fonts/True type
License:        GPLv2 with exceptions
URL:            http://wenq.org/enindex.cgi
Source0:        http://downloads.sourceforge.net/wqy/%{fontname}-%{version}-nightlybuild.tar.gz
Source1:        %{fontconf1}
Source2:        %{fontconf2}
Source3:        %{setscript}

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Obsoletes:      wqy-zenhei-fonts-common < 0.9.45-5 
Source44: import.info

%description
%common_desc

%prep
%setup -q -n %{fontname}

%build
%{nil}

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttc %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf1}
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf2}

ln -s %{_fontconfig_templatedir}/%{fontconf2} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf2}

install -m 0755 -d %{buildroot}%{_bindir}

install -m 0744 -p %{SOURCE3} \
        %{buildroot}%{_bindir}/%{setscript}
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz afm pfa pfb; do
    case "$fontpatt" in 
	pcf*) type=bitmap;;
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
%{_fontconfig_templatedir}/??-?-%{fontname}*.conf
%config(noreplace) %{_fontconfig_confdir}/??-?-%{fontname}*.conf
%{_fontbasedir}/*/%{_fontstem}/*.ttc
%dir %{_fontbasedir}/*/%{_fontstem}
%doc AUTHORS ChangeLog COPYING README
%attr(755, root, root) %{_bindir}/%{setscript}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.46-alt3_3
- rebuild to get rid of #27020

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.46-alt2_3
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.46-alt2_2
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.46-alt1_2
- initial release by fcimport

