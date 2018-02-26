%define dist IO-Zlib
Name: perl-%dist
Version: 1.10
Release: alt2

Summary: IO:: style interface to Compress::Zlib
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-IO-Compress perl-devel

%description
This modules provides an IO:: style interface to the Compress::Zlib
package. The main advantage is that you can use an IO::Zlib object
in much the same way as an IO::File object so you can have common
code that doesn't know which sort of file it is using.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/IO

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.10-alt2
- rebuilt as plain src.rpm

* Thu Jul 16 2009 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.09 -> 1.10

* Thu Jun 12 2008 Alexey Tourbin <at@altlinux.ru> 1.09-alt1
- 1.04 -> 1.09

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.04-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 1.04-alt1
- 1.04

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 1.01-alt2
- Url and Summary tags was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.01-alt1
- First build for ALT Linux.
