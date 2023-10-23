%global _unpackaged_files_terminate_build 1
%global import_path github.com/justjanne/powerline-go

Name: powerline-go
Version: 1.24
Release: alt1
Summary: A beautiful and useful low-latency prompt for your shell, written in go

License: GPLv3
Group: Shells
Url: https://github.com/justjanne/powerline-go
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
A Powerline like prompt for Bash, ZSH and Fish.

 - Shows some important details about the git/hg branch
 - Changes color if the last command exited with a failure code
 - If you're too deep into a directory tree, shortens the displayed
   path with an ellipsis
 - Shows the current Python virtualenv environment
 - It's easy to customize and extend.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Mon Oct 23 2023 Alexey Shabalin <shaba@altlinux.org> 1.24-alt1
- New version 1.24.

* Wed May 18 2022 Alexey Shabalin <shaba@altlinux.org> 1.22.1-alt1
- new version 1.22.1

* Sun Feb 21 2021 Alexey Shabalin <shaba@altlinux.org> 1.21.0-alt1
- new version 1.21.0

* Sat Jan 16 2021 Alexey Shabalin <shaba@altlinux.org> 1.20.0-alt1
- new version 1.20.0

* Tue Oct 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.18.0-alt1
- new version 1.18.0

* Thu Jun 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.17.0-alt1
- 1.17.0

* Sun Dec 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- 1.15.0

* Sun Nov 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- Initial build for ALT


