# Spec file for Perl module Proc::Simple

Name: perl-Proc-Simple
Version: 1.31
Release: alt1

Summary: Perl module Proc::Simple
Summary(ru_RU.UTF-8): модуль Perl Proc::Simple

%define real_name Proc-Simple

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Proc-Simple/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

%description
Perl module Proc::Simple provides objects mimicing real-life
processes from a user's point of view.

%description -l ru_RU.UTF-8
Модуль Perl Proc::Simple позволяет создавать объекты, имитирующие
процессы реального времени с точки зрения пользователя.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Proc/Simple*
%exclude /.perl.req

%changelog
* Sun Nov 25 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.31-alt1
- New version

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.27-alt1
- New version 1.27

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.26-alt1
- New version 1.26

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.23-alt1
- New version 1.23

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.22-alt1
- New version
  - Added patch by Chip Capelik to provide a wait()
    method waiting for a process to terminate.

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.21-alt1
- Initial build for ALT Linux Sisyphus

* Sun Jul 02 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.21-alt0
- First build

