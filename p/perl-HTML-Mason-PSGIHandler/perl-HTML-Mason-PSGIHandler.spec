# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(FindBin.pm) perl(HTML/Mason/CGIHandler.pm) perl(HTML/Mason/Exceptions.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-Mason-PSGIHandler
Version:        0.52
Release:        alt1_6
Summary:        PSGI handler for HTML::Mason
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-Mason-PSGIHandler/
Source0:        http://www.cpan.org/authors/id/A/AB/ABH/HTML-Mason-PSGIHandler-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(CGI/PSGI.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/Mason.pm)
BuildRequires:  perl(Plack/Test.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
HTML::Mason::PSGIHandler is a PSGI handler for HTML::Mason. It's based on
HTML::Mason::CGIHandler and allows you to process Mason templates on any
web servers that support PSGI.

%prep
%setup -q -n HTML-Mason-PSGIHandler-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_6
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_4
- fc import

