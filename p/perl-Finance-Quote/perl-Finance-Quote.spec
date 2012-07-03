%define dist Finance-Quote

Name: perl-%dist
Version: 1.17
Release: alt3

Summary: Get stock and mutual fund quotes from various exchanges
License: GPLv2+
Group: Development/Perl

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/E/EC/ECOCODE/%dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-CGI perl-Crypt-SSLeay perl-HTML-TableExtract perl-HTML-Tree perl-devel perl-libwww

%description
This module gets stock quotes from various internet sources, including
Yahoo! Finance, Fidelity Investments, and the Australian Stock Exchange.
There are two methods of using this module -- a functional interface
that is depreciated, and an object-orientated method that provides
greater flexibility and stability.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Examples/ Documentation/
%perl_vendor_privlib/Finance

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.17-alt3
- disabled build dependency on perl-Module-Install

* Mon Jan 10 2011 Victor Forsiuk <force@altlinux.org> 1.17-alt2
- Fix FTBFS (typo in makefile.PL).
- Correct License.

* Sat Mar 27 2010 Alexey Tourbin <at@altlinux.ru> 1.17-alt1
- 1.08 -> 1.17

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.08-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Oct 01 2003 Alexey Tourbin <at@altlinux.ru> 1.08-alt1
- updated to 1.08
- fixed dependencies
- added docs

* Tue Sep 30 2003 Grigory Milev <week@altlinux.ru> 1.07-alt3
- fix for autorequire find
- fix build requires

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1.07-alt2
- rebuild with new perl

* Tue May 28 2002 Grigory Milev <week@altlinux.ru> 1.07-alt1
- new version released

* Tue Jul 10 2001 Grigory Milev <week@altlinux.ru> 1.06-alt1
- new version (1.06)
- Some spec cleanup

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.05-alt3
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Fri Jun 13 2001 Grigory Milev <week@altlinux.ru> 1.05-alt2
- Rewrite spec for compatible with new police

* Tue May 29 2001 AEN <aen@logic.ru> 1.05-alt1
- first build for Sisyphus
