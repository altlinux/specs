%define dist autodie
Name: perl-%dist
Version: 2.11
Release: alt1

Summary: Replace functions with ones that succeed or die with lexical scope
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-BSD-Resource perl-DBM perl-Sub-Identify perl-Tie-RefHash perl-devel

%description
This distribution provides 'autodie', a lexical equivalent
of 'Fatal'.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Fatal*
%perl_vendor_privlib/autodie*

%changelog
* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 2.11-alt1
- 2.10 -> 2.11

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 2.10-alt2
- disabled build dependency on perl-Module-Install

* Sun Sep 19 2010 Alexey Tourbin <at@altlinux.ru> 2.10-alt1
- initial revision
