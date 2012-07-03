%define dist Inline
Name: perl-%dist
Version: 0.48
Release: alt1

Summary: Write Perl subroutines in other programming languages
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch
Requires: gcc >= 4.1

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Inline-Files perl-Parse-RecDescent perl-Test-Warn

%description
Inline lets you write Perl subroutines in other programming languages
like C, C++, Java, Python, Tcl and even Assembly. You don't need to
compile anything. All the details are handled transparently so you
can just run your Perl script like normal.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
	%perl_vendor_privlib/Inline.pm
%doc	%perl_vendor_privlib/Inline*.pod

%dir	%perl_vendor_privlib/Inline
	%perl_vendor_privlib/Inline/*.pm
%doc	%perl_vendor_privlib/Inline/*.pod

%dir	%perl_vendor_privlib/Inline/C
	%perl_vendor_privlib/Inline/C/*.pm

%dir	%perl_vendor_privlib/auto/Inline
	%perl_vendor_privlib/auto/Inline/*

%changelog
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
