# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Log-Any-Adapter
Version:        0.11
Release:        alt2_4
Summary:        Tell Log::Any where to send its logs
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Log-Any-Adapter/
Source0:        http://www.cpan.org/authors/id/J/JS/JSWARTZ/Log-Any-Adapter-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Devel/GlobalDestruction.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Guard.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(Log/Any.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info


%description
The Log-Any-Adapter distribution implements Log::Any class methods to
specify where logs should be sent. It is a separate distribution so as to
keep Log::Any itself as simple and unchanging as possible.

%prep
%setup -q -n Log-Any-Adapter-%{version}

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
* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2_4
- Sisyphus build; switch to fc import

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.11-alt2_2
- rebuild to get rid of unmets

* Sat Aug 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- mgaimport update

