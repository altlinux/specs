%define _unpackaged_files_terminate_build 1
%define dist podlators
Name: perl-%dist
Version: 4.10
Release: alt1

Summary: Convert POD data to various other formats
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RR/RRA/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012 (-bi)
BuildRequires: perl-Pod-Parser perl-Term-ANSIColor perl-Term-Cap perl-Test-Pod

%description
This package contains the replacement for pod2text and Pod::Text in
versions of Perl 5.005 and earlier.  It also contains Pod::Man and
pod2man, the replacement for pod2man found in Perl distributions prior
to 5.6.0.  The modules contained in it use Pod::Simple rather than doing
the POD parsing themselves, and are designed to be object-oriented and
to subclass.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README README.md docs
%_bindir/pod2man
%_bindir/pod2text
%_man1dir/perlpodstyle.*
%_man1dir/pod2man.*
%_man1dir/pod2text.*
%perl_vendor_privlib/Pod*

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 4.10-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.09-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 4.08-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 4.07-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.06-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 4.03-alt1
- automated CPAN update

* Mon Nov 02 2015 Vladimir Lettiev <crux@altlinux.ru> 2.5.3-alt2
- added man pages

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.2-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 2.4.2-alt1
- 2.4.0 -> 2.4.2

* Thu Dec 23 2010 Alexey Tourbin <at@altlinux.ru> 2.4.0-alt1
- 2.3.1 -> 2.4.0

* Mon Nov 15 2010 Vladimir Lettiev <crux@altlinux.ru> 2.3.1-alt2
- unbootsrap: added build dependency on perl-Pod-Parser

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.3.1-alt1
- initial revision, for perl-5.12
- disabled dependency on Pod::Usage, for bootstrap
