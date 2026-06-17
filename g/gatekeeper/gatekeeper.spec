%define _unpackaged_files_terminate_build 1
%global import_path github.com/gogatekeeper/gatekeeper

Name: gatekeeper
Version: 4.10.0
Release: alt1

Summary: An OpenID / Proxy service
License: Apache-2.0
Group: System/Servers
Url: https://gogatekeeper.github.io/gatekeeper/
Vcs: https://github.com/gogatekeeper/gatekeeper.git

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: %name.sysconfig
Source3: %name.service

BuildRequires(pre): rpm-build-golang

%description
Gatekeeper is a proxy which integrates with Keycloak IDP Provider,
it supports both access tokens in a browser cookie or bearer tokens.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export LDFLAGS="-X %import_path/pkg/proxy/core.release=%version-%release -X %import_path/pkg/proxy/core.gitsha=altlinux-package -X %import_path/pkg/proxy/core.compiled=$(date +%%s)"
%golang_build cmd/keycloak

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install
install -d %buildroot%_datadir/gatekeeper
cp -a templates %buildroot%_datadir/gatekeeper/
mv %buildroot%_bindir/keycloak %buildroot%_bindir/gatekeeper

install -D -p -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -D -p -m 0640 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -d %buildroot%_localstatedir/%name
install -d %buildroot%_logdir/%name

%pre
%_sbindir/groupadd -r -f _%name ||:
%_sbindir/useradd -r -g _%name -d %_localstatedir/%name -s /dev/null -c "Gatekeeper proxy" _%name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name
%files
%doc README.md
%_bindir/gatekeeper
%_datadir/gatekeeper
%_unitdir/%name.service
%config(noreplace) %attr(640,root,_%name) %_sysconfdir/sysconfig/%name
%dir %attr(750,_%name,_%name) %_localstatedir/%name
%dir %attr(750,_%name,_%name) %_logdir/%name

%changelog
* Tue Jun 16 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.10.0-alt1
- New version (4.10.0).

* Tue May 12 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.9.0-alt1
- New version (4.9.0).

* Thu Apr 02 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 4.7.1-alt1
- Initial build for ALT.
