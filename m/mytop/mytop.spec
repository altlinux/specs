Name: mytop
Version: 1.7
Release: alt1

Summary: A top clone for MySQL
Summary(ru_RU.UTF-8): Клон top для MySQL

License: GPL
Group: Databases
URL: http://jeremy.zawodny.com/mysql/mytop/

Source: http://jeremy.zawodny.com/mysql/mytop/%name-%version.tar

BuildArch: noarch

Patch: mytop-1.7-long.patch
Patch1: mytop-1.7-undef-resolv.patch

BuildRequires: perl-DBD-mysql perl-devel perl-podlators
Requires: perl-DBD-mysql perl-Term-ReadKey

%description
mytop is a console-based (non-gui) tool for monitoring the threads
and overall performance of MySQL servers.

%description -l ru_RU.UTF-8
%name --- консольная утилита для мониторинга процессов и общей
производительности сервера БД MySQL.

%prep
%setup
%patch -p1
%patch1 -p1

%build
perl Makefile.PL
%perl_vendor_build INSTALLMAN1DIR=%_man1dir INSTALLMAN3DIR=%_man3dir
make test

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install blib/script/%name %buildroot%_bindir
install -m644 blib/man1/%name.1 %buildroot%_man1dir

%files
%_bindir/%name
%_man1dir/%name.*
%doc README Changes

%changelog
* Sat Oct 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new build, cleanup spec, add fixes (thanks, Fedora!), (ALT bug #25783)

* Mon Dec 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.1
- Fixed build

* Sun Jan 13 2008 Denis Ovsienko <pilot@altlinux.ru> 1.6-alt1
- building current version

* Fri Feb 27 2004 Denis Ovsienko <pilot@altlinux.ru> 1.4-alt1
- first build for ALTLinux

