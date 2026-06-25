%define _unpackaged_files_terminate_build 1
%global import_path gogs.io/gogs

Name: gogs
Version: 0.14.3
Release: alt1
Summary: Self Hosted Git Service written in Go
License: MIT
Group: System/Servers
Url: https://gogs.io
Vcs: https://github.com/gogs/gogs.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar
Source2: app.ini
Source3: gogs.service
Source4: gogs.sysusers.conf
Source5: service.d-ports
Source6: service.d-ssh

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-macros-systemd
BuildRequires: libpam0-devel

%description
Gogs is a painless self-hosted Git service written in Go. It provides a simple,
stable, and extensible platform for hosting Git repositories, supporting
SSH, HTTP, and HTTPS protocols, with features like user management, repository
webhooks, issues, pull requests, and wiki.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="pam cert"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
%golang_install

install -d %buildroot%_localstatedir/%name
install -d %buildroot%_logdir/%name
install -D %SOURCE3 %buildroot%_unitdir/%name.service
install -D %SOURCE5 %buildroot%_sysconfdir/systemd/system/%name.service.d/port.conf
install -D %SOURCE6 %buildroot%_sysconfdir/systemd/system/%name.service.d/ssh.conf
install -D %SOURCE2 %buildroot%_sysconfdir/%name/app.ini
install -D %SOURCE4 %buildroot%_sysusersdir/%name.conf

%pre
%sysusers_create_package %name %SOURCE4

%post
%systemd_post %name.service

%preun
%systemd_preun %name.service

%postun
%systemd_postun_with_restart %name.service

%files
%doc README.md LICENSE
%_bindir/%name
%dir %attr(0750,root,gogs) %_localstatedir/%name
%dir %attr(0750,root,gogs) %_logdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0660,root,gogs) %_sysconfdir/%name/app.ini
%dir %_sysconfdir/systemd/system/%name.service.d
%config(noreplace) %_sysconfdir/systemd/system/%name.service.d/port.conf
%config(noreplace) %_sysconfdir/systemd/system/%name.service.d/ssh.conf
%_unitdir/%name.service
%_sysusersdir/%name.conf

%changelog
* Wed Jun 24 2026 Aleksandr A. Voyt <sobue@altlinux.org> 0.14.3-alt1
- 0.13.3 -> 0.14.3

* Mon Aug 18 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.13.3-alt1
- Initial build.
