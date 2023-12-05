%define _unpackaged_files_terminate_build 1
%define module_name Array-Iterator
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(blib.pm) perl-devel
# END SourceDeps(oneline)
%define upstream_name    Array-Iterator
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    0.132
Release:    alt1

Summary:    A subclass of Array::Iterator to allow forwards and backwards iteration
License:    perl
Group:      Development/Perl
URL:        http://search.cpan.org/dist/Array-Iterator/
Source0:    http://www.cpan.org/authors/id/P/PE/PERLANCAR/%{module_name}-%{version}.tar.gz

BuildRequires: perl(Capture/Tiny.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test/Exception.pm)
BuildArch:  noarch
Source44: import.info

%description
This class provides a very simple iterator interface. It is
uni-directional and can only be used once. It provides no means of
reversing or resetting the iterator. It is not recommended to alter the
array during iteration, however no attempt is made to enforce this
(although I will if I can find an efficient means of doing so). This class
only intends to provide a clear and simple means of generic iteration,
nothing more (yet).

%prep
%setup -q -n %{module_name}-%{version}

%build
# %%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

# ./Build
make

%check
# ./Build test
make test

%install
# ./Build install destdir=%%{buildroot}
%makeinstall_std

%files
%doc README Changes
%perl_vendor_privlib/*


%changelog
* Tue Dec 05 2023 Igor Vlasenko <viy@altlinux.org> 0.132-alt1
- automated CPAN update

* Tue Oct 05 2021 Igor Vlasenko <viy@altlinux.org> 0.131-alt1
- automated CPAN update

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0.130-alt1
- automated CPAN update

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt3
- to Sisyphus as dep for Devel-PerlySense

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_3
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.11-alt2_2
- rebuild to get rid of unmets

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- mga update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- mga update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- converted for ALT Linux by srpmconvert tools

