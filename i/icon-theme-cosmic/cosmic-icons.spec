%def_enable snapshot
%define _name cosmic-icons
%define ver_major 1.0
%define beta .alpha.1

%def_disable check

Name: icon-theme-cosmic
Version: %ver_major.0
Release: alt0.1%beta

Summary: COSMIC Icons
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-icons

Vcs: https://github.com/pop-os/cosmic-icons.git

BuildArch: noarch

Provides: %_name = %EVR

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: /usr/bin/appstreamcli /usr/bin/desktop-file-validate

%description
Icons for the COSMIC desktop environment.

%prep
%setup -n %_name-%version%beta

%install
just rootdir=%buildroot install

%files
%_iconsdir/Cosmic/
%doc README*

%changelog
* Sat Aug 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-8-gea9e3b8)


