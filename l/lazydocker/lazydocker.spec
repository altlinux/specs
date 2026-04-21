%define _unpackaged_files_terminate_build 1

%global import_path github.com/jesseduffield/lazydocker

Name:    lazydocker
Version: 0.25.2
Release: alt1

Summary: The lazier way to manage everything docker
License: MIT
Group:   Monitoring
Url:     https://github.com/jesseduffield/lazydocker

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
A simple terminal UI for both docker and docker-compose,
written in Go with the gocui library.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Tue Apr 21 2026 Nikita Shmatko <nash@altlinux.org> 0.25.2-alt1
- New version 0.25.2.

* Wed Jan 14 2026 Nikita Shmatko <nash@altlinux.org> 0.24.3-alt1
- New version 0.24.3.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 0.24.2-alt1
- Initial build for Sisyphus.
