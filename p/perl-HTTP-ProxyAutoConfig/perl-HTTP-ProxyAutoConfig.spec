%def_disable test

%define dist HTTP-ProxyAutoConfig
Name: perl-%dist
Version: 0.3
Release: alt2

Summary: Unifed way to get the proxy information
License: LGPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 21 2010
BuildRequires: perl-devel perl-libwww

%description
This module is being developed to provide access for Perl scripts to
the Proxy Auto Config format from Netscape.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Sun Oct 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2
- fixed build (disabled tests because network is disabled)

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 0.3-alt1
- 0.1 -> 0.3

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Oct 28 2003 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
