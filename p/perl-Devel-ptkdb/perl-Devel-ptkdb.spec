%define dist Devel-ptkdb
# upstream 1.234 is numerically greater than 1.1092, rpm needs 1.2340
%define uver 1.234
Name: perl-%dist
Version: 1.2340
Release: alt1

Summary: Perl debugger using a Tk GUI

License: GPL or Artistic
Group: Development/Perl

URL: https://sourceforge.net/projects/ptkdb/
# Source-url: https://downloads.sourceforge.net/project/ptkdb/ptkdb/%uver/Devel-ptkdb-%uver.tar.gz
Source: %name-%version.tar
Patch: %name-%uver-alt-no-cpan.patch
# Ubuntu/Debian bug 783756
Patch1: %name-%uver-ubuntu-precedence.patch

BuildArch: noarch

# Automatically added by buildreq on Sun Oct 18 2009
BuildRequires: perl-Tk perl-devel

%description
ptkdb is a debugger for perl that uses perl-Tk for a user interface.
It features pushbutton controls for run, step-in, step-out, return,
controls for breakpoints, expression evaluation and package browsing.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
# test.pl needs a running X display
%define _disable_test 1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README changes
%perl_vendor_privlib/Devel*

%changelog
* Fri Oct 16 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2340-alt1
- new version 1.234 (as 1.2340 to keep the version ordering)
- reworked no-cpan patch for the new version
- added Ubuntu patch: fix precedence issue in breakPointEvalExpr
- updated URL and Source-url (SourceForge)
- disabled tests (they need a running X display)
- switched to .tar source via gear tar rule

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.1092-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 18 2009 Grigory Batalov <bga@altlinux.ru> 1.1092-alt1
- New upstream release.

* Mon Aug 02 2004 Alexey Tourbin <at@altlinux.ru> 1.1091-alt1
- initial revision
- no-cpan.patch: do not try to install Tk with CPAN
