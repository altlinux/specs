%def_enable Werror

Name: acme-client
Version: 0.1.16+obsd7.2
Release: alt1

Summary: secure ACME client

Group: Networking/Other
License: ISC
Url: https://git.altlinux.org/g/gears/a/acme-client.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libtls-devel libbsd-devel

%description
Be up-front about security: OpenSSL is known to have issues,
you can't trust what comes down the pipe, and your private key's integrity
is a hard requirement. Not a situation where you can be careless.
acme-client is a client for Let's Encrypt users, but one designed for security.
No Python. No Ruby. No Bash.
A straightforward, open source implementation in C that isolates each step of the sequence.

%prep
%setup
%patch -p1

%build
%add_optflags -DDEFAULT_CA_FILE=\"/etc/pki/tls/certs/ca-bundle.crt\"
%add_optflags -DLIBBSD_OPENBSD_VIS
%add_optflags -Wno-pointer-sign
%make_build 'CFLAGS=%optflags'

%install
%makeinstall_std \
	PREFIX=%_prefix \
	MAN1DIR=%_man1dir \
	MAN5DIR=%_man5dir \
	#

%files
%_bindir/acme-client
%_man1dir/acme-client.1*
%_man5dir/acme-client.conf.5*

%changelog
* Wed Feb 01 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1.16+obsd7.2-alt1
- Synced with 2022-12-28 OpenBSD snapshot.
- Enabled Werror.
- Fixed license: use short SPDX idendifier.

* Thu Jun 07 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1.16-alt1.2
- NMU: rebuilt against libtls17

* Mon Nov 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1.16-alt1.1
- rebuilt against new libtls

* Sat Aug 05 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.16-alt1
- initial build for ALT Sisyphus
