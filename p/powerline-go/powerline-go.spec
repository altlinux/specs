%global import_path https://github.com/justjanne/powerline-go
%global commit c9f514f4d67478f055bd07db4ef30a08a19740cf

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %go_root %_bindir
%brp_strip_none %_bindir/*

Name: powerline-go
Version: 1.15.0
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

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Sun Dec 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.15.0-alt1
- 1.15.0

* Sun Nov 10 2019 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- Initial build for ALT


