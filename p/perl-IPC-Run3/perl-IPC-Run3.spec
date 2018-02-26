## SPEC file for Perl module IPC::Run3
## Used in SVK

Name: perl-IPC-Run3
Version: 0.044
Release: alt1

Summary: run a subprocess in batch mode (a la system) on Unix, Win32, etc.
Summary(ru_RU.UTF-8): позволяет запускать процессы в пакетном режиме (подобно system) в Unix, Win32 и др.

License: BSD, Artistic, or GPL
Group: Development/Perl

%define real_name IPC-Run3
URL: http://search.cpan.org/dist/IPC-Run3/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel

# Automatically added by buildreq on Tue Jun 21 2011
# optimized out: perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
IPC::Run3  Perl module allows you to run a subprocess and
redirect stdin, stdout,  and/or stderr  to files and perl
data structures. It aims to satisfy 99%%  of the need for
using  system() / qx`` / open3() with a simple, extremely
Perlish  API  and  none  of  the  bloat  and rarely  used
features of IPC::Run.

%description -l ru_RU.UTF-8
Модуль Perl  IPC::Run3 позволяет выполнять подпроцессы и
перенаправлять  stdin, stdout  и/или stderr  в файлы или
структуры данных Perl. Его целью является удовлетворение
на 99%%  необходимости  обращений к  вызовам  system() /
qx`` / open3() путём  замены их  простым и  написанным в
стиле Perl  API,  без  использования  наполненного редко
используемыми возможностями IPC::Run.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%exclude /.perl.req
%perl_vendor_privlib/IPC/Run3*

%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.044-alt1
- New version 0.044

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.043-alt1
- New version 0.043

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.042-alt1
- New version 0.042

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.040-alt1
- New version 0.040

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.037-alt1
- New version 0.037

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.035-alt1
- New version 0.035

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.034-alt1
- Initial build for ALT Linux

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.034-alt0
- New version 0.034

* Tue May 24 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.01-alt0.1
- Build for new perl-5.8.7

* Sat Mar 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.01-alt0
- Initial build
