%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define fedora 20
Name:           perl-Unicode-LineBreak
Version:        2017.004
Release:        alt1.1
Summary:        UAX #14 Unicode Line Breaking Algorithm
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Unicode-LineBreak/
Source0:        http://www.cpan.org/authors/id/N/NE/NEZUMI/Unicode-LineBreak-%{version}.tar.gz
# libthai is not available (yet) on EL5 and earlier.
%if 0%{?rhel} > 5 || 0%{?fedora}
BuildRequires:  libthai-devel
%endif
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  sombok-devel
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(MIME/Charset.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests
BuildRequires:  perl(Test/More.pm)
# Optional tests
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(Encode.pm) >= 1.98
Requires:       perl(MIME/Charset.pm) >= 1.006.2


%if 0%{?rhel} == 6
%filter_from_provides /^perl.Unicode.LineBreak.pm.$/d
%filter_from_requires /^perl.Unicode.LineBreak.Constants.pm.$/d

%endif

%if 0%{?fedora} > 14 || 0%{?rhel} > 6
%{echo 
%filter_from_requires /perl.Unicode.LineBreak.Constants.pm./d
%filter_from_provides /^perl.Unicode.LineBreak.pm.$/d
}



%endif
Source44: import.info


%description
Unicode::LineBreak performs Line Breaking Algorithm described in Unicode
Standards Annex #14 [UAX #14]. East_Asian_Width informative properties
defined by Annex #11 [UAX #11] will be concerned to determine breaking
positions.


%prep
%setup -q -n Unicode-LineBreak-%{version}
# Remove bundled library
rm -rf sombok
sed -i -e '/^sombok/d' MANIFEST

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%check
make test


%files
%doc ARTISTIC Changes Changes.REL1 GPL README Todo.REL1
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Unicode*
%{perl_vendor_archlib}/Text
%{perl_vendor_archlib}/POD2

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2017.004-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2017.004-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2016.003-alt1.1
- rebuild with new perl 5.24.1

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 2016.003-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2015.12-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2015.11-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 2015.11-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2015.06-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2013.11-alt1_2.1
- rebuild with new perl 5.20.1

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 2013.11-alt1_2
- moved to Sisyphus for perl-Text-vCard

* Wed Sep 11 2013 Igor Vlasenko <viy@altlinux.ru> 2012.06-alt2_6
- rebuild

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 2012.06-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 2012.06-alt1_5
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 2012.06-alt1_4
- update to new release by fcimport

* Thu Dec 13 2012 Igor Vlasenko <viy@altlinux.ru> 2012.06-alt1_3
- update to new release by fcimport

