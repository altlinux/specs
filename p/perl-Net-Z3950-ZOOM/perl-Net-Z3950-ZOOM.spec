%define dist Net-Z3950-ZOOM
Name: perl-%dist
Version: 1.28
Release: alt2

Summary: Perl extension implementing the ZOOM API for Information Retrieval
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011 (-bi)
BuildRequires: libssl-devel libwrap-devel libyaz-devel perl-MARC-Record perl-XML-LibXML perl-devel

%description
This distribution contains three Perl modules for the price of one.
They all provide facilities for building information retrieval clients
using the standard Z39.50 and SRW/U protocols, but do so using
different APIs.

%prep
%setup -n %dist-%version

%ifdef __BTE
# disable network-dependent tests
grep -lZ connect t/*.t |xargs -r0 rm -v
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/zselect
%_bindir/zoomdump
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net
%perl_vendor_archlib/ZOOM*

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.28-alt2
- rebuilt for perl-5.14

* Wed Jul 13 2011 Dmitry V. Levin <ldv@altlinux.org> 1.28-alt1
- Updated to 1.28.
- Updated build dependencies.

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 1.25-alt1.1.1
- rebuilt with perl 5.12

* Mon Oct 27 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.25-alt1.1
- rebuild w/o test

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.25-alt1
- new version

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.24-alt2
- fixed build

* Tue Jul 01 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.24-alt1
- new version

* Wed Aug 01 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.19-alt1
- new version

* Mon Jun 11 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 1.18-alt1
- first build for ALT Linux Sisyphus
