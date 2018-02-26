%define m_distro Net-FastCGI
Name: perl-Net-FastCGI
Version: 0.13
Release: alt1
Summary: Net::FastCGI - FastCGI Toolkit

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~chansen/Net-FastCGI/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Test-HexString perl-Test-Exception

%description
This distribution aims to provide a complete API for working with the
FastCGI protocol.
The primary goal is to provide a function oriented and object oriented
API which are not tied to a specific I/O model or framework.
Secondary goal is to provide higher level tools/API which can be used
for debugging and interoperability testing.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/FastCGI*
%doc Changes README 

%changelog
* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- New version 0.13

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- initial build
