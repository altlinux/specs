%global import_path github.com/bcicen/ctop

Name: ctop
Version: 0.7.7
Release: alt1

Summary: Top-like interface for container metrics
License: MIT
Group: Other
Url: https://%import_path

Packager: Stepan Paksashvili <paksa@altlinux.org>

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: golang

%description
Top-like interface for container metrics

ctop provides a concise and condensed overview of real-time metrics for multiple
containers as well as a single container view for inspecting a specific
container.

ctop comes with built-in support for Docker and runC;
connectors for other container and cluster systems are planned for future
releases.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-tags=release -mod=vendor"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -X main.version=${version}"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCE=1
mkdir -p %buildroot{%_bindir}

%golang_install

rm -rf %buildroot%go_root

%files
%doc LICENSE README.md _docs VERSION
%_bindir/ctop

%changelog
* Mon Mar 20 2023 Stepan Paksashvili <paksa@altlinux.org> 0.7.7-alt1
- Initial build for ALT
