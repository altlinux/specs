%define module		Proc-WaitStat
%define m_distro	Proc-WaitStat
%define m_name		Proc::WaitStat
%define m_author_id	ROSCH

Name: perl-%module
Version: 1.00
Release: alt4.1.1

Summary: Interpret and act on wait() status values
Group: Development/Perl
License: Artistic

Url: http://search.cpan.org/dist/%module/
Source: %m_distro-%version.tar.bz2
Buildarch: noarch

Requires: perl-IPC-Signal

# Automatically added by buildreq on Wed Jul 16 2003
BuildRequires: perl-IPC-Signal perl-devel

%description
This module contains functions for interpreting and acting on wait status
values.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Proc
%doc README Changes

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.00-alt4.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.00-alt4.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt4
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt3
- Added `Changes' file to docs.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt2
- Minor specfile fixes.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.00-alt1
- First build for ALTLinux.

