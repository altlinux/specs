Name: rack-plugin-freesurface
Version: 2.1.1
Release: alt1

Summary: Physical modeling system for Rack
License: GPLv3
Group: Sound
Url: https://github.com/freesurfacemodules/FreeSurface

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel
BuildRequires: pkgconfig(samplerate)

%description
Physical modeling system with a fully analog design

%prep
%setup

%build
%make_build RACK_DIR=%_datadir/rack/sdk

%install
make install RACK_DIR=%_datadir/rack/sdk \
     PLUGINS_DIR=%buildroot%_libdir/rack

%files
%doc README*
%_libdir/rack/*

%changelog
* Wed Sep 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.1-alt1
- 2.1.1 released

* Tue Feb 27 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.5-alt1
- 2.0.5 released
