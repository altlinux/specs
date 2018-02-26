%define dist Tie-IxHash
Name: perl-%dist
Version: 1.22
Release: alt1

Packager: Andrey Brindeew <abr@altlinux.ru>

Summary: Ordered associative arrays for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-Module-Build perl-Test-Pod

%description
This Perl module implements Perl hashes that preserve the
order in which the hash elements were added. The order is not
affected when values corresponding to existing keys in the
IxHash are changed. The elements can also be set to any
arbitrary supplied order. The familiar perl array operations
can also be performed on the IxHash.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Tie*

%changelog
* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.21 -> 1.22

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.21-alt5.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Oct 06 2003 Andrey Brindeew <abr@altlinux.ru> 1.21-alt5
- Both Packager & Summary tags was updated
- Url tag added

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.21-alt4
- rebuild with new perl

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 1.21-alt3
- rebuild with gcc3

* Mon Jun 10 2002 Sir Raorn <raorn@altlinux.ru> 1.21-alt2
- Oops. Wrong Url tag. Removed.

* Mon Jun 10 2002 Sir Raorn <raorn@altlinux.ru> 1.21-alt1
- Built for Sisyphus

