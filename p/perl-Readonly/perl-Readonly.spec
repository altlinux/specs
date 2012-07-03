%define dist Readonly

Name: perl-%dist
Version: 1.03
Release: alt1.2

Summary: Readonly - facility for creating read-only scalars, arrays, hashes
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Readonly/%dist-%version.tar.gz

BuildArch: noarch

# Always loaded when available.
Requires: perl-Readonly-XS

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Readonly-XS perl-devel

%description
This is a facility for creating non-modifiable variables. This is useful
for configuration files, headers, etc. It can also be useful as a
development and debugging tool, for catching updates to variables that
should not be changed.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install
# Come home, baby!
mv %buildroot%perl_vendor_privlib/benchmark.pl .

%files
%doc README benchmark.pl
%perl_vendor_privlib/Readonly.pm

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1.2
- rebuilt for perl-5.14
- enabled dependency on perl-Readonly-XS

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1.1
- rebuilt with perl 5.12

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.03-alt1
- Initial build.
