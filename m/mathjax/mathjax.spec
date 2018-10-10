Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       mathjax
Version:    2.7.4
Release:    alt1_3
Summary:    JavaScript library to render math in the browser
License:    ASL 2.0
URL:        http://mathjax.org
Source0:    https://github.com/mathjax/MathJax/archive/%{version}.tar.gz#/mathjax-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:   web-assets-devel
BuildRequires:   fontpackages-devel

Requires:        web-assets-filesystem
Requires:        fonts-otf-mathjax-ams
Requires:        fonts-otf-mathjax-caligraphic
Requires:        fonts-otf-mathjax-fraktur fonts-otf-mathjax-main
Requires:        fonts-otf-mathjax-math
Requires:        fonts-otf-mathjax-sansserif
Requires:        fonts-otf-mathjax-script
Requires:        fonts-otf-mathjax-typewriter
Requires:        fonts-otf-mathjax-size1
Requires:        fonts-otf-mathjax-size2
Requires:        fonts-otf-mathjax-size3
Requires:        fonts-otf-mathjax-size4
Requires:        fonts-otf-mathjax-size1
Requires:        fonts-otf-mathjax-winie6
Requires:        fonts-otf-mathjax-winchrome
Requires:        %{name}-vector-fonts
Requires:        %{name}-stixweb-fonts
Source44: import.info

%description
MathJax is an open-source JavaScript display engine for LaTeX, MathML,
and AsciiMath notation that works in all modern browsers. It requires no
setup on the part of the user (no plugins to download or software to
install), so the page author can write web documents that include
mathematics and be confident that users will be able to view it
naturally and easily. Supports LaTeX, MathML, and AsciiMath notation
in HTML pages.

%global fontsummary Fonts used by MathJax to display math in the browser

%package       -n fonts-otf-mathjax-ams
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-ams
%{fontsummary}.

%package       -n fonts-otf-mathjax-caligraphic
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-caligraphic
%{fontsummary}.

%package       -n fonts-otf-mathjax-fraktur
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-fraktur
%{fontsummary}.

%package       -n fonts-otf-mathjax-main
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-main
%{fontsummary}.

%package       -n fonts-otf-mathjax-math
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-math
%{fontsummary}.

%package       -n fonts-otf-mathjax-sansserif
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-sansserif
%{fontsummary}.

%package       -n fonts-otf-mathjax-script
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-script
%{fontsummary}.

%package       -n fonts-otf-mathjax-typewriter
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-typewriter
%{fontsummary}.

%package       -n fonts-otf-mathjax-size1
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-size1
%{fontsummary}.

%package       -n fonts-otf-mathjax-size2
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-size2
%{fontsummary}.

%package       -n fonts-otf-mathjax-size3
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-size3
%{fontsummary}.

%package       -n fonts-otf-mathjax-size4
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-size4
%{fontsummary}.

%package       -n fonts-otf-mathjax-winie6
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-winie6
%{fontsummary}.

%package       -n fonts-otf-mathjax-winchrome
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   -n fonts-otf-mathjax-winchrome
%{fontsummary}.

%package       vector-fonts
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   vector-fonts
%{fontsummary}.

%package       stixweb-fonts
Group: Other
Summary:       %{fontsummary}
License:       OFL
%description   stixweb-fonts
%{fontsummary}.

%prep
%setup -q -n MathJax-%{version}
# Remove bundled fonts
rm -rf MathJax-%{version}/jax/output
rm -rf MathJax-%{version}/fonts/HTML-CSS/{Asana-Math,Gyre-Pagella,Gyre-Termes,Latin-Modern,Neo-Euler}

# Remove minified javascript.
for i in $(find . -type f -path '*unpacked*'); do \
  mv $i ${i//unpacked/}; done
find . -depth -type d -path '*unpacked*' -delete
for i in MathJax.js jax/output/HTML-CSS/jax.js jax/output/HTML-CSS/imageFonts.js; do \
    sed -r 's#(MathJax|BASE)[.]isPacked#1#' <$i >$i.tmp; \
    touch -r $i $i.tmp; \
    mv $i.tmp $i; \
done

# Remove .htaccess file, just in case
find . -name .htaccess -print -delete

%build
# minification should be performed here at some point

%install
mkdir -p %{buildroot}%{_jsdir}/mathjax
cp -pr MathJax.js config/ extensions/ jax/ localization/ test/ \
    %{buildroot}%{_jsdir}/mathjax/

mkdir -p %{buildroot}%{_fontbasedir}/otf/%{_fontstem}

# TeX fonts
mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/
cp -pr fonts/HTML-CSS/TeX/png %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/

cp -pr fonts/HTML-CSS/TeX/*/MathJax_*.{eot,otf,svg} %{buildroot}%{_fontbasedir}/otf/%{_fontstem}

for t in eot otf svg; do \
    mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/$t; \
    for i in fonts/HTML-CSS/TeX/$t/MathJax_*.$t; do \
        ln -s %{_fontbasedir}/otf/%{_fontstem}/$(basename $i) \
            %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/TeX/$t/; \
    done \
done

# STIX-Web fonts
mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/STIX-Web/
cp -pr fonts/HTML-CSS/STIX-Web/*/STIXMathJax_*.{eot,otf} %{buildroot}%{_fontbasedir}/otf/%{_fontstem}

for t in eot otf; do \
    mkdir -p %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/STIX-Web/$t; \
    for i in fonts/HTML-CSS/STIX-Web/$t/STIXMathJax_*.$t; do \
        ln -s %{_fontbasedir}/otf/%{_fontstem}/$(basename $i) \
            %{buildroot}%{_jsdir}/mathjax/fonts/HTML-CSS/STIX-Web/$t/; \
    done \
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
%{_jsdir}/mathjax
%doc README.md LICENSE

%files -n fonts-otf-mathjax-ams
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_AMS*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_AMS*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_AMS*.svg
%files -n fonts-otf-mathjax-caligraphic
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Caligraphic*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Caligraphic*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Caligraphic*.svg
%files -n fonts-otf-mathjax-fraktur
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Fraktur*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Fraktur*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Fraktur*.svg
%files -n fonts-otf-mathjax-main
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Main*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Main*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Main*.svg
%files -n fonts-otf-mathjax-math
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Math*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Math*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Math*.svg
%files -n fonts-otf-mathjax-sansserif
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_SansSerif*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_SansSerif*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_SansSerif*.svg
%files -n fonts-otf-mathjax-script
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Script*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Script*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Script*.svg
%files -n fonts-otf-mathjax-typewriter
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Typewriter*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Typewriter*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Typewriter*.svg
%files -n fonts-otf-mathjax-size1
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size1*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size1*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size1*.svg
%files -n fonts-otf-mathjax-size2
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size2*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size2*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size2*.svg
%files -n fonts-otf-mathjax-size3
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size3*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size3*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size3*.svg
%files -n fonts-otf-mathjax-size4
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size4*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size4*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_Size4*.svg
%files -n fonts-otf-mathjax-winie6
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_WinIE6*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_WinIE6*.otf
%files -n fonts-otf-mathjax-winchrome
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_WinChrome*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_WinChrome*.svg
%files -n %{name}-vector-fonts
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/MathJax_Vector*.eot
%{_fontbasedir}/*/%{_fontstem}/MathJax_Vector*.otf
%{_fontbasedir}/*/%{_fontstem}/MathJax_WinChrome*.svg
%files -n %{name}-stixweb-fonts
%dir %{_fontbasedir}/*/%{_fontstem}/
%{_fontbasedir}/*/%{_fontstem}/STIXMathJax_*.eot
%{_fontbasedir}/*/%{_fontstem}/STIXMathJax_*.otf

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.4-alt1_3
- update to new release by fcimport

* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.1-alt1_2
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_3
- update to new release by fcimport

* Thu Dec 31 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_2
- new version

