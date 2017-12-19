Name: perl-Debug-Client
Version: 0.31
Release: alt1

Summary: debugger client side code for Padre, The Perl IDE.
Group: Development/Perl
License: perl

Url: %CPAN Debug-Client
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: perl(PadWalker.pm) perl(Test/Requires.pm) perl(Test/CheckDeps.pm) perl(Test/Deep.pm) perl(parent.pm) perl(Test/Class.pm) perl(File/HomeDir.pm) perl-devel perl(IO/Socket/IP.pm) perl(Term/ReadLine/Gnu.pm)

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md README
%perl_vendor_privlib/Debug/Client*
%doc Changes README

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Mon Feb 01 2016 Vladimir Lettiev <crux@altlinux.ru> 0.29-alt2
- Applied patch https://github.com/PadreIDE/Debug-Client/issues/2

* Mon Sep 16 2013 Vladimir Lettiev <crux@altlinux.ru> 0.29-alt1
- New version 0.29

* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.20-alt1
- New version 0.20

* Tue Dec 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt1
- New version 0.16

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
