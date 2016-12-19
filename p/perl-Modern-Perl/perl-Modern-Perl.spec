Serial: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Modern-Perl
Version:        1.20161005
Release:        alt1_1
Summary:        Enable all of the features of Modern Perl with one command
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Modern-Perl/
Source0:        http://www.cpan.org/authors/id/C/CH/CHROMATIC/Modern-Perl-%{version}.tar.gz
Patch0:         Modern-Perl-1.20161005-version.patch
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(autodie.pm)
BuildRequires:  perl(Module/Build.pm)
# Module Runtime
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(mro.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
# Runtime
Requires:       perl(autodie.pm) >= 2.22
Source44: import.info
Provides: perl(Modern/Perl.pm) = 2012.0

%description
Modern Perl often relies on the presence of several core and CPAN pragmas
and modules.  Wouldn't it be nice to use them all with a single command?

%prep
%setup -q -n Modern-Perl-%{version}

# Add back in the package version, needed for provides
# https://github.com/chromatic/Modern-Perl/issues/5
%patch0

%build
perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}

%check
./Build test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/Modern/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.20161005-alt1_1
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.20150127-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.20150127-alt1_3
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.20150127-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.20140107-alt1
- automated CPAN update

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.20121103-alt1_1
- update to new release by fcimport

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.20121103-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.03-alt1_7
- added provides

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121103-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_4
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_2
- fc import

