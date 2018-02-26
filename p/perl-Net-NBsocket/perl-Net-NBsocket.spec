%define module Net-NBsocket

Name: perl-%module
Version: 0.21
Release: alt1

Summary: Net::NBsocket - Non-Blocking Sockets
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/M/MI/MIKER/Net-NBsocket-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 25 2012
BuildRequires: perl-NetAddr-IP perl-devel

%description
Net::NBsocket provides a wrapper for Socket to supply Non-Blocking
sockets of various flavors.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net
%perl_vendor_privlib/auto/Net

%changelog
* Sun Mar 25 2012 Victor Forsiuk <force@altlinux.org> 0.21-alt1
- 0.21

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 0.15-alt1
- 0.15

* Thu Jul 05 2007 Victor Forsyuk <force@altlinux.org> 0.13-alt1
- Initial build.
