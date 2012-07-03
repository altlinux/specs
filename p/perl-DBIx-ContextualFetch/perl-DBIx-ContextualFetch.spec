%define dist DBIx-ContextualFetch
Name: perl-%dist
Version: 1.03
Release: alt2

Summary: Add contextual fetches to DBI
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-DBD-SQLite perl-Test-Pod

%description
It always struck me odd that DBI didn't take much advantage of Perl's
context sensitivity. DBIx::ContextualFetch redefines some of the various
fetch methods to fix this oversight. It also adds a few new methods for
convenience (though not necessarily efficiency).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DBIx

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2
- rebuilt

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.02 -> 1.03

* Thu Jul 14 2005 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- initial revision
