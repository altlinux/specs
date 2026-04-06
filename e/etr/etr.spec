%def_disable snapshot

%define _name etr
# conflicts with extreme-tuxracer
%define binary_name %_name
%define ver_major 1.2
%define import_path github.com/tkjaer/%_name

%def_disable bootstrap

Name: %_name
Version: %ver_major.5
Release: alt1

Summary: ECMP-aware traceroute
License: MIT
Group: Networking/Other
Url: https://github.com/tkjaer/etr

Vcs: https://github.com/tkjaer/etr.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
%{?_disable_bootstrap:Source1: %_name-%version-vendor.tar}

ExcludeArch: %ix86
Conflicts: extreme-tuxracer

BuildRequires(pre): rpm-build-golang
BuildRequires: golang libpcap-devel

%description
An MTR-like tool for discovering and analyzing ECMP (Equal-Cost
Multi-Path) network routes.

%prep
%setup -n %_name-%version %{?_disable_bootstrap: -a1}
%{?_enable_bootstrap:go mod vendor
tar -cf %_sourcedir/%_name-%version-vendor.tar vendor/}

%build
export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export IMPORT_PATH="%import_path"
export GOFLAGS="${GOFLAGS-} -buildvcs=false"
export VERSION=%version

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%binary_name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/%binary_name
%doc *.md docs/probe-encoding-design.md

%changelog
* Mon Apr 06 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5

* Mon Mar 23 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Thu Mar 19 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Mon Mar 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Feb 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Feb 08 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Feb 01 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- first build for Sisyphus



