%define module		IPC-Signal
%define m_distro	IPC-Signal
%define m_name		IPC::Signal
%define m_author_id	ROSCH
Name: perl-%module
Version: 1.00
Release: alt3.1.1

Summary: Utility functions dealing with signals
Summary(ru_RU.CP1251): Функции для работы с сигналами
Group: Development/Perl
License: Artistic

Url: http://search.cpan.org/dist/%module/
Source: %module-%version.tar.bz2
Buildarch: noarch

# Automatically added by buildreq on Wed Jul 16 2003
BuildRequires: perl-devel

%description
This module contains utility functions for dealing with signals.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/IPC
%doc README Changes

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.00-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt3
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt2
- Minor specfile fixes.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt1
- First build for ALTLinux.


