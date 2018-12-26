%def_with openssl1_1

Name:     lanmessenger
Version:  1.2.39
Release:  alt1

Summary:  LAN Messenger for Windows, Mac, Linux
License:  GPLv3+
Group:    Other
Url:      https://github.com/lanmessenger/lanmessenger

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch:    %name-%version.patch
%if_with openssl1_1
Patch1:   %name-alt-openssl1.1.patch
%endif
Patch2:   %name-alt-use-LIBDIR.patch
Patch3:   %name-alt-install-program.patch

BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: libssl-devel

%description
%summary

%prep
%setup
%patch -p1
%if_with openssl1_1
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

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
* Tue Dec 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.39-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.37-alt1
- Initial build for Sisyphus
