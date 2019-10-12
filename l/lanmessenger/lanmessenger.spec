Name: lanmessenger
Version: 1.2.39
Release: alt2

Summary: LAN Messenger for Windows, Mac, Linux
License: GPLv3+
Group: Other

Url: https://github.com/lanmessenger/lanmessenger
Source: %name-%version.tar
Patch0: %name-%version.patch
Patch1: %name-alt-openssl1.1.patch
Patch2: %name-alt-use-LIBDIR.patch
Patch3: %name-alt-install-program.patch
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libssl-devel

%description
%summary

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch %e2k
# strip UTF-8 BOM for lcc < 1.24
find -type f -print0 -name '*.cpp' -o -name '*.hpp' -o -name '*.cc' -o -name '*.h' |
	xargs -r0 sed -ri 's,^\xEF\xBB\xBF,,'
%endif

%build
pushd lmcapp/src
%qmake_qt5 LIBDIR=%_libdir
%make_build
popd
pushd lmc/src
%qmake_qt5
%make_build
popd

%install
%install_qt5 -C lmcapp/src
%install_qt5 -C lmc/src
rm -f %buildroot%_libdir/liblmcapp.so %buildroot%_qt5_libdatadir/liblmcapp.so

%files
%doc README.md
%_bindir/lan-messenger
%_libdir/liblmcapp.so.*

%changelog
* Sat Oct 12 2019 Michael Shigorin <mike@altlinux.org> 1.2.39-alt2
- E2K: strip UTF-8 BOM for lcc < 1.24
- Minor spec cleanup.

* Tue Dec 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.39-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.37-alt1
- Initial build for Sisyphus
