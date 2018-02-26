%define dist IO-All
Name: perl-%dist
Version: 0.44
Release: alt1

Summary: IO::All of it to Graham and Damian!
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# This dependency is in eval block
Requires: perl-Tie-File

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Encode-TW perl-File-ReadBackwards perl-IO-String perl-MLDBM perl-Pod-Escapes perl-Tie-File perl-devel

%description
IO::All combines all of the best Perl IO modules into a single nifty
object oriented interface to greatly simplify your everyday Perl IO
idioms. It exports a single function called io, which returns a new
IO::All object.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IO

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.36 -> 0.44

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.36-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.36-alt2
- fix directory ownership violation

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.36-alt1
- new version, return from orphaned

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
