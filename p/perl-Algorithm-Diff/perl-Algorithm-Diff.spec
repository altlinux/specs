%define dist Algorithm-Diff
Name: perl-%dist
Version: 1.1902
Release: alt2

Summary: Compute `intelligent' differences between two files / lists
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 03 2011
BuildRequires: perl-devel

%description
This is a module for computing the difference between two files, two strings,
or any other two lists of things.  It uses an  intelligent algorithm similar to
(or identical to) the one used by the Unix `diff' program. It is guaranteed to
find the *smallest possible* set of differences.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

rm %buildroot%perl_vendor_privlib/Algorithm/*diff*.pl

%files
%doc Changes README *diff*.pl
%dir %perl_vendor_privlib/Algorithm
%perl_vendor_privlib/Algorithm/Diff.pm
%perl_vendor_privlib/Algorithm/DiffOld.pm

%changelog
* Mon Oct 03 2011 Alexey Tourbin <at@altlinux.ru> 1.1902-alt2
- rebuilt as plain src.rpm

* Tue Sep 16 2008 Alexey Tourbin <at@altlinux.ru> 1.1902-alt1
- 1.1901 -> 1.1902

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.1901-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 1.1901-alt1
- 1.1901.

* Tue Nov 25 2003 Andrey Brindeew <abr@altlinux.ru> 1.15-alt3
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 1.15-alt2
- Minor specfile fixes.
- BuildArch was changed to `noarch'.
- Examples moved to docs.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 1.15-alt1
- First build for ALTLinux.
