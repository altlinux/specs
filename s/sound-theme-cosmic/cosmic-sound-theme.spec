%def_enable snapshot
%define _name cosmic-sound-theme
%define ver_major 1.4
%define beta %nil

%def_enable check

Name: sound-theme-cosmic
Version: %ver_major.0
Release: alt1%beta

Summary: COSMIC Sound Theme
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-sound-theme

Vcs: https://github.com/pop-os/cosmic-sound-theme.git

BuildArch: noarch

Provides: %_name = %EVR

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%_name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
%summary

%prep
%setup -n %_name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver}

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_datadir/sounds/COSMIC/
%doc README*

%changelog
* Thu Jul 23 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus


