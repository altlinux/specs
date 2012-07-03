%define dist Package-Stash
Name: perl-%dist
Version: 0.32
Release: alt2

Summary: Routines for manipulating stashes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# always loaded when available
Requires: perl-Package-Stash-XS

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Dist-CheckConflicts perl-Package-DeprecationManager perl-Package-Stash-XS perl-Test-Fatal perl-Test-Requires

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that behind
a simple API.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
# avoid built dependencies due to conflicts checking
sed -i- '/^check_conflicts/s/^/#/' Makefile.PL
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/package-stash-conflicts
%perl_vendor_privlib/Package

%changelog
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
