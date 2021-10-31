%global import_path github.com/evanw/esbuild

%global _unpackaged_files_terminate_build 1

Name: esbuild
Version: 0.11.20
Release: alt1
Summary: An extremely fast JavaScript and CSS bundler and minifier
Group: Development/Other
License: MIT
Url: https://esbuild.github.io
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang
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

#%golang_prepare
#pushd $BUILDDIR/src/%import_path
#go install ./...
%make_build esbuild
#popd

%install
install -D -m 755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Sun Oct 31 2021 Alexey Shabalin <shaba@altlinux.org> 0.11.20-alt1
- Initial build.

