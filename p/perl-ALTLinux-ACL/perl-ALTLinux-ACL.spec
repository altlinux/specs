%define module ALTLinux-ACL

Name: perl-%module
Version: 0.10
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering ALTLinux ACL files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl(Pod/Usage.pm) perl-RPM perl-IPC-Run3 perl(Data/Array2ArrayMap/Hash/XSTree.pm)

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
%perl_vendor_privlib/ALT*
%_bindir/*

%changelog
* Fri Jan 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added altlinux-acl-report-split-by-acl

* Wed Oct 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- new version

* Wed Oct 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- new version

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added altlinux-acl-filter-list-* scripts

* Thu May 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- support for shared options

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- altlinux-acl-filter: added filter by leadership

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added changelog2ALTLinuxACLleader script

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.M51.1
- backport

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- skip empty lines in acl filter

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- new version

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- new version

* Tue Oct 12 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- new version
