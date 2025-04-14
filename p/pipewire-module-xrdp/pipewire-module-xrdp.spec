%def_enable snapshot
%define _libexecdir %_prefix/libexec

Name: pipewire-module-xrdp
Version: 0.2
Release: alt1

Summary: Pipewire module for xrdp
License: MIT
Group: Sound
Url: https://github.com/neutrinolabs/pipewire-module-xrdp

Vcs: https://github.com/neutrinolabs/pipewire-module-xrdp.git

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-build-xdg
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.58

%description
This module allows xrdp to generate sound on a pipewire-based system.

%prep
%setup

%build
%autoreconf
%configure
%nil
%make_build

%check
%make -k check VERBOSE=1

%install
%makeinstall_std

%files
%_xdgconfigdir/autostart/pipewire-xrdp.desktop
%dir %_libexecdir/%name
%_libexecdir/%name/load_pw_modules.sh
%_libdir/pipewire-0.3/libpipewire-module-xrdp.so

%exclude %_libdir/pipewire-0.3/*.la

%changelog
* Mon Apr 14 2025 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first build for Sisyphus


