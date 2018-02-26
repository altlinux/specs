%define dist Archive-Zip
Name: perl-%dist
Version: 1.30
Release: alt2

Summary: Perl module for manipulating Zip archives
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-Compress-Raw-Zlib perl-devel

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes examples README
%dir	%perl_vendor_privlib/Archive
	%perl_vendor_privlib/Archive/Zip.pm
%dir	%perl_vendor_privlib/Archive/Zip
	%perl_vendor_privlib/Archive/Zip/*.pm
%doc	%perl_vendor_privlib/Archive/Zip/*.pod

%changelog
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
