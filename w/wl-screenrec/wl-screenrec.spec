%def_disable snapshot
%define ver_major 0.1

%def_disable bootstrap
# wayland display required
%def_disable check

Name: wl-screenrec
Version: %ver_major.2
Release: alt1

Summary: High performance screen recorder for wlroots Wayland
License: Apache-2.0
Group: Video
Url: https://github.com/russelltg/wl-screenrec

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/russelltg/wl-screenrec.git
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

%ifnarch %ix86 armh
Requires: slurp
%endif

BuildRequires(pre): rpm-build-rust
BuildRequires: clang-devel
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libswscale)
BuildRequires: pkgconfig(libswresample)

%description
%summary

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name
%doc README*

%changelog
* Mon Dec 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- 0.1.2

* Sat Nov 25 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.1-alt1
- first build for Sisyphus (v0.1.1-5-g82622bb)


