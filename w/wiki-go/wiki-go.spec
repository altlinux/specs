%global _unpackaged_files_terminate_build 1
%global import_path github.com/leomoon-studios/wiki-go

Name: wiki-go
Version: 1.8.10
Release: alt1
Summary: A modern, feature-rich, databaseless flat-file wiki platform built with Go
License: GPL-3.0
Group: System/Servers
Url: https://wikigo.leomoon.com
VCS: https://github.com/leomoon-studios/wiki-go

Source: %name-%version.tar
Source1: wiki-go.service

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
LeoMoon Wiki-Go is a modern, feature-rich, databaseless flat-file
wiki platform built with Go. It provides a clean, intuitive
interface for creating and managing knowledge bases, documentation
and collaborative content without requiring any external database.
No database. No bloat. Zero maintenance. Just Markdown.

%prep
%setup

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor

go build -ldflags="-X wiki-go/internal/version.Version=%version" -o wiki-go .

%install
mkdir -p %buildroot%_bindir \
    %buildroot%_unitdir \
    %buildroot%_sysconfdir/wiki-go \
    %buildroot%_localstatedir/wiki-go
install -m 0755 wiki-go %buildroot%_bindir
install -m 0644 %SOURCE1 %buildroot%_unitdir
touch %buildroot%_sysconfdir/wiki-go/config.yaml

%pre
%_sbindir/groupadd -r -f wiki-go
%_sbindir/useradd -r -g wiki-go -s /sbin/nologin \
    -d %_localstatedir/wiki-go wiki-go 2>/dev/null ||:

%post
%post_service wiki-go

%preun
%preun_service wiki-go

%files
%_bindir/wiki-go
%_unitdir/wiki-go.service
%dir %attr(750, wiki-go, wiki-go) %_sysconfdir/wiki-go
%dir %attr(750, wiki-go, wiki-go) %_localstatedir/wiki-go
%ghost %config(noreplace) %_sysconfdir/wiki-go/config.yaml
%doc LICENSE README.md SECURITY.md

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.10-alt1
- Updated to version 1.8.10.

* Wed Mar 11 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.6-alt1
- Updated to version 1.8.6.

* Sat Feb 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.5-alt1
- Updated to version 1.8.5.

* Mon Nov 10 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.5-alt1
- Updated to version 1.7.5.

* Sat May 17 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.4.5-alt1
- Initial build for ALT.
