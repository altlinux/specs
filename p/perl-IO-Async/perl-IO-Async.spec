Name: perl-IO-Async
Version: 0.64
Release: alt1

Summary: Asynchronous event-driven programming
Group: Development/Perl
License: perl

Url: %CPAN IO-Async
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: /proc perl(IO/Socket/IP.pm) perl(Module/Build.pm) perl(Test/Refcount.pm) perl(Future.pm) perl(Test/Fatal.pm) perl(Future/Utils.pm) perl-devel perl(Test/Identity.pm) perl(Struct/Dumb.pm)

%add_findreq_skiplist */IO/Async/MergePoint.pm

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/IO/Async*
%doc Changes LICENSE README

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Sat Dec 14 2013 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt1
- initial build for ALTLinux

