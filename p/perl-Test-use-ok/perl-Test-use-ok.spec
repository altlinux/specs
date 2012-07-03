%define dist Test-use-ok
Name: perl-%dist
Version: 0.02
Release: alt2.3

Summary: Alternative to Test::More::use_ok
License: MIT
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-devel

%description
According to the Test::More documentation, it is recommended to run
"use_ok()" inside a "BEGIN" block, so functions are exported at
compile-time and prototypes are properly honored.

With this module, simply change all "use_ok" in test scripts to "use
ok", and they will be executed at "BEGIN" time. The explicit space after
"use" makes it clear that this is a single compile-time action.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test
%perl_vendor_privlib/ok.pm

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt2.3
- disabled build dependency on perl-Module-Install

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.02-alt2.2
- specfile cleanup

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2.1
- NMU for unknown reason

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 0.02-alt2
- spec file cleanup (correct license, docs added)

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.02-alt1
- first build for ALT Linux Sisyphus
