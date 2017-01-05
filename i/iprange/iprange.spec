Name: iprange
Version: 1.0.3
Release: alt1

Url: http://firehol.org
License: GPLv2+
Group: Networking/Other

Summary: Manage IP ranges utility

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/firehol/iprange/archive/v%version.tar.gz
Source: %name-%version.tar

%description
iprange - manage IP ranges.

%prep
%setup
# hack against gitignored iprange.spec.in
%__subst "s|.*iprange.spec||" ./configure.ac Makefile.am

%build
%autoreconf
%configure --disable-man
%make_build

%install
%makeinstall_std

%files
%_bindir/%name

%changelog
* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Fri Aug 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux Sisyphus
