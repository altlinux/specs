# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Plack-Test-ExternalServer
Version:        0.01
Release:        alt3_5
Summary:        Run HTTP tests on external live servers
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Plack-Test-ExternalServer/
Source0:        http://www.cpan.org/authors/id/F/FL/FLORA/Plack-Test-ExternalServer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTTP/Request/Common.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(Plack/Loader.pm)
BuildRequires:  perl(Plack/Test.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/TCP.pm)
BuildRequires:  perl(URI.pm)
# additional deps for "release" testing
%if !0%{?perl_bootstrap}
BuildRequires:  perl(Pod/Coverage/TrustPod.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif
Requires:       perl(Plack/Test.pm)


Source44: import.info

%description
This module allows you to run your Plack::Test tests against an external
server instead of just against a local application through either mocked
HTTP or a locally spawned server.

%prep
%setup -q -n Plack-Test-ExternalServer-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;


%check
RELEASE_TESTING=1 make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt3_5
- sisyphus release

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_5
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_2
- fc import

