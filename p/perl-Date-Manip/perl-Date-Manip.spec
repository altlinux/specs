%define _unpackaged_files_terminate_build 1
BuildRequires: perl-podlators perl(File/Find/Rule.pm)
%define dist Date-Manip
Name: perl-Date-Manip
Version: 6.90
Release: alt1.1

Summary: Date manipulation routines
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SB/SBECK/%{dist}-%{version}.tar.gz

%add_findprov_skiplist */Date/Manip/Offset/*.pm
%add_findprov_skiplist */Date/Manip/TZ/*.pm

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-Module-Build perl-Test-Inter perl-Test-Pod perl-Test-Pod-Coverage perl-YAML-Syck

%description
This is a set of Perl routines designed to make any common date/time
manipulation easy to do.  Operations such as comparing two times,
calculating a time a given amount of time from another, or parsing
international times are all easily done.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README README.first examples
%dir	%perl_vendor_privlib/Date
	%perl_vendor_privlib/Date/Manip.pm
%doc	%perl_vendor_privlib/Date/Manip.pod
%dir	%perl_vendor_privlib/Date/Manip
	%perl_vendor_privlib/Date/Manip/*.pm
%doc	%perl_vendor_privlib/Date/Manip/*.pod
%dir	%perl_vendor_privlib/Date/Manip/Lang
	%perl_vendor_privlib/Date/Manip/Lang/*.pm
	%perl_vendor_privlib/Date/Manip/Lang/*.pod
%dir	%perl_vendor_privlib/Date/Manip/Offset
	%perl_vendor_privlib/Date/Manip/Offset/*.pm
%dir	%perl_vendor_privlib/Date/Manip/TZ
	%perl_vendor_privlib/Date/Manip/TZ/*.pm

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 6.90-alt1.1
- automated CPAN update

* Wed Dec 14 2022 Igor Vlasenko <viy@altlinux.org> 6.90-alt1
- automated CPAN update

* Fri Sep 02 2022 Igor Vlasenko <viy@altlinux.org> 6.89-alt1
- automated CPAN update

* Fri Jun 03 2022 Igor Vlasenko <viy@altlinux.org> 6.88-alt1
- automated CPAN update

* Thu Jun 02 2022 Igor Vlasenko <viy@altlinux.org> 6.87-alt1
- automated CPAN update

* Wed Nov 17 2021 Igor Vlasenko <viy@altlinux.org> 6.86-alt1
- automated CPAN update

* Wed Mar 03 2021 Igor Vlasenko <viy@altlinux.org> 6.85-alt1
- automated CPAN update

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 6.83-alt1
- automated CPAN update

* Fri Jun 05 2020 Igor Vlasenko <viy@altlinux.ru> 6.82-alt1
- automated CPAN update

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 6.81-alt1
- automated CPAN update

* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 6.79-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 6.78-alt1
- automated CPAN update

* Wed Jun 05 2019 Igor Vlasenko <viy@altlinux.ru> 6.77-alt1
- automated CPAN update

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 6.76-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 6.75-alt1
- automated CPAN update

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 6.73-alt1
- automated CPAN update

* Sat Jun 09 2018 Igor Vlasenko <viy@altlinux.ru> 6.72-alt1
- automated CPAN update

* Sun Jun 03 2018 Igor Vlasenko <viy@altlinux.ru> 6.71-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 6.70-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 6.60-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.59-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.58-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 6.57-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 6.56-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 6.54-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 6.53-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 6.52-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 6.51-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 6.49-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 6.48-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 6.43-alt1
- automated CPAN update

* Fri Dec 06 2013 Igor Vlasenko <viy@altlinux.ru> 6.42-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 6.41-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 6.40-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 6.34-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 6.25-alt1
- automated CPAN update

* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 6.23-alt1
- 6.21 -> 6.23

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 6.21-alt1
- 6.20 -> 6.21

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 6.20-alt1
- 5.54 -> 6.20

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 5.54-alt1
- 5.48 -> 5.54

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 5.48-alt1
- 5.44 -> 5.48
- use `date +%%z' as possible source for timezone data (rh#248500)

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 5.44-alt2
- imported into git and adapted for gear
- renamed package perl-DateManip -> perl-Date-Manip
- applied rhbz214709.patch from Fedora

* Sat Jun 04 2005 Alexey Tourbin <at@altlinux.ru> 5.44-alt1
- 5.42a -> 5.44
- applied Mandriva patches
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.42a-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 11 2003 Alexey Tourbin <at@altlinux.ru> 5.42a-alt1
- 5.42a
- descriptions updated

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 5.40-alt4.1
- fix spec

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 5.40-alt4
- rebuild with new perl

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 5.40-alt3
- Rebuilt with perl-5.6.1

* Fri Jun 13 2001 Grigory Milev <week@altlinux.ru> 5.40-alt2
- Rewrite spec for compatible with new police

* Fri Jun 08 2001 Grigory Milev <week@altlinux.ru> 5.40-alt1
- new version (5.40)

* Tue May 29 2001 AEN <aen@logic.ru> 5.39-alt1
- first build for Sisyphus
