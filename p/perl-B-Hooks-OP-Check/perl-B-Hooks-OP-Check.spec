%define dist B-Hooks-OP-Check
Name: perl-%dist
Version: 0.19
Release: alt1

Summary: Wrap OP check callbacks
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-ExtUtils-Depends perl-Pod-Escapes perl-devel perl-parent

%description
This module provides a C api for XS modules to hook into the callbacks
of PL_check.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/B
%perl_vendor_autolib/B

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.19-alt1
- initial revision
