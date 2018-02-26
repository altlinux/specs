Name: openpref
Version: 0.1.3
Release: alt2

Summary: OpenPref - Preference game for linux
Summary(ru_RU.UTF-8): OpenPref - преферанс для Linux
Group: Games/Cards
License: GPLv3+

Source0: %name-%version.tar.gz
Source1: openpref.desktop

Patch0: openpref-0.1.3-alt-locale.patch

Url: http://sourceforge.net/projects/openpref/

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Oct 17 2009
BuildRequires: gcc-c++ libqt4-devel

%description
OpenPref - Preference game for linux.

%description -l ru_RU.UTF-8
OpenPref - преферанс для Linux.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4
%make_build

%install
mkdir -p %buildroot%_bindir/
install -m755 -p %name %buildroot%_bindir/

mkdir -p %buildroot%_desktopdir
install -m644 -p %SOURCE1 %buildroot%_desktopdir/

mkdir -p %buildroot%_datadir/openpref/
install -m644 -p openpref_ru.qm %buildroot%_datadir/openpref/

%files
%_bindir/%name
%_desktopdir/%name.desktop
%dir %_datadir/openpref
%_datadir/openpref/openpref_ru.qm

%changelog
* Sat Oct 17 2009 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt2
- update License to GPLv3+

* Sat Oct 17 2009 Igor Zubkov <icesik@altlinux.org> 0.1.3-alt1
- 0.1.2 -> 0.1.3

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 0.1.2-alt1
- 0.1.0 -> 0.1.2 (closes: #21014)

* Sun Aug 02 2009 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt6
- apply repocop patch

* Fri Jul 11 2008 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt5
- fix desktop file

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt4
- add Packager tag
- convert menu file to desktop file
- buildreq

* Wed Mar 21 2007 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt3
- fix build on x86_64

* Tue Mar 20 2007 Igor Zubkov <icesik@altlinux.org> 0.1.0-alt2.1
- rebuild with new gcc flags (-Wl,--as-needed)

* Wed Dec 28 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.0-alt2
- fix menu file

* Mon Oct 31 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.0-alt1
- Initial build for Sisyphus
