Name:           i7z
Version:        93.20131013
Release:        alt2
Summary:        A better i7 (and now i3, i5) reporting tool for Linux
License:        GPLv2
URL:            https://github.com/ajaiantilal/i7z
Group:          Monitoring

ExclusiveArch:  %ix86 x86_64
Source:         %name-%version.tar

BuildPreReq:    rpm-macros-qt5
BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  qt5-base-devel

%define global_desc i7z is a low level hardware monitoring tool for i3/i5/i7 CPUs.
%description
%global_desc

%package        gui
Summary:        A better i7 (and now i3, i5) reporting tool for Linux (qt5 GUI version)
Group:          Monitoring

%description gui
A Qt5 GUI version of the i7.
%global_desc

%package        perfmon
Summary:        A better i7 (and now i3, i5) reporting tool for Linux (perfomance monitor)
Group:          Monitoring

%description perfmon
Provides perfmon-i7z perfomance and temperature monitoring tool.
%global_desc

%prep
%setup -q
cd GUI
%qmake_qt5 i7z_GUI.pro
cd ..

%build
%make_build
%make_build -C GUI clean
%make_build -C GUI
%make_build -C perfmon-i7z

%install
%makeinstall_std
install GUI/i7z_GUI %buildroot/%_sbindir
%makeinstall_std -C perfmon-i7z


%files
%_sbindir/i7z
%_sbindir/i7z_rw_registers
%_docdir/*
%_mandir/man1/*

%files gui
%_sbindir/i7z_GUI

%files perfmon
%_sbindir/perfmon-i7z

%changelog
* Fri Dec 04 2020 Andrew Savchenko <bircoph@altlinux.org> 93.20131013-alt2
- Fix build with -fcommon (or gcc-10)

* Sun Oct 21 2018 Andrew Savchenko <bircoph@altlinux.org> 93.20131013-alt1
- Initial spec.
- Use latest upstream snapshot.
