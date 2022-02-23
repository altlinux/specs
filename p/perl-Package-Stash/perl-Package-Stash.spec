%define _unpackaged_files_terminate_build 1
%define dist Package-Stash
Name: perl-%dist
Version: 0.40
Release: alt1

Summary: Routines for manipulating stashes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# always loaded when available
Requires: perl-Package-Stash-XS

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Dist-CheckConflicts perl-Package-DeprecationManager perl-Package-Stash-XS perl-Test-Fatal perl-Test-Requires perl(Module/Implementation.pm) perl(CPAN/Meta/Check.pm) perl(Test/Needs.pm)

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that behind
a simple API.

%prep
%setup -q -n %{dist}-%{version}

%ifdef __buildreqs
# avoid built dependencies due to conflicts checking
sed -i- '/^check_conflicts/s/^/#/' Makefile.PL
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README CONTRIBUTING
%_bindir/package-stash-conflicts
%perl_vendor_privlib/Package

%changelog
* Wed Feb 23 2022 Igor Vlasenko <viy@altlinux.org> 0.40-alt1
- automated CPAN update

* Mon Nov 23 2020 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Mon Dec 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.33-alt1
- 0.32 -> 0.33
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.32-alt2
- added depdendency on perl-Package-Stash-XS

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.05 -> 0.13

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision, for Class::MOP
