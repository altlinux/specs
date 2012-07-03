Name:    tetex-latex-feynmf
Version: 1.08
Release: alt3.1.1
Summary: A combined LaTeX/Metafont package for easy drawing of professional quality Feynman diagrams.
Summary(ru_RU.KOI8-R): Макропакет для LaTeX/Metafont для создания фейнмановских диаграмм с проффесиональным графическим качеством.
License: GPL
Group:   Publishing
URL:     http://www.ctan.org

BuildArchitectures: noarch

Requires: tetex-core tetex-latex
Provides: feynmf

Obsoletes: feynmf

Source0: feynmf-%version.tar.bz2

# Automatically added by buildreq on Sun Mar 21 2004
BuildRequires: tetex-core tetex-latex
BuildRequires: perl-podlators

%description 
A combined LaTeX/Metafont package for easy drawing of professional quality
Feynman diagrams.

%description -l ru_RU.KOI8-R
Макропакет для LaTeX/Metafont для создания фейнмановских диаграмм с
проффесиональным графическим качеством.

%prep
%setup -q -n feynmf

%build
%make

%install
%__install -d $RPM_BUILD_ROOT{%_bindir,%_man1dir,%_datadir/texmf/{doc/latex,tex/latex/feynmf,metafont/misc,metapost/misc}}
%makeinstall
ln -sf ../../../doc/%name-%version  $RPM_BUILD_ROOT%_datadir/texmf/doc/latex/feynmf


%files
%_bindir/*
%_datadir/texmf/tex/latex/feynmf
%_datadir/texmf/meta*/misc/*
%_datadir/texmf/doc/latex/*
%_man1dir/*
%doc manual.ps.gz COPYING README Tutorial

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.08-alt3.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Nov 05 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.08-alt3.1
- NMU (by repocop): the following fixes applied:
  * altlinux-policy-tex-obsolete-util-calls-in-post for tetex-latex-feynmf

* Sun Aug 29 2004 Yury A. Zotov <yz@altlinux.ru> 1.08-alt3
- typo in summary and description corrected

* Thu May 27 2004 Yury A. Zotov <yz@altlinux.ru> 1.08-alt2
- package renamed to tetex-latex-feynmf

* Sun Mar 21 2004 Yury A. Zotov <yz@altlinux.ru> 1.08-alt1
- first build for Sisyphus
