%define _unpackaged_files_terminate_build 1
%global import_path github.com/grafviktor/goto

Name: goto
Version: 1.6.0
Release: alt1
Summary: %name is console SSH client application
Group: Networking/Remote access
License: MIT
Url: https://github.com/grafviktor/goto

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: openssh
Conflicts: grip-grab

%description
This is a tool for managing and organizing your SSH servers.
Unlike PuTTY it doesn't include any connection logic, but integrates with ssh
utility which should be installed on your system. It's perfect for dev teams
allowing SSH configurations to be centrally stored on an internal server and
shared across developers or entire tech departments.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install
mkdir -p %buildroot_bindir
ln -s %buildroot_bindir/%name %buildroot%_bindir/gg

%files
%doc *.md
%_bindir/%name
%_bindir/gg

%changelog
* Thu Jun 04 2026 Pavel Shilov <zerospirit@altlinux.org> 1.6.0-alt1
- Update to new version 1.6.0.

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 1.5.1-alt2
- Add conflicts with grip-grab.

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 1.5.1-alt1
- Update to new version 1.5.1.

* Mon Dec 29 2025 Pavel Shilov <zerospirit@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus for close (ALT #57383).

