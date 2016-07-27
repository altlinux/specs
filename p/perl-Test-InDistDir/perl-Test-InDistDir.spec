# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Test-InDistDir
%define upstream_version 1.112071

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_7

Summary:    Test environment setup for development with IDE
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(Test/More.pm)
BuildArch: noarch
Source44: import.info

%description
This module helps run test scripts in IDEs like Komodo.

When running test scripts in an IDE i have to set up a project file
defining the dist dir to run tests in and a lib dir to load additional
modules from. Often I didn't feel like doing that, especially when i only
wanted to do a small patch to a dist. In those cases i added a BEGIN block
to mangle the environment for me.

This module basically is that BEGIN block. It automatically moves up one
directory when it cannot see the test script in "t/$scriptname" and
includes 'lib' in @INC when there's no blib present. That way the test ends
up with almost the same environment it'd get from EUMM/prove/etc., even
when it's actually run inside the t/ directory.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json
%perl_vendor_privlib/*




%changelog
* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt2_7
- update by mgaimport

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt2_6.1
- to Sisyphus

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt2_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.112071-alt2_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.112071-alt1_1
- converted for ALT Linux by srpmconvert tools

