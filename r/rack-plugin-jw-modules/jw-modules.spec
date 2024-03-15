Name: rack-plugin-jw-modules
Version: 2.0.2
Release: alt1

Summary: JW modules for VCV Rack
License: BSD-3-Clause
Group: Sound
Url: https://github.com/jeremywen/JW-Modules

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
* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.2-alt1
- 2.0.2 released


