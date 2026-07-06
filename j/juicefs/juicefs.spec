%global import_path github.com/juicedata/juicefs

Name: juicefs
Version: 1.4.0
Release: alt1

Summary: Distributed POSIX file system built on top of Redis and S3
License: Apache-2.0
Group: System/Servers 
Url: https://www.juicefs.com/
Vcs: https://github.com/juicedata/juicefs.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

ExcludeArch: %ix86

%description
%summary.

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
ln -s juicefs %buildroot%_bindir/mount.juicefs

%files
%doc README.md
%_bindir/*

%changelog
* Mon Jul 06 2026 Andrew A. Vasilyev <andy@altlinux.org> 1.4.0-alt1
- v1.4.0

* Wed Apr 29 2026 Andrew A. Vasilyev <andy@altlinux.org> 1.4.0-alt0.beta1
- v1.4.0-beta1

* Tue Dec 02 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.3.1-alt1
- v1.3.1

* Tue Jul 08 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.3.0-alt1
- v1.3.0

* Mon Mar 10 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.2.3-alt1
- Initial build for ALT.

