%define _unpackaged_files_terminate_build 1
%define dist Inline
Name: perl-%dist
Version: 0.86
Release: alt1

Summary: Write Perl subroutines in other programming languages
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/I/IN/INGY/%{dist}-%{version}.tar.gz

BuildArch: noarch
Requires: gcc >= 4.1
Requires: perl(Parse/RecDescent.pm)

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Inline-Files perl-Parse-RecDescent perl-Test-Warn perl(Encode.pm) perl(JSON/PP.pm)

%description
Inline lets you write Perl subroutines in other programming languages
like C, C++, Java, Python, Tcl and even Assembly. You don't need to
compile anything. All the details are handled transparently so you
can just run your Perl script like normal.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

rm -f %buildroot%perl_vendor_privlib/Inline/MakeMaker/Changes

%files
%doc	Changes README CONTRIBUTING example
	%perl_vendor_privlib/Inline.pm
%doc	%perl_vendor_privlib/Inline*.pod

%dir	%perl_vendor_privlib/Inline
	%perl_vendor_privlib/Inline/*.pm
%doc	%perl_vendor_privlib/Inline/*.pod

%changelog
* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- automated CPAN update

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.83-alt1
- automated CPAN update

* Sun Mar 31 2019 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- automated CPAN update

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- automated CPAN update

* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.80-alt2
- fixed unpackaged files

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.76-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt2
- added Requires: perl(Parse/RecDescent.pm)

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.48-alt1
- 0.46 -> 0.48

* Sun Dec 26 2010 Alexey Tourbin <at@altlinux.ru> 0.46-alt1
- 0.45 -> 0.46

* Tue Jul 28 2009 Alexey Tourbin <at@altlinux.ru> 0.45-alt1
- 0.44 -> 0.45

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.44-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon May 17 2004 Alexey Tourbin <at@altlinux.ru> 0.44-alt2
- revamped specfile (fixed URL etc.)
- mdk-underscore-localization.patch: fixes the use of $_ in Inline::denter
- alt-our-vars.patch: made Inline::C::ParseRegExp work with perl-5.8.4
- Requires: gcc > 3 (because of Inline::C)

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 0.44-alt1
- 0.44

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 0.43-alt2
- Rebuilt with perl-5.8.

* Mon Sep 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.43-alt1
- Initial revision.
