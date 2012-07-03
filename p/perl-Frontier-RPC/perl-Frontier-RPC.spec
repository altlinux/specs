%define dist Frontier-RPC
Name: perl-%dist
Version: 0.07b4
Release: alt3

Summary: Perl module for RPC over XML
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# disable dependency on mod_perl
%add_findreq_skiplist */Apache/XMLRPC.pm

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-HTTP-Daemon perl-XML-Parser perl-devel

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote Procedure Calls
using Extensible Markup Language).  Frontier::RPC includes both a client module
for making requests to a server and several server modules for implementing
servers using CGI, Apache, and standalone with HTTP::Daemon.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Frontier
%perl_vendor_privlib/Frontier/*.pm
%dir %perl_vendor_privlib/Apache
%perl_vendor_privlib/Apache/XMLRPC.pm

%changelog
* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 0.07b4-alt3
- updated build dependencies
- disabled dependency on mod_perl

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07b4-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Aug 28 2005 Serge A. Volkov <vserge at altlinux.ru> 0.07b4-alt2
- Update BuildReq and add BuildPreReq: apache-mod_perl

* Thu Jun 24 2004 Serge A. Volkov <vserge@altlinux.ru> 0.07b4-alt1
- Update to new version 0.07b
- Update BuildReq
- Spec cleanup

* Tue Nov 05 2002 Serge A. Volkov <vserge@altlinux.ru> 0.06-alt1
- first version of rpm for ALT Linux Team.
