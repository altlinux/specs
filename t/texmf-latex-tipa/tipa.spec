%define origname tipa
Name: texmf-latex-%origname
Version: 1.3
Release: alt4
Summary: international phonetic alphabet package for LaTeX
Group: Publishing
BuildArch: noarch

Packager: Alex V. Myltsev <avm@altlinux.ru>

Obsoletes: %origname

License: Distributable
URL: http://www.l.u-tokyo.ac.jp/~fkr/tipa/
Source: %url/%origname-%version.tar.gz
Patch0: texmf-latex-tipa-install.patch

BuildRequires(pre): rpm-build-texmf
Requires: fonts-type1-tipa-tex

%description
tipa provides IPA fonts and a LaTeX package to typeset phonetic symbols.

%package -n %name-doc
Summary: documentation for tipa, phonetic symbols package for LaTeX
Group: Publishing

Obsoletes: %origname-doc

%description -n %name-doc
tipa provides IPA fonts and a LaTeX package to typeset phonetic symbols.
This package contains documentation files for tipa.

%package -n fonts-type1-%origname-tex
Summary: tipa TeX fonts
Group: Publishing

%description -n fonts-type1-%origname-tex
tipa provides IPA fonts and a LaTeX package to typeset phonetic symbols.
This package contains TeX fonts.

%prep
%setup -q -n %origname-%version
%patch0 -p1

%install
%makeinstall PREFIX=%buildroot%_texmfmain 

mkdir -p %buildroot%_sysconfdir/{tex-fonts.d,texmf/updmap.d}
echo "Map %origname.map" >%buildroot%_sysconfdir/tex-fonts.d/%origname.cfg
echo "Map %origname.map" >%buildroot%_sysconfdir/texmf/updmap.d/31-%origname.cfg
mkdir -p %buildroot%_texmfmain/fonts/map/dvips/tipa/
cp %buildroot%_texmfmain/dvips/config/tipa.map %buildroot%_texmfmain/fonts/map/dvips/tipa/tipa.map

%files
%dir %_texmfmain/fonts/source/
%_texmfmain/fonts/source/fkr
%dir %_texmfmain/fonts/tfm/
%_texmfmain/fonts/tfm/fkr
%dir %_texmfmain/tex/
%dir %_texmfmain/tex/latex/
%_texmfmain/tex/latex/tipa

%files -n fonts-type1-tipa-tex
%_sysconfdir/tex-fonts.d/%origname.cfg
%_sysconfdir/texmf/updmap.d/*
%dir %_texmfmain/dvips/
%_texmfmain/dvips/config
%dir %_texmfmain/fonts/
%dir %_texmfmain/fonts/map/
%dir %_texmfmain/fonts/map/dvips/
%_texmfmain/fonts/map/dvips/tipa
%dir %_texmfmain/fonts/type1/
%_texmfmain/fonts/type1/fkr

%files -n %name-doc
%doc doc/*

%changelog
* Thu Jul 02 2009 Grigory Batalov <bga@altlinux.ru> 1.3-alt4
- Package was renamed to texmf-latex-tipa, according to TeX policy.
- Fonts were splited.

* Sat Sep 02 2006 Alex V. Myltsev <avm@altlinux.ru> 1.3-alt3
- Created /etc/tex-fonts.d/tipa.cfg (#9950).

* Sat Mar 26 2005 Alex V. Myltsev <avm@altlinux.ru> 1.3-alt2
- Renamed package to tetex-latex-tipa [bug 6328].

* Wed Mar 09 2005 Alex V. Myltsev <avm@altlinux.ru> 1.3-alt1
- Initial build for ALT Linux.

