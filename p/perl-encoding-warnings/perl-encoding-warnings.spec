%define dist encoding-warnings
Name: perl-%dist
Version: 0.11
Release: alt2

Summary: Warn on implicit encoding conversions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Encode perl-devel

%description
This perl pragma emits warnings whenever an ASCII character string containing
high-bit bytes is implicitly converted into UTF-8. It is useful when working
with mixed encoding strings.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/encoding

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- disabled build dependency on perl-Module-Install

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- initial revision
