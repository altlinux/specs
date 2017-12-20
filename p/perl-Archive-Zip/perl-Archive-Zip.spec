%define _unpackaged_files_terminate_build 1
BuildRequires: perl-podlators perl(Test/MockModule.pm)
%define dist Archive-Zip
Name: perl-%dist
Version: 1.60
Release: alt1

Summary: Perl module for manipulating Zip archives
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/P/PH/PHRED/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Compress-Raw-Zlib perl-devel

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.

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
%doc	Changes examples README.md
%dir	%perl_vendor_privlib/Archive
	%perl_vendor_privlib/Archive/Zip.pm
%dir	%perl_vendor_privlib/Archive/Zip
	%perl_vendor_privlib/Archive/Zip/*.pm
%doc	%perl_vendor_privlib/Archive/Zip/*.pod

%files scripts
%_bindir/*
#%_man1dir/*


%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.60-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.59-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.57-alt1
- automated CPAN update

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.53-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 1.30-alt2
- rebuilt as plain src.rpm

* Tue Jul 21 2009 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.28 -> 1.30

* Fri Jun 19 2009 Alexey Tourbin <at@altlinux.ru> 1.28-alt1
- 1.26 -> 1.28

* Mon Oct 13 2008 Alexey Tourbin <at@altlinux.ru> 1.26-alt1
- 1.24 -> 1.26

* Sun Oct 05 2008 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.23 -> 1.24

* Fri Apr 18 2008 Alexey Tourbin <at@altlinux.ru> 1.23-alt1
- 1.15 -> 1.23

* Fri Sep 01 2006 Alexey Tourbin <at@altlinux.ru> 1.15-alt2
- fixed test suite: File::Temp has been hardened to check /tmp
  ownership in taint mode; in the hasher build system, /tmp happens
  to be owned neither by the user nor by root, but by special "rooter"
  satellite user; test suite now uses current working directory for
  temporary file creation
- %_bindir/crc32 not packaged

* Sat Jun 25 2005 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.10 -> 1.15
- alt-tmp.patch merged upstream (cpan #6343)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.10-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue May 18 2004 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.5 -> 1.10
- alt-tmp.patch: secure handling of temporary files (cpan #6343)
- packaged docs/ and examples/

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.05-alt1
- rebuild with new perl

* Tue Jun 11 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.01-alt1
- Initial package created
