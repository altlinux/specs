%define api_ver 0.1
%define libname libcallaudio

Name: callaudiod
Version: 0.1.2
Release: alt1

Summary: Daemon for dealing with audio routing during phone calls
Group: System/Servers
License: GPL-3.0-or-later
Url: https://gitlab.com/mobian1/callaudiod

Vcs: https://gitlab.com/mobian1/callaudiod.git
Source: https://gitlab.com/mobian1/%name/-/archive/%version/%name-%version.tar.gz

Requires: %libname = %EVR

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse-mainloop-glib)

%description
%name is a daemon for dealing with audio routing during phone calls.
It provides a D-Bus interface allowing other programs to:
- switch audio profiles
- output audio to the speaker or back to its original port
- mute the microphone

%package -n %libname
Summary: Library for %name
Group: System/Libraries

%description -n %libname
This package provides %name library.

%package -n %libname-devel
Summary: Development files for %name
Group: Development/C++
Requires: %libname = %EVR

%description -n %libname-devel
This package contains libraries and header files for developing
applications that use %libname.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_bindir/callaudiocli
%_datadir/dbus-1/interfaces/org.mobian_project.CallAudio.xml
%_datadir/dbus-1/services/org.mobian_project.CallAudio.service
%doc README.md

%files -n %libname
%_libdir/%libname-%api_ver.so.*

%files -n %libname-devel
%_includedir/%libname-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%libname-%api_ver.pc

%changelog
* Wed Jan 05 2022 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Thu Sep 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- 0.1.1

* Fri Jul 16 2021 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus


