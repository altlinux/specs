# Spec file for Perl module Proc::SyncExec

Name: perl-Proc-SyncExec
Version: 1.01
Release: alt1.1

Summary: Perl module Proc::SyncExec
Summary(ru_RU.UTF-8): модуль Perl Proc::SyncExec

%define real_name Proc-SyncExec

License: Artistic
Group: Development/Perl
URL: http://search.cpan.org/~rosch/Proc-SyncExec/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel

%description
Perl module Proc::SyncExec contains functions for synchronized 
process spawning with full error return. If the child's exec() 
call fails the reason for the failure  is reported back to the 
parent.

%description -l ru_RU.UTF-8
Модуль Perl Proc::SyncExec содержит функции для синхронизированного
запуска процессов  с возможностью  отслеживания возникающих ошибок.
Если в результате вызова exec()  в дочернем  процессе по каким-либо
причинам произойдёт ошибка, это будет сообщено обратно в родительс-
кий процесс.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Proc/SyncExec*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.01-alt1
- Initial build for ALT Linux Sisyphus

* Sun Jul 02 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.01-alt0
- First build

