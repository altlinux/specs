%define dist Text-Diff
Name: perl-%dist
Version: 1.41
Release: alt1

Summary: Perform diffs on files and record sets
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-Algorithm-Diff perl-devel

%description
Text::Diff provides a basic set of services akin to the GNU diff utility.
It is not anywhere near as feature complete as GNU diff, but it is better
integrated with Perl and available on all platforms. It is often faster
than shelling out to a system's diff executable for small files, and
generally slower on larger files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Text

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.41-alt1
- 1.37 -> 1.41
- rebuild as plain src.rpm

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 0.35 -> 1.37

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.35-alt3.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 0.35-alt3
- Url and Summary tags was fixed.

* Tue Jul 29 2003 Andrey Brindeew <abr@altlinux.ru> 0.35-alt2
- Minor specfile fixes.
- BuildArch was changed to `noarch'.

* Wed Jul 16 2003 Andrey Brindeew <abr@altlinux.ru> 0.35-alt1
- First build for ALTLinux.
