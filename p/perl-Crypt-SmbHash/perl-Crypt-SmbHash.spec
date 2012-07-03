%define dist Crypt-SmbHash
Name: perl-%dist
Version: 0.12
Release: alt2

Summary: lanman and nt md4 hash functions, for use in Samba style smbpasswd entries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# always loaded when available
Requires: perl-Digest-MD4 perl-Encode

# Automatically added by buildreq on Wed Oct 26 2011
BuildRequires: perl-Digest-MD4 perl-Encode perl-devel

%description
This module provides functions to generate LM/NT hashes used in Samba's
'password' files, like smbpasswd.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Crypt

%changelog
* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- noarch

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.02-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Aug 16 2004 Nick S. Grechukh <gns@altlinux.ru> 0.02-alt1
- first build fo Sisyphus.
