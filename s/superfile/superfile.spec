%define _unpackaged_files_terminate_build 1
%global import_path github.com/yorukot/superfile
%global bin_name spf
%def_with check

Name: superfile
Version: 1.6.0
Release: alt2
Summary: Pretty fancy and modern terminal file manager
License: MIT
Group: File tools
URL: https://superfile.dev
VCS: https://github.com/yorukot/superfile

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-disabled-checking-upstream-version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

# https://bugzilla.altlinux.org/60049
Requires: fonts-ttf-fira-code-nerd

%if_with check
%ifnarch i586
BuildRequires: perl-Image-ExifTool
BuildRequires: zoxide
%endif
%endif

%description
superfile is crafted for developers who live in the terminal.
Built with Go and Bubble Tea, combining obsessively refined UI
with the raw speed and power of terminal tools.

%prep
%setup -a1
%patch -p1

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
%golang_prepare
cd "$BUILDDIR/src/$IMPORT_PATH"
%golang_build .

%install
install -Dm 0755 .gopath/bin/%name %buildroot%_bindir/%bin_name

%check
%ifnarch i586
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
cd "$BUILDDIR/src/$IMPORT_PATH"
%gotest ./...
%endif

%files
%_bindir/%bin_name
%doc README.md LICENSE

%changelog
* Thu Aug 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.0-alt2
- Added requires to nerd fonts (closes: #60049).

* Sat Jul 25 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.6.0-alt1
- Updated to version 1.6.0.
- Renamed binary to spf to match upstream.

* Thu Jun 06 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.1.3-alt2
- Disable comparison of release with upstream version.

* Thu Jun 06 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.1.3-alt1
- Updated to version 1.1.3.

* Tue May 14 2024 Anastasia Osmolovskaya <lola@altlinux.org> 1.1.2-alt1
- Initial build for ALT.
