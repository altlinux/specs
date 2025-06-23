%define import_path https://gitverse.ru/strongpass/manage-local-admin-password

Name:    manage-local-admin-password
Version: 1.0
Release: alt1.git02c8e73

Summary: Microsoft LAPS alternative for Windows and Linux using Hashicorp Vault/OpenBao/StarVault
License: Apache-2.0
Group:   Security/Networking
Url:     https://strongpass.ru/blog/manage-local-admin-password
Vcs:     https://gitverse.ru/strongpass/manage-local-admin-password.git

Source0:   %name-%version.tar
Source1:   vendor.tar

BuildRequires: golang
BuildRequires(pre): rpm-build-golang
BuildRequires: libselinux-utils
BuildRequires: libpcre2-devel
BuildRequires: glibc-devel-static


%description
Microsoft LAPS alternative for Windows and Linux using Hashicorp
Vault/OpenBao/StarVault. Allows you to automatically rotate passwords
for any local accounts.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
pushd linux
%golang_build .
%golang_prepare
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Mon Jun 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1.git02c8e73
- Initial build for Sisyphus (thanks Olesya Shuster).
