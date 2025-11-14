%global import_path github.com/evanw/esbuild

%global _unpackaged_files_terminate_build 1

Name: esbuild
Version: 0.27.0
Release: alt1
Summary: An extremely fast JavaScript and CSS bundler and minifier
Group: Development/Other
License: MIT
Url: https://esbuild.github.io
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.23.12
BuildRequires: node

%description
%summary.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

#%%golang_prepare
#pushd $BUILDDIR/src/%%import_path
#go install ./...
%make_build esbuild
#popd

%install
install -D -m 755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Fri Nov 14 2025 Alexey Shabalin <shaba@altlinux.org> 0.27.0-alt1
- New version 0.27.0.

* Sat Nov 01 2025 Alexey Shabalin <shaba@altlinux.org> 0.25.11-alt1
- New version 0.25.11.

* Wed Aug 13 2025 Alexey Shabalin <shaba@altlinux.org> 0.25.9-alt1
- New version 0.25.9.

* Mon Dec 23 2024 Alexey Shabalin <shaba@altlinux.org> 0.24.2-alt1
- New version 0.24.2 (ALT#52497).

* Fri Apr 07 2023 Alexey Shabalin <shaba@altlinux.org> 0.14.54-alt1
- 0.14.54

* Mon Jun 13 2022 Alexey Shabalin <shaba@altlinux.org> 0.14.39-alt1
- 0.14.39

* Wed Mar 02 2022 Alexey Shabalin <shaba@altlinux.org> 0.14.13-alt1
- 0.14.13

* Sun Oct 31 2021 Alexey Shabalin <shaba@altlinux.org> 0.11.20-alt1
- Initial build.

