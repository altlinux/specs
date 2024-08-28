%def_enable snapshot

%define _name SpoofDPI
# binary renamed in 0.11.0
%define binary_name spoofdpi
%define old_binary_name spoof-dpi
%define ver_major 0.11
%define import_path github.com/xvzc/%_name

%def_disable bootstrap

Name: %old_binary_name
Version: %ver_major.0
Release: alt1

Summary: A simple and fast software designed to bypass Deep Packet Inspection
License: Apache-2.0
Group: Networking/Other
Url: https://github.com/xvzc/SpoofDPI

Vcs: https://github.com/xvzc/SpoofDPI.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
%{?_disable_bootstrap:Source1: %_name-%version-vendor.tar}

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%{summary}.

%prep
%setup -n %_name-%version %{?_disable_bootstrap: -a1}
%{?_enable_bootstrap:go mod vendor
tar -cf %_sourcedir/%_name-%version-vendor.tar vendor/}

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
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
%doc *.md

%changelog
* Wed Aug 28 2024 Yuri N. Sedunov <aris@altlinux.org> 0.11.0-alt1
- 0.11.0

* Sun Aug 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.11-alt1
- 0.10.11

* Thu Aug 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.10-alt1
- updated to v0.10.10-2-gd97d4e4

* Fri Aug 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.8-alt1
- 0.10.8

* Tue Aug 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.6-alt1
- first build for Sisyphus



