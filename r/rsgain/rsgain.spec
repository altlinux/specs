Name: rsgain
Version: 3.5.2
Release: alt1

Summary: ReplayGain 2.0 utility
License: BSD-2-Clause
Group: Sound
Url: https://github.com/complexlogic/rsgain

Source: %name-%version.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(libebur128)
BuildRequires: pkgconfig(inih)
BuildRequires: pkgconfig(fmt)

%description
ReplayGain 2.0 command line utility.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
install -pm0644 -D docs/rsgain.1 %buildroot%_man1dir/rsgain.1

%files
%doc LICENSE README*
%_bindir/rsgain
%_datadir/rsgain
%_man1dir/rsgain.1*

%changelog
* Mon Sep 23 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.5.2-alt1
- 3.5.2 released
