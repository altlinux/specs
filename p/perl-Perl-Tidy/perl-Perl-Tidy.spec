%define _unpackaged_files_terminate_build 1
%define dist Perl-Tidy
Name: perl-%dist
Version: 20171214
Release: alt1

Summary: Parses and beautifies perl source
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SH/SHANCOCK/%{dist}-%{version}.tar.gz
Patch: perl-Perl-Tidy-20120714-alt-deps.patch

BuildArch: noarch

Provides: perltidy = %version
Obsoletes: perltidy < %version

# Automatically added by buildreq on Fri Dec 24 2010
BuildRequires: perl-devel perl(Pod/Man.pm)

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
%doc CHANGES README BUGS examples docs/tutorial.pod docs/stylekey.pod docs
%perl_vendor_privlib/Perl*
%_bindir/perltidy
%_man1dir/*

%changelog
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

