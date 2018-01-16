%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm) perl(Test/LeakTrace.pm)
%define dist Mouse
Name: perl-%dist
Version: 2.5.1
Release: alt1

Summary: Moose minus the antlers
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SK/SKAJI/%{dist}-v%{version}.tar.gz

# XXX syntax check fails
%define __spec_autodep_custom_pre export MOUSE_PUREPERL=1
%add_findreq_skiplist */Mouse/PurePerl.pm

# Automatically added by buildreq on Sun Oct 09 2011 (-bi)
BuildRequires: perl-HTTP-Message perl-IO-String perl-Locale-US perl-Module-Install perl-Moose perl-Package-Stash-XS perl-Params-Coerce perl-Path-Class perl-Regexp-Common perl-Test-Deep perl-Test-Output perl-autodie perl-threads perl(Module/Build/XSUtil.pm) perl(Test/Exception.pm) perl(Test/Requires.pm) perl(Test/Fatal.pm)

%description
Moose, a powerful metaobject-fuelled extension of the Perl 5 object system,
is wonderful.  Unfortunately, it's a little slow.  Though significant progress
has been made over the years, the compile time penalty is a non-starter for
some applications.  Mouse aims to alleviate this by providing a subset of
Moose's functionality, faster.

%prep
%setup -q -n %{dist}-v%{version}

%build
export XSUBPP_NO_STATIC_XS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md example
%perl_vendor_archlib/Mouse*
%perl_vendor_autolib/Mouse*
%perl_vendor_archlib/ouse.pm
%perl_vendor_archlib/Squirrel*
%perl_vendor_archlib/Test

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.10-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.10-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.9-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.8-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt1.1
- rebuild with new perl 5.24.1

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.5-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.5-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- automated CPAN update

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.02-alt1
- 0.95 -> 1.02
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- 0.93 -> 0.95
- built for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Fri Feb 25 2011 Vladimir Lettiev <crux@altlinux.ru> 0.90-alt1
- 0.88 -> 0.90
- fixed build

* Tue Jan 25 2011 Alexey Tourbin <at@altlinux.ru> 0.88-alt1
- 0.40 -> 0.88

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 0.40-alt1
- 0.40

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.39-alt1
- Initial build.
