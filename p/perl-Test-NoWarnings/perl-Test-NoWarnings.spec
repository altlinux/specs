%define dist Test-NoWarnings
Name: perl-%dist
Version: 1.04
Release: alt1

Summary: Make sure you didn't emit any warnings while testing
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# always loaded when available
Requires: perl-Devel-StackTrace

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Devel-StackTrace perl-Test-Tester

%description
In general, your tests shouldn't produce warnings. This modules causes any
warnings to be captured and stored. It automatically adds an extra test that
will run when your script ends to check that there were no warnings. If
there were any warings, the test will give a "not ok" and diagnostics of
where, when and what the warning was, including a stack trace of what was
going on when the it occurred.

If some of your tests are supposed to produce warnings then you should be
capturing and checking them with Test::Warn, that way Test::NoWarnings
will not see them and so not complain.

The test is run by an END block in Test::NoWarnings. It will not be run when
any forked children exit.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 1.03 -> 1.04

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2
- added explicit dependency on perl-Devel-StackTrace

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- 1.01 -> 1.03

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- 0.084 -> 1.01
- enabled dependency on Devel::StackTrace

* Mon Dec 08 2008 Mikhail Pokidko <pma@altlinux.org> 0.084-alt1
- initial build for ALT Linux Sisyphus
