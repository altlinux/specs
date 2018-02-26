%define dist URI-Fetch
Name: perl-%dist
Version: 0.09
Release: alt2

Summary: Smart URI fetching/caching
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Class-ErrorHandler perl-Filter perl-Pod-Escapes perl-devel perl-libwww

%description
URI::Fetch is a smart client for fetching HTTP pages, notably
syndication feeds (RSS, Atom, and others), in an intelligent,
bandwidth- and time-saving way.

%prep
%setup -q -n %dist-%version

%ifdef __BTE
# requires network
rm t/01-fetch.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/URI

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt2
- disabled build dependency on perl-Module-Install

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.08 -> 0.09

* Sun Jul 22 2007 Alexey Tourbin <at@altlinux.ru> 0.08-alt2
- eliminated build dependency on ExtUtils::AutoInstall

* Tue Sep 05 2006 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- 0.07 -> 0.08

* Sat Jun 24 2006 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- 0.06 -> 0.07

* Thu Apr 20 2006 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- 0.03 -> 0.06

* Mon Aug 22 2005 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision (for XML::Feed)
