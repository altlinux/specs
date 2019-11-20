Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Compress/Zlib.pm) perl(ExtUtils/CBuilder.pm) perl(JSON.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-WWW-Mechanize-Catalyst
Summary:        Test::WWW::Mechanize for Catalyst
Version:        0.62
Release:        alt1_4
License:        GPL+ or Artistic

Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Test-WWW-Mechanize-Catalyst-%{version}.tar.gz
URL:            https://metacpan.org/release/Test-WWW-Mechanize-Catalyst
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Catalyst.pm)
# Catalyst::Plugin::Session::State::Cookie and Test::WWW::Mechanize::Catalyst
# use each other in their test suites
%if !0%{?perl_bootstrap}
BuildRequires:  perl(Catalyst/Plugin/Session/State/Cookie.pm)
%endif
BuildRequires:  perl(Catalyst/Plugin/Session/Store/Dummy.pm)
BuildRequires:  perl(Catalyst/Test.pm)
BuildRequires:  perl(Class/Load.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(HTTP/Request/Common.pm)
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(LWP.pm)
BuildRequires:  perl(MIME/Base64.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Moose/Object.pm)
BuildRequires:  perl(namespace/clean.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/utf8.pm)
BuildRequires:  perl(Test/WWW/Mechanize.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(WWW/Mechanize.pm)
BuildRequires:  sed

Requires:       perl(Catalyst.pm) >= 5.0
Requires:       perl(LWP.pm) >= 5.816
Requires:       perl(Moose.pm) >= 0.670
Requires:       perl(namespace/clean.pm) >= 0.090
Requires:       perl(Test/WWW/Mechanize.pm) >= 1.140
Requires:       perl(WWW/Mechanize.pm) >= 1.540


Source44: import.info

%description
Catalyst is an elegant MVC Web Application Framework. Test::WWW::Mechanize
is a subclass of WWW::Mechanize that incorporates features for web
application testing. The Test::WWW::Mechanize::Catalyst module meshes the
two to allow easy testing of Catalyst applications without starting up a
web server.

%prep
%setup -q -n Test-WWW-Mechanize-Catalyst-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

# silence rpmlint warning
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README t/
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1_4
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1_1
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_15
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_12
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_11
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_8
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_4
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_1
- update to new release by fcimport

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1_1
- update to new release by fcimport

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- automated CPAN update

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt2_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt2_2
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt2_1
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1_1
- update to new release by fcimport

* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_1
- fc import

