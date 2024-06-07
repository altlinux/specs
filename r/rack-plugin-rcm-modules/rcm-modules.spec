Name: rack-plugin-rcm-modules
Version: 0.6.13
Release: alt1

Summary: RCM modules for VCV Rack
License: GPLv3
Group: Sound
Url: https://github.com/Rcomian/rcm-modules

ExclusiveArch: aarch64 x86_64

Source: %name-%version-%release.tar

BuildRequires: rack-devel

%description
%summary

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
* Fri Jun 07 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.13-alt1
- 0.6.13 released
