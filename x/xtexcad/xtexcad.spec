Name:     xtexcad
Version:  2.4.1
Release:  alt4
Packager: Igor Vlasenko <viy@altlinux.org>
License:  Other License(s), see package
Group:    Graphics
Url: http://www.ctan.org/tex-archive/help/Catalogue/entries/xtexcad.html
Provides: texcad xtexcad
Summary:  Drawing program for LaTeX pictures
Source:   %name-%version.tar.gz
Patch:    xtexcad-2.4-flex.patch
Patch1:   xtexcad-2.4.1-CRLF-fix.patch
Patch21:  xtexcad-2.4.diff
Patch22:  xtexcad-2.4-getcwd.patch

#TODO: \multiput

# Automatically added by buildreq on Mon Aug 25 2008 (-bi)
BuildRequires: flex gccmakedep groff-dvi imake libX11-devel libXext-devel libXaw-devel libXp-devel libXpm-devel xorg-cf-files

%description
A nice drawing program which is especially useful in cooperation
with LaTeX. Note the documentation and COPYRIGHT file in %_docdir.

Authors:
--------
    Klaus Zitzmann <zitzmann@infko.uni-koblenz.de>
    J.K.Wight <J.K.Wight@newcastle.ac.uk>
    Byron  Rakitzis <byron@netapp.com>
    Johannes Sixt <Johannes.Sixt@eudaptics.co.at>
    Notker Amann <amann@isr.uni-stuttgart.de>

%prep
%setup
%patch -p0
%patch1 -p1
%patch21 -p1
%patch22 -p0


%build
xmkmf -a
make
`grog -Tdvi xtexcad.man` > XTeXcad.dvi

%install
make install      DESTDIR=$RPM_BUILD_ROOT
make install.man  DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=XTeXCAD
GenericName=X TeX CAD
Comment=%{summary}
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Graphics;VectorGraphics;X-ALTLinux-TeX;
EOF

%files
%doc COPYRIGHT HISTORY MANIFEST README XTeXcad.dvi
%config(noreplace) %_sysconfdir/X11/app-defaults/*
%_bindir/*
%_mandir/man?/*
%_desktopdir/*

%changelog -n texcad
* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt4
- converted debian menu to freedesktop

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.4.1-alt3.3.1
- NMU:
  * updated build dependencies

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt3.3
- NMU (by repocop): the following fixes applied:
 * update_menus for xtexcad

* Mon Nov 10 2008 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt3.2
- rebuild with BReq: libXpm-devel

* Fri Nov 07 2008 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt3.1
- rebuild with libXaw (requested by Valery Inozemtsev)

* Mon Aug 25 2008 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt3
- spec cleanup; texcad symlink is removed

* Sat Nov 19 2005 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2
- fixed CRLF files processing

* Sat Apr 23 2005 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- first build based on SuSE 2.4-1009.1

