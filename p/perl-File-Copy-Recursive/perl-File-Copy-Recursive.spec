%define _unpackaged_files_terminate_build 1
%define dist File-Copy-Recursive
Name: perl-%dist
Version: 0.39
Release: alt1

Summary: Perl extension for recursively copying files and directories
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DM/DMUEY/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-devel perl(Test/Deep.pm) perl(Test/Exception.pm) perl(Test/File.pm) perl(Test/Warn.pm) perl(File/Slurp.pm) perl(Path/Iter.pm)

%description
This module copies and moves directories recursively (or single files,
well... singley) to an optional depth and attempts to preserve each file
or directory's mode.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File

%changelog
* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.38-alt2
- rebuilt as plain src.rpm

* Tue Jan 19 2010 Vitaly Lipatov <lav@altlinux.ru> 0.38-alt1
- new version (0.38)

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- 0.36 -> 0.37

* Mon Aug 11 2008 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.29 -> 0.36

* Wed Nov 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.29-alt1
- first build for ALT Linux Sisyphus
