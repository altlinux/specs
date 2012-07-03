%define dist Net-XWhois
Name: perl-%dist
Version: 0.90
Release: alt1.1.1

Summary: Whois Client Interface for Perl5
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.bz2

Patch0: %name-0.90-alt-tmp.patch

BuildArch: noarch

# Automatically added by buildreq on Sun Mar 07 2004
BuildRequires: perl-devel

%description
The Net::XWhois class provides a generic client framework for doing
whois (RFC 954) queries and parsing server response.

%prep
%setup -q -n %dist-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes TODO contribs examples
%perl_vendor_privlib/Net*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.90-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Mar 07 2004 Alexey Tourbin <at@altlinux.ru> 0.90-alt1
- initial revision (this package is required by ispman)
- alt-tmp.patch: regard $ENV{TMPDIR}
