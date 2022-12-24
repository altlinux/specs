%define _unpackaged_files_terminate_build 1
%define dist Module-Build
Name: perl-%dist
Version: 0.4232
Release: alt1.1

Summary: Build and install Perl modules
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/L/LE/LEONT/%{dist}-%{version}.tar.gz
Patch: Module-Build-0.4224-alt-fix-shabang.patch

BuildArch: noarch

# moved to separate package
Requires: perl(inc/latest.pm)

# loaded with try_require
Requires: perl-CPAN-Meta

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Archive-Tar perl-Archive-Zip perl-CPAN-Meta perl-ExtUtils-CBuilder perl-File-ShareDir perl-Module-Metadata perl-PAR-Dist perl-Perl-OSType perl-Tie-IxHash perl(Pod/Man.pm) perl-podlators

%description
Module::Build is a Perl module to build and install Perl modules.
It is meant to be a replacement for ExtUtils::MakeMaker.

%prep
%setup -q -n %{dist}-%{version}
%patch -p1
bzip2 -k Changes

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	README Changes
	%_bindir/config_data
	%_man1dir/config_data*
%dir	%perl_vendor_privlib/Module
	%perl_vendor_privlib/Module/Build.pm
%dir	%perl_vendor_privlib/Module/Build
	%perl_vendor_privlib/Module/Build/*.pm
%doc	%perl_vendor_privlib/Module/Build/*.pod
%dir	%perl_vendor_privlib/Module/Build/Platform
	%perl_vendor_privlib/Module/Build/Platform/Unix.pm

%exclude %perl_vendor_privlib/Module/Build/Platform/Default.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/MacOS.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/VMS.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/VOS.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/Windows.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/aix.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/cygwin.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/darwin.pm
%exclude %perl_vendor_privlib/Module/Build/Platform/os2.pm

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.4232-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 0.4232-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.4231-alt1
- automated CPAN update

* Fri Apr 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.4229-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.4224-alt2
- Module-Build-0.4224-alt-fix-shabang.patch

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.4224-alt1
- automated CPAN update

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.4222-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.4220-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.4218-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.4216-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.4214-alt1
- new version

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.4210-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.4206-alt1
- automated CPAN update

* Mon Feb 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.4205-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.4204-alt1
- automated CPAN update

* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.4203-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.4202-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.4200-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.4007-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.4003-alt1
- 0.3800 -> 0.4003
- fixed build with perl-5.16

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.3800-alt1
- 0.36_04 -> 0.3800

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.36_04-alt1.1
- rebuilt with perl 5.12

* Thu Mar 18 2010 Alexey Tourbin <at@altlinux.ru> 0.36_04-alt1
- 0.33 -> 0.36_04

* Tue May 12 2009 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.30 -> 0.33

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.2808 -> 0.30

* Fri Aug 17 2007 Alexey Tourbin <at@altlinux.ru> 0.28.08-alt2
- Module/Build/Version.pm: unveil dependency on version.pm

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 0.28.08-alt1
- 0.2612 -> 0.2808
- disabled dependency on Archive::Tar

* Sat Apr 07 2007 Alexey Tourbin <at@altlinux.ru> 0.26.12-alt1
- 0.2610 -> 0.2612; note: we are still on 0.26 branch; 0.28 branch
  uses ExtUtils::CBuilder which I do not want for now

* Sat Apr 16 2005 Alexey Tourbin <at@altlinux.ru> 0.26.10-alt1
- 0.26 -> 0.2610
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.26-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Oct 12 2004 Alexey Tourbin <at@altlinux.ru> 0.26-alt1
- 0.25 -> 0.26

* Sun May 09 2004 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- initial revision
