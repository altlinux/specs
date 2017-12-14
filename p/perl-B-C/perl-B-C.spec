# hack for perl 5.26.1 migration
%def_without test
Name: perl-B-C
Version: 1.55_04
Release: alt1

Summary: Perl compiler's C backend
License: Perl
Group: Development/Perl

URL: %CPAN B-C
# Cloned from git https://code.google.com/p/perl-compiler
Source: %name-%version.tar

BuildRequires: perl-Pod-Parser perl-devel perl-IPC-Run libgdbm-devel libdb4-devel perl-B-Flags perldoc perl-threads perl(Attribute/Handlers.pm) perl(AnyDBM_File.pm) perl(Encode/JP.pm)

%description
%summary

%prep
%setup -q
#for t in issue305
#do
# mv t/$t.t t/$t.t.failed
#done

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/*
%_man1dir/*
%perl_vendor_archlib/B
%perl_vendor_autolib/B
%perl_vendor_archlib/ByteLoader.pm
%perl_vendor_autolib/ByteLoader
%perl_vendor_archlib/BcVersions.pod

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.55_04-alt1
- new version

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.55-alt1
- new version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1.1.1
- rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1.1
- hack for perl 5.24.1 migration

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.54-alt1
- new version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.52-alt2.1
- rebuild with new perl 5.22.0

* Fri Nov 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.52-alt2
- bunch of hacks from mageia to fix build under perl 5.22
- to be removed when upstream release the proper version

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.52-alt1
- automated CPAN update
- locally tests pass, but disabled issue305 for incoming

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.43-alt0.2
- 1.43_git_b16d217b -> 1.43_git_a07eafb8
- disabled failed tests

* Mon Sep 03 2012 Vladimir Lettiev <crux@altlinux.ru> 1.43-alt0.1
- 1.42 -> 1.43_git_b16d217b
- built for perl-5.16
- temporary disabled failed tests

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt2
- Explicitly required build dependency on perl-threads

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- New version 1.42
- Source cloned from git
- New test dependencies: libgdbm-devel, libdb4-devel, perl-B-Flags,
  perldoc

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.36-alt1
- New version 1.36
- Cleanup buildreqs

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.34 -> 1.35
- built for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 1.29-alt1
- New version 1.29

* Wed Nov 10 2010 Vladimir Lettiev <crux@altlinux.ru> 1.27-alt2
- disabled failing test on i586 for a while

* Tue Nov 02 2010 Vladimir Lettiev <crux@altlinux.ru> 1.27-alt1
- initial build
