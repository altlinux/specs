%define module Mail-IMAPClient

Name: perl-%module
Version: 3.31
Release: alt1

Summary: This module provides methods implementing the IMAP protocol
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/P/PL/PLOBBES/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 01 2012
BuildRequires: perl-Authen-SASL perl-IO-Compress perl-IO-Socket-SSL perl-NTLM perl-Parse-RecDescent perl-Test-Pod

%description
This module provides methods implementing the IMAP protocol. It allows perl
scripts to interact with IMAP message stores.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc examples
%perl_vendor_privlib/Mail/

%changelog
* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 3.31-alt1
- 3.31

* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 3.30-alt1
- 3.30

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.29-alt1
- automated CPAN update

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 3.28-alt1
- 3.28

* Fri Feb 11 2011 Victor Forsiuk <force@altlinux.org> 3.26-alt1
- 3.26

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.25-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jun 15 2010 Victor Forsiuk <force@altlinux.org> 3.25-alt1
- 3.25

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 3.23-alt1
- 3.23

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 3.21-alt1
- 3.21

* Mon Jul 13 2009 Victor Forsyuk <force@altlinux.org> 3.19-alt1
- 3.19

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 3.12-alt1
- 3.12
- Package examples.

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 3.10-alt1
- 3.10

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 3.08-alt1
- 3.08

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 3.05-alt1
- 3.05

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 3.02-alt1
- 3.02

* Tue Jul 03 2007 Victor Forsyuk <force@altlinux.org> 2.2.9-alt2
- Spec cleanups.
- Update build requirements.

* Tue Feb 22 2005 Vladimir Lettiev <crux@altlinux.ru> 2.2.9-alt1
- Initial release for ALTLinux Sisyphus
