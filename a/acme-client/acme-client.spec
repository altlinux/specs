Name: acme-client
Version: 0.1.16
Release: alt1

Summary: secure ACME client

Group: Networking/Other
License: ISC License
Url: https://kristaps.bsd.lv/acme-client/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/kristapsdz/acme-client-portable.git
Source: %name-%version.tar

BuildRequires: libtls-devel libbsd-devel

%add_optflags -DHAVE_CONFIG_H -DDEFAULT_CA_FILE=\"/etc/pki/tls/certs/ca-bundle.crt\"
#-D_GNU_SOURCE -DNOBODY_USER="nobody"

%description
Be up-front about security: OpenSSL is known to have issues,
you can't trust what comes down the pipe, and your private key's integrity
is a hard requirement. Not a situation where you can be careless.
acme-client is a client for Let's Encrypt users, but one designed for security.
No Python. No Ruby. No Bash.
A straightforward, open source implementation in C that isolates each step of the sequence.

TODO: build lib libseccomp.

%prep
%setup

%build
%make_build 'CFLAGS=%optflags'

%install
%makeinstall_std PREFIX=%_prefix MAN1DIR=%_man1dir

%files
%doc README.md
%_bindir/%name
%_man1dir/%name.*

%changelog
* Sat Aug 05 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.16-alt1
- initial build for ALT Sisyphus
