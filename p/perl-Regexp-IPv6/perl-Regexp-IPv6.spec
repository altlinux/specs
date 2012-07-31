# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Regexp-IPv6
Version:        0.03
Release:        alt1_6
Summary:        Regular expression for IPv6 addresses
License:        GPLv2+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Regexp-IPv6/
Source0:        http://www.cpan.org/authors/id/S/SA/SALVA/Regexp-IPv6-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This module exports the $IPv6_re regular expression that matches any valid
IPv6 address as described in "RFC 2373 - 2.2 Text Representation of
Addresses" but ::. Any string not compliant with such RFC will be rejected.

%prep
%setup -q -n Regexp-IPv6-%{version}

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
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_6
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_4
- fc import

