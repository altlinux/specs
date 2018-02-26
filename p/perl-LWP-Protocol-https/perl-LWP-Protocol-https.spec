%define dist LWP-Protocol-https
Name: perl-%dist
Version: 6.02
Release: alt3

Summary: Provide https support for LWP::UserAgent
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: LWP-Protocol-https-6.02-alt-ca.patch

Requires: /usr/share/ca-certificates/ca-bundle.crt
Conflicts: perl-libwww < 6.02

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Net-HTTPS perl-devel perl-libwww

%description
The LWP::Protocol::https module provide support for using https schemed
URLs with LWP.  This module is a plug-in to the LWP protocol handling,
so you don't use it directly.  Once the module is installed LWP is able
to access sites using HTTP over SSL/TLS.

%prep
%setup -q -n %dist-%version
%patch -p1

%ifdef __BTE
# disable online tests
%def_without test
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/LWP

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt3
- rebuilt as plain src.rpm

* Tue Sep 13 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt2
- disabled online tests in hasher

* Mon Apr 04 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- initial revision
- replaced Mozilla::CA with /usr/share/ca-certificates/ca-bundle.crt
