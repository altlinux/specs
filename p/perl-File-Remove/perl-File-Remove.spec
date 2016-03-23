%define _unpackaged_files_terminate_build 1
%define dist File-Remove
Name: perl-%dist
Version: 1.56
Release: alt1

Summary: Remove files and directories
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SH/SHLOMIF/File-Remove-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Pod-Escapes perl-devel perl(Module/Build.pm)

%description
File::Remove::remove removes files and directories.  It acts like
/bin/rm, for the most part.  Although unlink can be given a list
of files, it will not remove directories; this module remedies that.
It also accepts wildcards, * and ?, as arguments for filenames.

File::Remove::trash accepts the same arguments as remove, with
the addition of an optional, infrequently used "other platforms"
hashref.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File

%changelog
* Wed Mar 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.56-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.51-alt1
- 1.46 -> 1.51

* Sun Feb 27 2011 Alexey Tourbin <at@altlinux.ru> 1.46-alt1
- 1.42 -> 1.46

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 1.42-alt1
- 0.30 -> 1.42

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.30-alt2
- fix directory ownership violation

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.30-alt1
- new version

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.29-alt1
- first build for ALT Linux Sisyphus
