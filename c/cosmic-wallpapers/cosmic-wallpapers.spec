# git tarball doesn't contains images
# use git-lfs to fetch
%def_enable snapshot
%define _name cosmic-wallpapers
%define ver_major 1.0
%define beta .alpha.5.1

Name: %_name
Version: %ver_major.0
Release: alt0.52%beta

Summary: COSMIC Wallpapers
License: CC-BY-SA-4.0
Group: Graphical desktop/Other
Url: https://github.com/pop-os/cosmic-wallpapers

Vcs: https://github.com/pop-os/cosmic-wallpapers.git

BuildArch: noarch

%define git_ver epoch-%version%(echo %beta|sed 's/^\./-/')
%if_disabled snapshot
Source: %url/archive/%git_ver/%name-%version%beta.tar.gz
%else
Source: %_name-%version%beta.tar
%endif

%description
Wallpapers for the COSMIC desktop environment.

%prep
%setup -n %name-%{?_enable_snapshot:%version%beta}%{?_disable_snapshot:%git_ver}

%install
%makeinstall_std

%files
%_datadir/backgrounds/cosmic/
%doc README*

%changelog
* Thu Jan 16 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.52.alpha.5.1
- use git-lfs to actually download the wallpapers

* Wed Jan 15 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.51.alpha.5.1
- 1.0.0-alpha.5.1

* Fri Jan 10 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.5.alpha.5
- first build for Sisyphus


