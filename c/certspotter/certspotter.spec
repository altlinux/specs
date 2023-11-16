# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: certspotter
Version: 0.18.0
Release: alt1
Summary: Certificate Transparency Log Monitor
License: MPL-2.0
Group: Security/Networking
Url: https://github.com/SSLMate/certspotter
Requires: /usr/sbin/sendmail

Source: %name-%version.tar
BuildRequires: golang
BuildRequires: lowdown

%description
Cert Spotter is a Certificate Transparency log monitor from SSLMate
that alerts you when an SSL/TLS certificate is issued for one of your
domains. Cert Spotter is easier to use than other open source CT monitors,
since it does not require a database. It's also more robust, since it
uses a special certificate parser that ensures it won't miss certificates.

%prep
%setup

%build
go build -v -o . -buildmode=pie -ldflags="-X main.Version=%version" ./...
%make_build -C man

%install
install -Dp certspotter -t %buildroot%_bindir
install -Dpm644 .gear/%name.service -t %buildroot%_unitdir
install -Dpm644 .gear/watchlist -t %buildroot%_sysconfdir/%name
install -Dpm644 .gear/README.hooks %buildroot%_sysconfdir/%name/hooks.d/README
install -Dpm644 .gear/sysusers %buildroot%_sysusersdir/%name.conf
install -d %buildroot%_cachedir/%name
install -Dpm644 man/certspotter*.8 -t %buildroot%_man8dir

%check
./certspotter --version | grep -Fw '%version'
go test -v

%files
%define _customdocdir %_docdir/%name
%doc README.md LICENSE CHANGELOG.md
%_bindir/certspotter
%_sysconfdir/certspotter
%_unitdir/certspotter.service
%_sysusersdir/certspotter.conf
%_man8dir/certspotter*.8*
%_cachedir/certspotter

%changelog
* Thu Nov 16 2023 Vitaly Chikunov <vt@altlinux.org> 0.18.0-alt1
- Update to v0.18.0 (2023-11-13).

* Sat Oct 21 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.0-alt1
- First import v0.16.0-9-g6ae7ae1 (2023-09-01).
