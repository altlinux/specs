%define origname tipa
Name: tetex-latex-%origname
Version: 1.3
Release: alt3.1
Summary: international phonetic alphabet package for LaTeX
Group: Publishing
BuildArch: noarch

Packager: Alex V. Myltsev <avm@altlinux.ru>

Requires: tetex-latex
Obsoletes: %origname

License: Distributable
URL: http://www.l.u-tokyo.ac.jp/~fkr/tipa/
Source: %url/%origname-%version.tar.gz
Patch0: tetex-latex-tipa-install.patch

%description
tipa provides IPA fonts and a LaTeX package to typeset phonetic symbols.

%package -n %name-doc
Summary: documentation for tipa, phonetic symbols package for LaTeX
Group: Publishing

Obsoletes: %origname-doc

%description -n %name-doc
tipa provides IPA fonts and a LaTeX package to typeset phonetic symbols.
This package contains documentation files for tipa.

%prep
%setup -q -n %origname-%version
%patch0 -p1

%install

%define texprefix %_datadir/texmf
%makeinstall PREFIX=%buildroot%texprefix 

mkdir -p %buildroot%_sysconfdir/tex-fonts.d
echo "Map %origname.map" >%buildroot%_sysconfdir/tex-fonts.d/%origname.cfg

%files
%_sysconfdir/tex-fonts.d/%origname.cfg
%texprefix/dvips/config/*
%texprefix/fonts/source/fkr
%texprefix/fonts/tfm/fkr
%texprefix/fonts/type1/fkr
%texprefix/tex/latex/tipa

%files -n %name-doc
%doc doc/*

%changelog
* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3-alt3.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-tipa

* Sat Sep 02 2006 Alex V. Myltsev <avm@altlinux.ru> 1.3-alt3
- Created /etc/tex-fonts.d/tipa.cfg (#9950).

* Sat Mar 26 2005 Alex V. Myltsev <avm@altlinux.ru> 1.3-alt2
- Renamed package to tetex-latex-tipa [bug 6328].

* Wed Mar 09 2005 Alex V. Myltsev <avm@altlinux.ru> 1.3-alt1
- Initial build for ALT Linux.

