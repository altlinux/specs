%define dist WWW-RobotRules
Name: perl-%dist
Version: 6.03
Release: alt1

Summary: Database of robots.txt-derived permissions
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# requires AnyDBM_File; not required by any packag
%add_findreq_skiplist */WWW/RobotRules/AnyDBM_File.pm
%add_findreq_skiplist */WWW/RobotRules/DB_File.pm

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-DBM perl-URI perl-devel

%description
This module parses /robots.txt files as specified in "A Standard
for Robot Exclusion", at <http://www.robotstxt.org/wc/norobots.html>
Webmasters can use the /robots.txt file to forbid conforming robots
from accessing parts of their web site.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/WWW

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 6.03-alt1
- new version 6.03
- dropped README from %%doc (not shipped by upstream anymore).
- skip dependency scan of WWW/RobotRules/DB_File.pm (optional backend, needs DB_File; like AnyDBM_File.pm).

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- 6.01 -> 6.02

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- initial revision
