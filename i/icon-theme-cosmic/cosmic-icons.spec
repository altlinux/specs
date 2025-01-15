%def_disable snapshot
%define _name cosmic-icons
%define ver_major 1.0
%define beta .alpha.5.1

%def_disable check

Name: icon-theme-cosmic
Version: %ver_major.0
Release: alt0.51%beta

Summary: COSMIC Icons
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-icons

Vcs: https://github.com/pop-os/cosmic-icons.git

BuildArch: noarch

Provides: %_name = %EVR

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

BuildRequires(pre): rpm-build-rust
BuildRequires: just
BuildRequires: /usr/bin/appstreamcli /usr/bin/desktop-file-validate

%description
Icons for the COSMIC desktop environment.

%prep
%setup -n %_name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver}

%install
just rootdir=%buildroot install

%files
%_iconsdir/Cosmic/
%doc README*

%changelog
* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- 1.0.0-alpha.5

* Sat Dec 07 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.4.alpha.4
- 1.0.0-alpha.4

* Thu Sep 26 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2.alpha.2
- 1.0.0-alpha.2

* Sat Aug 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1.alpha.1
- first build for Sisyphus (epoch-1.0.0-alpha.1-8-gea9e3b8)


