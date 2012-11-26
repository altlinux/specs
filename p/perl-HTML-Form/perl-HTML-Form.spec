# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Encode.pm) perl(LWP/UserAgent.pm) perl(Test.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-Form
Version:        6.03
Release:        alt1_3
Summary:        Class that represents an HTML form element
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-Form/
Source0:        http://www.cpan.org/authors/id/G/GA/GAAS/HTML-Form-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/TokeParser.pm)
BuildRequires:  perl(HTTP/Request.pm)
BuildRequires:  perl(HTTP/Request/Common.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
Requires:       perl(HTML/TokeParser.pm)
Requires:       perl(HTTP/Request.pm) >= 6
Requires:       perl(HTTP/Request/Common.pm) >= 6


Source44: import.info

%description
Objects of the HTML::Form class represents a single HTML <form> ... </form>
instance. A form consists of a sequence of inputs that usually have names,
and which can take on various values. The state of a form can be tweaked
and it can then be asked to provide HTTP::Request objects that can be
passed to the request() method of LWP::UserAgent.

%prep
%setup -q -n HTML-Form-%{version}

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
* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_3
- fixed build by auto update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1
- automated CPAN update

* Sat Mar 10 2012 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- 6.00 -> 6.02

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
