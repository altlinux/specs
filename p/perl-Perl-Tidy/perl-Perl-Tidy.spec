%define _unpackaged_files_terminate_build 1
%define dist Perl-Tidy
Name: perl-%dist
Version: 20221112
Release: alt1

Summary: Parses and beautifies perl source
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SH/SHANCOCK/%{dist}-%{version}.tar.gz
Patch: perl-Perl-Tidy-20221112-alt-deps.patch

BuildArch: noarch

Provides: perltidy = %version
Obsoletes: perltidy < %version

# Automatically added by buildreq on Fri Dec 24 2010
BuildRequires: perl-devel perl(Pod/Man.pm) perl(HTML/Entities.pm) perl(Pod/Html.pm)

%description
Perltidy is a tool to indent and reformat perl scripts. It can also
write scripts in html format.

%prep
%setup -q -n %{dist}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc examples docs BUGS.md CHANGES.md INSTALL.md README.md
%perl_vendor_privlib/Perl*
%_bindir/perltidy
%_man1dir/*

%changelog
* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 20221112-alt1
- automated CPAN update

* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 20220613-alt1
- automated CPAN update

* Wed Feb 16 2022 Igor Vlasenko <viy@altlinux.org> 20220217-alt1
- automated CPAN update

* Mon Nov 01 2021 Igor Vlasenko <viy@altlinux.org> 20211029-alt1
- automated CPAN update

* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.org> 20210717-alt1
- automated CPAN update

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 20210625-alt1
- automated CPAN update

* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 20210402-alt1
- automated CPAN update

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 20210111-alt1
- automated CPAN update

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 20201207-alt1
- automated CPAN update

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 20201001-alt1
- automated CPAN update

* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 20200907-alt1
- automated CPAN update

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 20200822-alt1
- automated CPAN update

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 20200619-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 20200110-alt1
- automated CPAN update

* Wed Dec 04 2019 Igor Vlasenko <viy@altlinux.ru> 20191203-alt1
- automated CPAN update

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 20190915-alt1
- automated CPAN update

* Sat Jun 01 2019 Igor Vlasenko <viy@altlinux.ru> 20190601-alt1
- automated CPAN update

* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 20181120-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 20180220-alt1
- automated CPAN update

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 20180219-alt1
- automated CPAN update

* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 20180101-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 20171214-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 20170521-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 20160302-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 20150815-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 20140711-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 20140328-alt1
- automated CPAN update

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 20130922-alt1
- automated CPAN update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 20130806-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 20130717-alt1
- automated CPAN update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 20120714-alt1
- automated CPAN update

* Fri Dec 24 2010 Alexey Tourbin <at@altlinux.ru> 20101217-alt1
- 20101217 -> 20101217

* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 20090616-alt1
- 20031021 -> 20090616
- enabled dependency on HTML::Entities
- merged /usr/bin/perltidy into perl-Perl-Tidy

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 20031021-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 20031021-alt1
- 20031021
- Url and Summary was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 20030726-alt2
- Package splitted, added missed docs.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 20030726-alt1
- First build for ALTLinux.

