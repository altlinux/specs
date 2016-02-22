#define module Source-Text-Dependency-Analyser
%define module RPM-Source-Dependency-Analyzer
# useful for testexpect updates
#define _without_test 1

Name: perl-%module
Version: 0.011
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl library for finding build dependencies from software sources
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

Conflicts: perl-RPM-Source-Editor < 0.855

BuildRequires: perl-devel /usr/bin/pod2man perl-podlators perl-RPM-Source-Editor perl(Pod/Strip.pm)
BuildRequires: perl-DistroMap perl-Marpa-R2

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# TODO! distrodb!
install -Dm644 stdheaders.txt %buildroot%_datadir/%module/headers-ignore/stdheaders.txt

%files
%doc Changes
%perl_vendor_privlib/R*
%_datadir/%module
%_bindir/buildreq-*
%_man1dir/buildreq-*

%changelog
* Mon Feb 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.011-alt1
- development release

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- development release

* Sat Feb 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- development release

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- development release

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- bugfix release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- bugfix release

* Sat Jan 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- development release

* Fri Jan 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- development release

* Fri Jan 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- bugfix release

* Wed Dec 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- development release

* Tue Dec 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version

