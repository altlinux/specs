%define dist Tk-Pod
Name: perl-%dist
Version: 0.9939_58
Release: alt1

Summary: Perl/Tk Pod browser
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# wrapped in eval
Requires: perl-Tk-HistEntry

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-Pod-Simple perl-Text-English perl-Tk-HistEntry perl-devel

%description
This is a graphical user interface for viewing and browsing perl's Pod
documentation.

%prep
%setup -q -n %dist-%version

%build
%ifndef _build_display
%def_without test
%endif
%ifdef __buildreqs
%def_without test
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/tkmore
%_bindir/tkpod
%perl_vendor_privlib/Tk

%changelog
* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.9939_58-alt1
- 0.9929 -> 0.9939_58

* Sun Jul 17 2005 Alexey Tourbin <at@altlinux.ru> 0.9929-alt1
- 0.9926 -> 0.9929
- manual pages not packaged (use perldoc)
- FindPods.patch: fixed @INC search order (cpan #13736)
- font_size.patch: increased default font size

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.9926-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Feb 06 2004 Alexey Tourbin <at@altlinux.ru> 0.9926-alt1
- 0.9926

* Fri Nov 21 2003 Alexey Tourbin <at@altlinux.ru> 0.9925-alt1
- 0.9925

* Tue Oct 07 2003 Alexey Tourbin <at@altlinux.ru> 0.9922-alt1
- initial revision; all tests pass (disabled by default)
