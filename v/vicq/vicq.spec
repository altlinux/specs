Name: vicq
Version: 0.4.1
Release: alt5.2

Summary: A clone of the Mirabilis ICQ online messaging program
Summary(ru_RU.UTF-8): Консольный вариант программы обмена сообщениями ICQ.
License: Public Domain
Group: Networking/Instant messaging
Url: http://www.gonzo.kiev.ua/projects/vicq
Packager: Andrey Astafiev <andrei@altlinux.ru>

Source: %url/%name-%version.tar.bz2
Patch1: %name-0.4.1-alt-no_SOCKS.patch

BuildArch: noarch
BuildPreReq: perl-Term-ReadLine-Gnu
BuildRequires: perl-Pod-Parser

%description
Vicq is a clone of the Mirabilis ICQ online messaging/conferencing
program.

%description -l ru_RU.UTF-8
Консольный вариант программы обмена сообщениями ICQ, использующий протокол ICQ2000.

%prep
%setup -q -n %name
%patch1 -p1

%build
pod2man %name > %name.1

%install
install -pD Net/vICQ/vICQ.pm %buildroot%perl_vendor_privlib/Net/vICQ.pm
install -pD %name %buildroot%_bindir/%name
install -pD %name.1 %buildroot%_man1dir/%name.1

%files
%doc README INSTALL TODO ChangeLog vicqrc*
%_man1dir/%name.*
%_bindir/%name
%perl_vendor_privlib/Net

%changelog
* Sat Nov 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.4.1-alt5.2
- rebuilt with perl 5.12
- fixed requires

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt5.1
- rebuild (with the help of girar-nmu utility)

* Thu Nov 20 2008 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt5
- fix building
- fix install on x86_64

* Mon Oct 06 2003 Andrey Astafiev <andrei@altlinux.ru> 0.4.1-alt3
- Now builds with hasher.

* Mon Dec 02 2002 Andrey Astafiev <andrei@altlinux.ru> 0.4.1-alt2
- Corrected dependencies.

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 0.4.1-alt1
- 0.4.1
- rebuilt in new environment.

* Tue Feb 12 2002 Andrey Astafiev <andrei@altlinux.ru> 0.4-alt1
- 0.4

