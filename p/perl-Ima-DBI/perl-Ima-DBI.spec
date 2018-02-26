%define dist Ima-DBI
Name: perl-%dist
Version: 0.35
Release: alt2

Summary: Database connection caching and organization
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# this dependency cannot be detected automatically
Requires: perl-DBIx-ContextualFetch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Class-Data-Inheritable perl-DBI-devel perl-DBIx-ContextualFetch perl-Test-Pod

%description
Ima::DBI attempts to organize and facilitate caching and more efficient
use of database connections and statement handles by storing DBI and
SQL information with your class (instead of as seperate objects).
This allows you to pass around just one object without worrying about
a trail of DBI handles behind it.

%prep
%setup -q -n %dist-%version

# don't check for existing installation
sed -i- '/^eval { require/,/^}/s/^/#/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Ima

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.35-alt2
- rebuilt

* Sun Aug 05 2007 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- 0.33 -> 0.35

* Mon Aug 29 2005 Alexey Tourbin <at@altlinux.ru> 0.33-alt2
- removed build dependency on perl-Class-WhiteHole (cpan #14359)
- added dependency on perl-DBIx-ContextualFetch
- eliminated build dependency on itself

* Wed Jul 06 2005 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- initial revision
