Name: apg
Version: 2.2.3
Release: alt4

Summary: Automated password generator
License: BSD
Group: Text tools

Url: http://www.adel.nursat.kz/apg/
Source0: %url/download/%name-%version.tar.gz
Source1: %name.xinetd
Patch: %name-makefile.patch
Packager: Denis Ovsienko <pilot@altlinux.ru>

Summary(ru_RU.KOI8-R): Автоматический генератор паролей

%description
* Built-in ANSI X9.17 RNG (Random Number Generator)(CAST/SHA1)
* Built-in password strength checking system (support for Bloom filter
  for faster access)
* Two password generation algorithms:
  1. pronounceable password generation algorithm (NIST FIPS 181)
  2. random character password generation algorithm
     with 35 configurable modes of operation
* Configurable password length
* Configurable passwords amount
* Ability to initialize RNG with user string
* /dev/random support
* Ability to crypt() generated passwords and print crypted value
  as additional output
* Special parameters to call APG from shell scripts

%prep
%setup
%patch

%build
%make_build -e all

%install
INSTALL_PREFIX=%buildroot APG_BIN_DIR=%_bindir APG_MAN_DIR=%_man1dir APGD_BIN_DIR=%_sbindir \
	APGD_MAN_DIR=%_man8dir %make_install -e install
install -D %SOURCE1 %buildroot%_sysconfdir/xinetd.d/%{name}d

%files
%_bindir/%name
%_bindir/%{name}bfm
%_man1dir/*
%doc CHANGES INSTALL README THANKS TODO

%package daemon
Requires: %name xinetd service
# pwdgen entry
Requires: setup >= 2.2.3-alt1
Group: System/Servers
Summary: Automated password generator service
Summary(ru_RU.KOI8-R): Сервис автоматической генерации паролей

%description daemon
* Ability to log password generation requests for network version
* Password Generator Protocol (RFC972) support
* Ability to enforce remote users to use only allowed
  password generation method

%files daemon
%_sbindir/%{name}d
%_man8dir/*
%config(noreplace) %attr(0640,root,root) %_sysconfdir/xinetd.d/%{name}d

%pre daemon
[ "$1" -eq 1 ] && useradd -c "APG pseudouser" -r -d /dev/null -s /dev/null apgd

%post daemon
[ "$1" -eq 1 ] && service xinetd condreload

# TODO:
# - migrate to _apgd pseudouser?

%changelog
* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 2.2.3-alt4
- rebuilt
- dropped pseudouser removal upon package deletion
  (considered harmful)
- minor spec cleanup

* Thu May 20 2004 Denis Ovsienko <pilot@altlinux.ru> 2.2.3-alt3
- improved interaction with xinetd and useradd/userdel

* Fri Jan 23 2004 Denis Ovsienko <pilot@altlinux.ru> 2.2.3-alt2
- since pwdgen came into %_sysconfdir/services, xinetd entry changes from UNLISTED to a standard one
- useradd and macros fix

* Fri Nov 07 2003 Denis Ovsienko <pilot@altlinux.ru> 2.2.3-alt1
- new version with a minor fix

* Mon Sep 01 2003 Denis Ovsienko <pilot@altlinux.ru> 2.2.2-alt1.0
- Initial Sisyphus build

