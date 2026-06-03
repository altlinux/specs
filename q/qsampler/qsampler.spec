Name: qsampler
Version: 1.0.2
Release: alt1

Summary: A LinuxSampler Qt GUI
License: GPLv2
Group: Sound
Url: https://qsampler.sourceforge.io/
VCS: https://github.com/rncbc/qsampler

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(lscp)
BuildRequires: pkgconfig(gig)

%description
Qsampler is a LinuxSampler GUI front-end application written in C++ around
the Qt framework using Qt Designer. At the moment it just wraps as a client
reference interface for the LinuxSampler Control Protocol (LSCP).

%prep
%setup

%build
%cmake -DCONFIG_WAYLAND=TRUE
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE README

%_bindir/qsampler
%_datadir/qsampler

%_datadir/metainfo/*.xml
%_datadir/mime/packages/*.xml
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%_iconsdir/*/*/*/*.svg

%_man1dir/qsampler.1*

%changelog
* Wed Jun 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.2-alt1
- 1.0.2 released

* Fri Jul 25 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.1-alt1
- 1.0.1 released

