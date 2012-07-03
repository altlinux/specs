Name: alt-docs-main
Version: 0.5.1
Release: alt1.qa3
Group: Documentation
Packager: ALT Docs Team <docs@packages.altlinux.org>

Source0: %name-%version.tar.bz2

License: %fdl
BuildArch: noarch
Url: http://heap.altlinux.ru/alt-docs/index.html

BuildRequires(pre): rpm-build-licenses >= 0.6
PreReq: alt-docs-genextras >= 0.2
Requires: webclient

Summary: ALT Linux Documentation main page
Summary(ru_RU.KOI8-R): Главная страница документации ALT Linux

# Automatically added by buildreq on Fri Apr 07 2006
BuildRequires: ALDConvert python-modules python-modules-compiler python-modules-encodings

%description
Main page for ALT Linux Documentation. This package does not contain 
documentation itself but provides convenient interface for all installed 
documentation resources via menu and desktop link. It is also intented to 
serve as a main page of ALT Linux Documantation website.

%description -l ru_RU.KOI8-R
Главная страница документации ALT Linux. Данный пакет не содержит 
собственно документации, он нужен, чтобы обеспечить удобный доступ 
к документации через меню и ссылку на десктопе. Он также будет служить 
главной страницей сайта документации ALT Linux.

%prep
%setup -q -n %name-%version

%build
make

%install
# TODO: deprecated path; kde no more lives there
install -Dm644 %_builddir/%name-%version/alt-docs-main-link.desktop %buildroot%_datadir/apps/kdesktop/DesktopLinks/%name.desktop
# menu
install -Dm644 %_builddir/%name-%version/alt-docs-main-menu.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_docdir/alt-docs
#cp -r %_builddir/%name-%version/* %buildroot%_docdir/alt-docs/
make DESTDIR=%buildroot install

%post
%_bindir/alt-docs-genextras alt-docs

%files
%_docdir/alt-docs
%_desktopdir/%name.desktop
# TODO: deprecated path; kde no more lives there
%_datadir/apps/kdesktop/DesktopLinks/%name.desktop


%changelog
* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.qa3
- NMU: .desktop file cleanup (use url_handler)

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.qa2
NMU: converted menu to desktop file

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for alt-docs-main
  * obsolete-call-in-post-alternatives-0.3 for alt-docs-main
  * postclean-05-filetriggers for spec file

* Tue Feb 24 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.5.1-alt1
- fdl.html: fix broken link (#3223)

* Wed Apr 16 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.5-alt1
- made modules link more visible (#13756)
- added altlogo
- added menu (links to subparts)

* Sun Aug 19 2007 Artem Zolochevskiy <azol@altlinux.ru> 0.4-alt7
- Fixed desktop link path

* Mon May 21 2007 Kirill Maslinsky <kirill@altlinux.ru> 0.4-alt6
- Fixed links on main page
  + relative links fixed (due to change in m-k link syntax)
  + external links to project web pages updated
- Change package group to more appropriate: Documentation

* Sun May 20 2007 Vitaly A. Ostanin <vyt@altlinux.ru> 0.4-alt5
- Fixed links to installed modules
- Fixed install in Makefile

* Tue Sep 12 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.4-alt4
- Makefile:
  + index.html build fixed (closes #9232 once more)
  + list of installed files fixed

* Fri Apr 07 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.4-alt3
- fixed html links on index page

* Tue Apr 04 2006 Kirill Maslinsky <kirill@altlinux.ru> 0.4-alt2
- content:
  + main page text rewritten (closes inconsistensy described in #9232 and more)
  + main page now in m-k source format
- package:
  + fixed incorrect alternatives removal (closes #8308)
  + URL changed to real one
  + spec cleanup (unnecessary macros removed)
  + Makefile and build stage added (m-k -> html)

* Tue Oct 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.4-alt1
- all alternatives and absolute links removed

* Mon Sep 26 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt4
- fixed typo in alternative for index.html

* Mon Sep 19 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt3
- slightly updated

* Mon Jul 18 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt2
- hacked for release, to be fixed

* Wed Sep 01 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.3-alt1
- changed browser launch command in menu file ("/bin/sh -c" added)
- added sectioan and link for ALT development documentation, new
alternative and tap-page, consequently.

* Fri Jun 25 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.2-alt1
- Main page structured and rewritten
- Added automatically generated list of installed docs for various distributions
- FAQ section and new corresponing symlink in alt-docs added 
- Links to GPL and FDL point now to local copies (common-licenses package)
- Russian translation of GPL and FDL included (in license subdir)


* Fri May 28 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt3
- Added symbolic links for .css in alt-docs directory

* Mon May 24 2004 Kirill Maslinsky  <kirill@altlinux.ru> 0.1-alt2
- absolute links in index.html changed to relative 

* Fri Apr 30 2004 Kirill Maslinsky <kirill@altlinux.ru> 0.1-alt1
- initial working release 
