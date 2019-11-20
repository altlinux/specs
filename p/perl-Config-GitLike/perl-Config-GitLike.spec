Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(ExtUtils/CBuilder.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Moose.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Config-GitLike
Version:        1.17
Release:        alt1_8
Summary:        Git-compatible config file parsing
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Config-GitLike
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXMV/Config-GitLike-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(File/Copy.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Module/Install/ExtraTests.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(MooX/Types/MooseLike/Base.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  sed


Source44: import.info

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

%prep
%setup -q -n Config-GitLike-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_8
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_4
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_2
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_6
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Mon Dec 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_4
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_1
- fc import

