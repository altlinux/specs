Name: repocop-demo-menu-altlinux-sisyphus
Version: 0.04.20120704
Release: alt1

Summary: menu test with demo applications
License: %lgpl2plus
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: %name-%version.tar
Packager: Igor Vlasenko <viy@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: perl(File/Path.pm) perl(DBI.pm) perl(DBD/SQLite.pm)
BuildArch: noarch
Requires: /usr/bin/kdialog

%description
The package contains demonstration versions of desktop menu entries for all 
existing sisyphus applications. Use it for menu layout testing purposes.

%prep
%setup

%build
#./generate_fake_menus freedesktop-desktop.db

%install
mkdir -p %buildroot%_datadir/desktop-directories %buildroot%_sysconfdir/xdg/menus
mkdir -p %buildroot%_bindir
#%buildroot%_desktopdir

cp -a usr %buildroot/

cat > %buildroot%_bindir/demo-menu-entry << 'EOF'
#!/bin/sh
categories=`grep '^Categories=' "$1"`
terminal=`grep '^X-Demo-Terminal=' "$1" | sed -e s,X-Demo-,,`
id=`grep '^X-Demo-ID=' "$1" | sed -e s,X-Demo-,,`
kdialog --title 'demo application' --msgbox 'This is menu demo, not a real application.\nUninstall %name to remove me.\n\n'"file=$1\n\n""$categories\n$terminal\n""$id"
EOF
chmod 755 %buildroot%_bindir/demo-menu-entry
install -Dm644 demo-menu-entry.png %buildroot%_liconsdir/demo-menu-entry.png

%files 
%_bindir/demo-menu-entry
%_liconsdir/demo-menu-entry.png
%_datadir/kde*/*
%_desktopdir/*

%changelog
* Wed Jul 04 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120704-alt1
- repocop cronbuild 20120704. At your service.

* Wed Jun 20 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120620-alt1
- repocop cronbuild 20120620. At your service.

* Wed Jun 06 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120606-alt1
- repocop cronbuild 20120606. At your service.

* Wed May 23 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120523-alt1
- repocop cronbuild 20120523. At your service.

* Wed May 09 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120509-alt1
- repocop cronbuild 20120509. At your service.

* Wed Apr 25 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120425-alt1
- repocop cronbuild 20120425. At your service.

* Wed Apr 11 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120411-alt1
- repocop cronbuild 20120411. At your service.

* Wed Mar 28 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120328-alt1
- repocop cronbuild 20120328. At your service.

* Wed Mar 14 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120314-alt1
- repocop cronbuild 20120314. At your service.

* Wed Feb 29 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120229-alt1
- repocop cronbuild 20120229. At your service.

* Wed Feb 15 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120215-alt1
- repocop cronbuild 20120215. At your service.

* Wed Feb 01 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120201-alt1
- repocop cronbuild 20120201. At your service.

* Wed Jan 18 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120118-alt1
- repocop cronbuild 20120118. At your service.

* Wed Jan 04 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04.20120104-alt1
- repocop cronbuild 20120104. At your service.

* Wed Dec 21 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111221-alt1
- repocop cronbuild 20111221. At your service.

* Wed Dec 07 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111207-alt1
- repocop cronbuild 20111207. At your service.

* Wed Nov 23 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111123-alt1
- repocop cronbuild 20111123. At your service.

* Wed Nov 09 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111109-alt1
- repocop cronbuild 20111109. At your service.

* Wed Oct 26 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111026-alt1
- repocop cronbuild 20111026. At your service.

* Wed Oct 12 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20111012-alt1
- repocop cronbuild 20111012. At your service.

* Wed Sep 28 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110928-alt1
- repocop cronbuild 20110928. At your service.

* Wed Sep 14 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110914-alt1
- repocop cronbuild 20110914. At your service.

* Wed Aug 31 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110831-alt1
- repocop cronbuild 20110831. At your service.

* Wed Aug 17 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110817-alt1
- repocop cronbuild 20110817. At your service.

* Wed Aug 03 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110803-alt1
- repocop cronbuild 20110803. At your service.

* Wed Jul 20 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110720-alt1
- repocop cronbuild 20110720. At your service.

* Wed Jul 06 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110706-alt1
- repocop cronbuild 20110706. At your service.

* Wed Jun 22 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110622-alt1
- repocop cronbuild 20110622. At your service.

* Wed Jun 08 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110608-alt1
- repocop cronbuild 20110608. At your service.

* Wed May 25 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110525-alt1
- repocop cronbuild 20110525. At your service.

* Wed May 11 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110511-alt1
- repocop cronbuild 20110511. At your service.

* Wed Apr 27 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110427-alt1
- repocop cronbuild 20110427. At your service.

* Thu Apr 21 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110421-alt1
- repocop cronbuild 20110421. At your service.

* Thu Apr 07 2011 Cronbuild Service <cronbuild@altlinux.org> 0.04.20110407-alt1
- repocop cronbuild 20110407. At your service.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.04.20110329-alt1
- repocop cronbuild 20110329. At your service.

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.04.20110328-alt1
- update 20110328

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.04.20110326-alt1
- package generated .desktop instead of db

* Thu Mar 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.03.20110324-alt1
- support for Terminal key

* Tue Mar 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.02.20110321-alt1
- added categories info.

* Wed Mar 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.01.20110315-alt1
- Initial build

