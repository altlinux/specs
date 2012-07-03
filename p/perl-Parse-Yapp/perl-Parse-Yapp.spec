%define module	Parse-Yapp

Name: perl-%module
Version: 1.05
Release: alt3.1.1

Summary: %module module for perl
License: distributable
Group: Development/Perl

Url: http://www.cpan.org
Source: http://cpan.valueclick.com/modules/by-module/Parse/%module-%version.tar.bz2

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators
BuildArch: noarch

%description
%module module for perl

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
cd $RPM_BUILD_ROOT%perl_vendor_privlib/Parse
find . -type f -name '*.pm'|xargs chmod 644

%files
%perl_vendor_privlib/Parse*
%_bindir/*
%_man1dir/*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.05-alt3.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.05-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Jan 12 2004 Stanislav Ievlev <inger@altlinux.org> 1.05-alt3
- added to package missed yapp utility (#3348)

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.05-alt2
- rebuild with new perl

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 1.05-alt1
- 1.05

* Thu Aug 09 2001 Stanislav Ievlev <inger@altlinux.ru> 1.04-alt1
- We need it for foomatic too.

* Mon Jun 18 2001 Till Kamppeter <till@mandrakesoft.com> 1.04-1mdk
- Updated to 1.04 (for Foomatic).

* Sun Jun 17 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.02-4mdk
- Rename spec file.
- Remove the Distribution and Vendor tag.
- Rebuild for the latest perl.

* Tue Mar 13 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 1.02-3mdk
- BuildArch: noarch

* Sat Sep 16 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.02-2mdk
- Call spec-helper before creating filelist

* Wed Aug 09 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.02-1mdk
- Macroize package
