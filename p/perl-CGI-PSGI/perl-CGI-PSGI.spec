# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CGI/Util.pm) perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(IO/Handle.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-CGI-PSGI
Version:        0.15
Release:        alt1_5
Summary:        Enable your CGI.pm aware applications to adapt PSGI protocol
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/CGI-PSGI/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/CGI-PSGI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(CGI.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
This module is for web application framework developers who currently uses
CGI to handle query parameters. You can switch to use CGI::PSGI instead of
CGI, to make your framework compatible to PSGI with a slight modification
of your framework adapter. The framework should already be collecting the
body content to print at one place, and not printing any content directly
to STDOUT.

%prep
%setup -q -n CGI-PSGI-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_5
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- fc import

