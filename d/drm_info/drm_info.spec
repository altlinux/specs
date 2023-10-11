%def_enable snapshot
%def_enable man

Name: drm_info
Version: 2.6.0
Release: alt1

Summary: Small utility to dump info about DRM devices
License: MIT
Group: System/Kernel and hardware
Url: https://gitlab.freedesktop.org/emersion/drm_info

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/emersion/drm_info/-/releases/v%version/downloads/%name-%version.tar.gz
%else
Vcs: https://gitlab.freedesktop.org/emersion/drm_info.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libdrm-devel pkgconfig(json-c) >= 0.14 libpci-devel
%{?_enable_man:BuildRequires: scdoc}

%description
%summary

%prep
%setup

%build
%meson \
%{?_disable_man:-Dman-pages=disabled}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_bindir/%name
%{?_enable_man:%_man1dir/*}
%doc README*

%changelog
* Wed Oct 11 2023 Yuri N. Sedunov <aris@altlinux.org> 2.6.0-alt1
- 2.6.0

* Mon May 29 2023 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- first build for Sisyphus (v2.5.0-3-gc18976c)



