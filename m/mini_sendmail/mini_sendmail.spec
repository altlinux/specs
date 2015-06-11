Summary: accept email on behalf of real sendmail
Name: mini_sendmail
Version: 1.3.8
Release: alt1
License: BSD-like
Group: Networking/Mail
Url: http://www.acme.com/software/mini_sendmail/
Source0: %name-%version.tar

%description
mini_sendmail reads its standard input up to an end-of-file and sends
a copy of the message found there to all of the addresses listed. The
message is sent by connecting to a local SMTP server. This means
mini_sendmail can be used to send email from inside a chroot(2) area.

%prep
%setup
%build
%make_build CFLAGS="%optflags" LDFLAGS=""

%install
mkdir -p %buildroot%_sbindir %buildroot%_man8dir
make install BINDIR=%buildroot%_sbindir MANDIR=%buildroot%_mandir

%files
%_sbindir/%name
%_man8dir/%name.8.*
%doc README

%changelog
* Thu Jun 11 2015 Terechkov Evgenii <evg@altlinux.org> 1.3.8-alt1
- Initial build for ALT Linux Sisyphus
