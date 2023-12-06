Name: perl-Debug-Client
Version: 0.31
Release: alt3

Summary: debugger client side code for Padre, The Perl IDE.
Group: Development/Perl
License: perl

Url: %CPAN Debug-Client
Source: %name-%version.tar
Patch0: perl-Debug-Client-0.31-issue2.patch
Patch1: perl-Debug-Client-0.31-perl5.38-no-given-when.patch

BuildArch: noarch
BuildRequires: perl(PadWalker.pm) perl(Test/Requires.pm) perl(Test/CheckDeps.pm) perl(Test/Deep.pm) perl(parent.pm) perl(Test/Class.pm) perl(File/HomeDir.pm) perl-devel perl(IO/Socket/IP.pm) perl(Term/ReadLine/Gnu.pm)

%description
%summary

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# no upstream patch yet
# see https://github.com/PadreIDE/Debug-Client/issues/12
[ %version = 0.31 ] && rm -f t/11-add.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md README
%perl_vendor_privlib/Debug/Client*
%doc Changes README

%changelog
* Wed Dec 06 2023 Igor Vlasenko <viy@altlinux.org> 0.31-alt3
- fixed https://github.com/PadreIDE/Debug-Client/issues/13

* Sun Jun 27 2021 Igor Vlasenko <viy@altlinux.org> 0.31-alt2
- disabled test 11 for the sake of p10 (closes: #40292)
- known as https://github.com/PadreIDE/Debug-Client/issues/12

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
