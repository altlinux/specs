%define _unpackaged_files_terminate_build 1
%define dist GDGraph
Name: perl-GD-Graph
Version: 1.56
Release: alt1
Epoch: 1

Summary: Create charts using GD
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BP/BPS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-GD-Text perl-devel perl(CGI.pm) perl(Config.pm) perl(DBI.pm) perl(Data/Dumper.pm) perl(GD.pm)  perl(Test.pm) perl(Test/More.pm) perl(Text/ParseWords.pm) perl(Test/Exception.pm) perl(Capture/Tiny.pm)

%description
This is GDGraph, a package to generate charts, using Lincoln Stein's
GD.pm. See the documentation for some history and more information.

%prep
%setup -q -n %{dist}-%{version}

#libgd3 disabled gd2, so some tests fail; see perl-GD
%if "%version" == "1.54"
%define _without_test 1
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/GD

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 1:1.56-alt1
- automated CPAN update

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 1:1.54-alt2
- fixed build

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.54-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.53-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.52-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.51-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.49-alt1
- automated CPAN update

* Sun Mar 30 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.48-alt1
- new version

* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1:1.44-alt2
- rebuilt

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.44-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Sep 30 2008 Afanasov Dmitry <ender@altlinux.org> 1.44-alt1
- back to 1.44 release due to unmets

* Mon Sep 29 2008 Afanasov Dmitry <ender@altlinux.org> 1.4401-alt1
- pick orphaned package and specify Packager
- 1.4401 release
- fix BuildRequires
- remove Requires due to hope in automatic search

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 1.4307-alt1
- 1.4307 release

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.43-alt7.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt7
- Summary tag was fixed.

* Wed Aug 13 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt6
- BuildArch was changed to `noarch'.

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt5
- Fixed BuildRequires list using buildreq

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt4
- Applied patch from at@

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt3
- Fixed Requires list.

* Thu Jul 17 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt2
- {,Build}Reqires lists updated.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.43-alt1
- First build for ALTLinux.


