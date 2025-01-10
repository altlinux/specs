%def_enable snapshot
%define _name cosmic-wallpapers
%define ver_major 1.0
%define beta .alpha.5

Name: %_name
Version: %ver_major.0
Release: alt0.5%beta

Summary: COSMIC Wallpapers
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-wallpapers

Vcs: https://github.com/pop-os/cosmic-wallpapers.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

%description
Wallpapers for the COSMIC desktop environment.

%prep
%setup -n %_name-%version%beta

%install
%makeinstall_std

%files
%_datadir/backgrounds/cosmic/
%doc README*

%changelog
* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- first build for Sisyphus


