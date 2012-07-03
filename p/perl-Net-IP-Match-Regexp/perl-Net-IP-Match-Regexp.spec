%define dist Net-IP-Match-Regexp

Name: perl-%dist
Version: 1.01
Release: alt3

Summary: Efficiently match IP addresses against IP ranges
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildPreReq: /proc rpm-build-licenses

# Automatically added by buildreq on Sun Aug 23 2009
BuildRequires: perl-Module-Build

%description
This module allows you to check an IP address against one or more IP ranges.
It employs Perl's highly optimized regular expression engine to do the hard
work, so it is very fast. It is optimized for speed by doing the match against
a regexp which implicitly checks the broadest IP ranges first. An advantage is
that the regexp can be computed and stored in advance (in source code, in a
database table, etc) and reused, saving much time if the IP ranges don't change
too often. The match can optionally report a value (e.g. a network name) instead
of just a boolean, which makes module useful for mapping IP ranges to names or
codes or anything else.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES

%perl_vendor_privlib/Net/IP/*

%changelog
* Wed Nov 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.01-alt3
- removed macro %%perl_vendor_man3dir from spec
- removed Packager from spec

* Mon Aug 24 2009 Sergey Y. Afonin <asy@altlinux.ru> 1.01-alt2
- Fixed description

* Sun Aug 23 2009 Sergey Y. Afonin <asy@altlinux.ru> 1.01-alt1
- Initial build for ALTLinux
