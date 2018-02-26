%define dist HTTP-Cookies
Name: perl-%dist
Version: 6.01
Release: alt1

Summary: HTTP cookie jars
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# requires Win32
%add_findreq_skiplist */HTTP/Cookies/Microsoft.pm

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-HTTP-Message perl-devel

%description
This class is for objects that represent a "cookie jar" - that is,
a database of all the HTTP cookies that a given LWP::UserAgent object
knows about.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- 6.00 -> 6.01

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
