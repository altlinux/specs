# network is disabled :(
%def_disable test
%define module Mail-DKIM

Name: perl-%module
Version: 0.39
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Perl module for DKIM-based mail-signing and -verifying
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/J/JA/JASLONG/Mail-DKIM-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: perl-Crypt-OpenSSL-RSA perl-MailTools perl-Net-DNS perl-devel

%description
This module implements the various components of the DKIM message-signing and
verifying standard for Internet mail.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc sample_mime_lite.pl
%perl_vendor_privlib/Mail
%exclude %perl_vendor_privlib/Mail/sample*

%changelog
* Sun Oct 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.39-alt2
- fixed build (disabled tests because network is disabled)

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 0.39-alt1
- 0.39

* Mon Jun 21 2010 Victor Forsiuk <force@altlinux.org> 0.38-alt1
- 0.38

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 0.37-alt1
- 0.37

* Thu Jun 19 2008 Victor Forsyuk <force@altlinux.org> 0.32-alt1
- 0.32

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 0.30.1-alt1
- 0.30.1

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 0.29-alt1
- 0.29

* Fri Oct 26 2007 Victor Forsyuk <force@altlinux.org> 0.28-alt1
- 0.28

* Fri Jun 01 2007 Victor Forsyuk <force@altlinux.org> 0.26-alt1
- 0.26

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.24-alt1
- 0.24

* Thu Aug 31 2006 Victor Forsyuk <force@altlinux.ru> 0.18-alt1
- 0.18
- Refresh BuildRequires.

* Wed Jun 07 2006 Victor Forsyuk <force@altlinux.ru> 0.16-alt1
- Initial build.
