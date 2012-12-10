# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Catalyst/Controller.pm) perl(Catalyst/ScriptRunner.pm) perl(Config.pm) perl(Encode.pm) perl(Fcntl.pm) perl(HTML/Entities.pm) perl(HTTP/Request/Common.pm) perl(IO/Socket/INET.pm) perl(MIME/Base64.pm) perl(URI.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-WWW-Mechanize-Catalyst
Summary:        Test::WWW::Mechanize for Catalyst
Version:        0.58
Release:        alt2_1
License:        GPL+ or Artistic
Group:          Development/Perl
Source0:        http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Test-WWW-Mechanize-Catalyst-%{version}.tar.gz
URL:            http://search.cpan.org/dist/Test-WWW-Mechanize-Catalyst/
BuildArch:      noarch

BuildRequires:  perl(Catalyst.pm)
# Catalyst::Plugin::Session::State::Cookie and Test::WWW::Mechanize::Catalyst
# use each other in their test suites
%if !0%{?perl_bootstrap}
BuildRequires:  perl(Catalyst/Plugin/Session/State/Cookie.pm)
%endif
BuildRequires:  perl(Catalyst/Plugin/Session/Store/Dummy.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(LWP.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(namespace/clean.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/utf8.pm)
BuildRequires:  perl(Test/WWW/Mechanize.pm)
BuildRequires:  perl(WWW/Mechanize.pm)

Requires:       perl(Catalyst.pm) >= 5.00
Requires:       perl(LWP.pm) >= 5.816
Requires:       perl(Moose.pm) >= 0.67
Requires:       perl(namespace/clean.pm) >= 0.09
Requires:       perl(Test/WWW/Mechanize.pm) >= 1.14
Requires:       perl(WWW/Mechanize.pm) >= 1.54

# obsolete/provide old tests subpackage
# can be removed during F19 development cycle
Obsoletes:      %{name}-tests < 0.56-3
Provides:       %{name}-tests = %{version}-%{release}


Source44: import.info

%description
Catalyst is an elegant MVC Web Application Framework. Test::WWW::Mechanize
is a subclass of WWW::Mechanize that incorporates features for web
application testing. The Test::WWW::Mechanize::Catalyst module meshes the
two to allow easy testing of Catalyst applications without starting up a
web server.

%prep
%setup -q -n Test-WWW-Mechanize-Catalyst-%{version}

# silence rpmlint warning
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc CHANGES README t/
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt2_1
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1_1
- update to new release by fcimport

* Sat May 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_1
- fc import

