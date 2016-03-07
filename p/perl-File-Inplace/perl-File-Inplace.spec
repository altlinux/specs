# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(IO/File.pm) perl(IO/Handle.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Inplace
Version:        0.20
Release:        alt2_14
Summary:        Perl module for in-place editing of files
License:        (GPL+ or Artistic)
Group:          Development/Perl
URL:            http://search.cpan.org/dist/File-Inplace/
Source0:        http://www.cpan.org/modules/by-module/File/File-Inplace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
File::Inplace is a perl module intended to ease the common task of editing
a file in-place. Inspired by variations of perl's -i option, this module is
intended for somewhat more structured and reusable editing than command
line perl typically allows. File::Inplace endeavors to guarantee file
integrity; that is, either all of the changes made will be saved to the
file, or none will. It also offers functionality such as backup creation,
automatic field splitting per-line, automatic chomping/unchomping, and
aborting edits partially through without affecting the original file.

%prep
%setup -q -n File-Inplace-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_13
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_8
- update to new release by fcimport

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_7
- build for Sisyphus

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_6
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_4
- fc import

