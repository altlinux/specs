%global _unpackaged_files_terminate_build 1

Name: acmed
Summary: An ACME (RFC 8555) client daemon
Version: 0.23.0
Release: alt2
License: MIT AND Apache-2.0
Group: Networking/WWW
Url: https://github.com/breard-r/acmed

Vcs: https://github.com/breard-r/acmed.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: /proc

%description
ACMEd is a daemon, which means it is designed to run in the background
and executes all the required actions all by itself.
Unlike some other ACME client, it therefore does not require any cron job
or any other kind of timer.

%prep
%setup

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%build
%make_build acmed tacd

%install
%makeinstall_std

# systemd units
install -D -p -m 0644 contrib/systemd/%name.service %buildroot%_unitdir/%name.service
# polkit rules for allow restart services for acmed user
install -D -p -m 0644 contrib/polkit/10-acmed.rules %buildroot%_datadir/polkit-1/rules.d/10-acmed.rules

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -N -g %name -c 'ACME client daemon' -s /sbin/nologin \
        -M -d %_sharedstatedir/%name %name 2>/dev/null ||:

%post
%post_systemd_postponed %name

%preun
%preun_systemd %name

%files
%attr(0750,root,%name) %dir %_sysconfdir/%name
%attr(0640,root,%name) %config(noreplace) %_sysconfdir/%name/*.toml
%_bindir/acmed
%_bindir/tacd
%_unitdir/%name.service
%_datadir/polkit-1/rules.d/10-acmed.rules
%_man5dir/*
%_man8dir/*
%attr(0755,%name,%name) %dir %_sharedstatedir/%name
%attr(0755,%name,%name) %dir %_sharedstatedir/%name/certs
%attr(0700,%name,%name) %dir %_sharedstatedir/%name/accounts

%changelog
* Fri Aug 23 2024 Alexey Shabalin <shaba@altlinux.org> 0.23.0-alt2
- fix rebuild, update rust modules.

* Fri May 31 2024 Alexey Shabalin <shaba@altlinux.org> 0.23.0-alt1
- 0.23.0.

* Mon Dec 25 2023 Alexey Shabalin <shaba@altlinux.org> 0.22.1-alt1
- 0.22.1.

* Sun Jun 04 2023 Alexey Shabalin <shaba@altlinux.org> 0.21.0-alt1
- Initial build.

