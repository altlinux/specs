%define module Gear-Rules

Name: perl-%module
Version: 0.08
Release: alt4
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering Gear rules files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl-RPM-Source-Editor > 0.73
Requires: gear

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/G*
%_bindir/*

%changelog
* Sat Nov 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- added --force to gear-rules-restore-branches

* Wed Nov 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt3
- added gear dependency.

* Wed Nov 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- added gear-rules-restore-branches

* Tue Nov 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- new version

* Sun Oct 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- new version

* Thu Oct 20 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Tue Oct 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- new version

* Sun Oct 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- new version

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

* Thu Oct 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Sun Sep 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
