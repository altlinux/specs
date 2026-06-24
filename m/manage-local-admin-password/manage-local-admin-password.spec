%define import_path https://gitverse.ru/strongpass/manage-local-admin-password
%define oname password-auto-rotate
%filter_from_requires /\/usr\/local\/bin\/password-auto-rotate/d

Name:    manage-local-admin-password
Version: 1.1.1
Release: alt1

Summary: Microsoft LAPS alternative for Windows and Linux using Hashicorp Vault/OpenBao/StarVault
License: Apache-2.0
Group:   Security/Networking
Url:     https://strongpass.ru/blog/manage-local-admin-password
Vcs:     https://gitverse.ru/strongpass/manage-local-admin-password.git

Source0:   %name-%version.tar
Source1:   vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang /proc
BuildRequires: libselinux-utils
BuildRequires: libpcre2-devel
BuildRequires: glibc-devel-static


%description
Microsoft LAPS alternative for Windows and Linux using Hashicorp
Vault/OpenBao/StarVault. Allows you to automatically rotate passwords
for any local accounts.

%prep
%setup -q -a1

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
install -D -m0644 linux/assets/%oname.service \
%buildroot%_unitdir/%oname.service
install -D -m0644 linux/assets/%oname.timer \
%buildroot%_unitdir/%oname.timer
install -D -m0644 linux/assets/%oname.env \
%buildroot%_sysconfdir/%oname.env

%post
%systemd_post %oname

%preun
%systemd_preun %oname

%postun
%systemd_postun %oname

%files
%doc README.md
%_bindir/%oname
%_unitdir/%oname.service
%_unitdir/%oname.timer
%config(noreplace) %_sysconfdir/%oname.env

%changelog
* Mon May 18 2026 Olesya Shuster <lesyafox@altlinux.org> 1.1.1-alt1
- New version 1.1.1.

* Fri Oct 17 2025 Alexander Danilov <admsasha@altlinux.org> 1.1-alt1
- New version to 1.1.

* Tue Jul 15 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.0-alt2.git02c8e73
- {post,preun,postun}_service:added support of service systemd units and
  for *.service and *.timer file (closes: #54989).

* Mon Jun 23 2025 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1.git02c8e73
- Initial build for Sisyphus (thanks Olesya Shuster).
