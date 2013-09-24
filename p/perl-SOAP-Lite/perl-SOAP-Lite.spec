%define dist SOAP-Lite
Name: perl-%dist
Version: 1.06
Release: alt1

Summary: Perl's Web Services Toolkit
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/P/PH/PHRED/SOAP-Lite-%{version}.tar.gz
Patch0: perl-SOAP-Lite-0.715-IO-modules.patch

BuildArch: noarch

# Cannot be detected automatically
Requires: perl-XML-Parser

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: apache-mod_perl-base perl-Class-Inspector perl-Crypt-SSLeay perl-DIME-Tools perl-HTTP-Daemon perl-IO-Socket-SSL perl-MIME-Lite perl-MIME-tools perl-Task-Weaken perl-Test-Differences perl-Test-MockObject perl-UNIVERSAL-require perl-XML-Parser perl(XMLRPC/Lite.pm)

%description
SOAP::Lite is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both
on client and server side.

%prep
%setup -q -n %dist-%version
sed -i '1s@^#!.*/bin/env perl@#!/usr/bin/perl@' bin/*.pl
%patch0 -p1 -b .IO

%build
%perl_vendor_build

%install
%perl_vendor_install

# Avoid dependency on mod_perl
%add_findreq_skiplist */SOAP/Transport/HTTP.pm

# XXX Can't locate SOAP/Transport/TCP.pm in @INC
%add_findreq_skiplist */XMLRPC/Transport/TCP.pm

# Workaround "Supported versions:" error
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MSOAP::Lite'

%files
%doc Changes README examples
%_bindir/*.pl
%perl_vendor_privlib/Apache/SOAP.pm
#perl_vendor_privlib/IO
%perl_vendor_privlib/SOAP
#perl_vendor_privlib/UDDI
#perl_vendor_privlib/XML
#perl_vendor_privlib/XMLRPC

%changelog
* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- manual CPAN update
- staff moved to perl-IO-SessionData perl-XMLRPC-Lite

* Sat Oct 13 2012 Vladimir Lettiev <crux@altlinux.ru> 0.715-alt3
- Fixed bug rt#78692 (Closes: #27833)

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.715-alt2
- restored perl(IO/SessionData.pm), perl(IO/SessionSet.pm)
  using fc perl-SOAP-Lite-0.715-IO-modules.patch

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.715-alt1
- automated CPAN update

* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 0.714-alt1
- 0.712 -> 0.714

* Thu Apr 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.712-alt2
- fix build

* Fri Feb 04 2011 Alexey Tourbin <at@altlinux.ru> 0.712-alt1
- 0.67 -> 0.712

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1.qa1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.67-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for perl-SOAP-Lite
  * postclean-05-filetriggers for spec file

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 0.67-alt1
- 0.67 release

* Wed Mar 30 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.60-alt3.a
- disabled server tests (03-server.t has too many prerequisites)

* Sun Dec 12 2004 Andrey Brindeew <abr@altlinux.org> 0.60-alt2.a
- rebuild with new rpm-build-perl
- invalid paths for env patched
- examples are now in separate package

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 0.60-alt1.a
- First build for ALT Linux

