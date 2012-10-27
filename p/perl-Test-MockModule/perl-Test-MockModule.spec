# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Scalar/Util.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-MockModule
Version:        0.05
Release:        alt1_17
Summary:        Override subroutines in a module for unit testing
Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-MockModule/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SI/SIMONFLK/Test-MockModule-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl(CGI.pm)
BuildRequires:  perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
%{summary}.

%prep
%setup -q -n Test-MockModule-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Test


%changelog
* Sat Oct 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_17
- picked up by robot, thanks to enp@

* Fri Oct 26 2012 Eugene Prokopiev <enp@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

