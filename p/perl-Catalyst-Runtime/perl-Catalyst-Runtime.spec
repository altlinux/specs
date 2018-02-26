%define dist Catalyst-Runtime
Name: perl-%dist
Version: 5.90002
Release: alt1

Summary: Web application framework
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Catalyst-Runtime/
Source: http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Runtime-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011 (-bi)
BuildRequires: perl-CGI-Simple perl-Catalyst-Devel perl-Class-C3-Adopt-NEXT perl-Class-Data-Inheritable perl-Data-Dump perl-FCGI perl-HTTP-Body perl-HTTP-Request-AsCGI perl-Module-Pluggable perl-MooseX-Getopt perl-MooseX-MethodAttributes perl-MooseX-Role-WithOverloading perl-MooseX-Types-Common perl-Pod-Parser perl-String-RewritePrefix perl-Task-Weaken perl-Test-Exception perl-Text-Balanced perl-Text-SimpleTable perl-Tree-Simple-VisitorFactory perl-YAML perl(Plack/Test.pm) perl(Plack/Middleware/ReverseProxy.pm) perl(MooseX/Types/LoadableClass.pm)

%description
This is the Runtime distribution for the Catalyst MVC framework.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
# FIXME: Circular deps on Catalyst::Devel
%doc Changes README
%_bindir/catalyst.pl
%_man1dir/catalyst.pl.1*
%perl_vendor_privlib/Catalyst*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 5.90002-alt1
- automated CPAN update

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 5.80030-alt1
- 5.80024 -> 5.80030

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 5.80024-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun May 16 2010 Alexey Tourbin <at@altlinux.ru> 5.80024-alt1
- 5.80022 -> 5.80024

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 5.80022-alt3
- rebuilt with rpm-build-perl 0.72

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 5.80022-alt2
- re-enabled dependency on Catalyst::Restarter

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 5.80022-alt1
- 5.7015 -> 5.80022
- unit_core_script_test.t: fixed STDIN/STDOUT thinko (rt.cpan.org #56590)
- disabled dependency on Catalyst::Restarter, to facilitate bootstrap

* Sun Dec 14 2008 Michael Bochkaryov <misha@altlinux.ru> 5.7015-alt1
- 5.7015 version
- build requirements updated

* Mon Sep 08 2008 Michael Bochkaryov <misha@altlinux.ru> 5.7014-alt2
- fix directory ownership violation

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 5.7014-alt1
- 5.7014 version

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 5.7006-alt1
- first build for ALT Linux Sisyphus

