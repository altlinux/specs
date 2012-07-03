%define dist Xmms-Perl
Name: perl-Xmms
version: 0.12
Release: alt2

Summary: fullname (module for perl)
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libxmms-devel perl-Term-ANSIColor perl-Term-ReadLine-Gnu perl-devel

%description
Xmms module for perl

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Xmms*
%perl_vendor_autolib/Xmms

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1.5.1
- rebuilt with perl 5.12

* Fri Jun 17 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.12-alt1.5
- Fixed Arch (closes #6499).

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.12-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Oct 31 2004 Pavlov Konstantin <thresh@altlinux.ru> 0.12-alt1
- Initial build for Sisyphus

