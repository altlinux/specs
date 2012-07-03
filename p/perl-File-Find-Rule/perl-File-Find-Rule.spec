%define dist File-Find-Rule
Name: perl-%dist
Version: 0.33
Release: alt1

Summary: Alternative interface to File::Find
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Number-Compare perl-Test-Differences perl-Text-Glob perl-devel

%description
File::Find::Rule is a friendlier interface to File::Find.  It allows
you to build rules which specify the desired files and directories.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%_bindir/findrule
%perl_vendor_privlib/File

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.33-alt1
- 0.32 -> 0.33

* Mon May 03 2010 Alexey Tourbin <at@altlinux.ru> 0.32-alt1
- 0.30 -> 0.32

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.28 -> 0.30
- packaged %_bindir/findrule

* Tue Jul 12 2005 Vitaly Lipatov <lav@altlinux.ru> 0.28-alt1
- first build for ALT Linux Sisyphus
