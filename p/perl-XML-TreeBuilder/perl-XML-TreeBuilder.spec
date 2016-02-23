%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl(Test.pm) perl-devel perl-podlators perl(XML/Catalog.pm)
# END SourceDeps(oneline)
Summary:	Parser that builds a tree of XML::Element objects
Name:		perl-XML-TreeBuilder
Version:	5.4
Release:	alt1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/XML-TreeBuilder/
Source:		http://www.cpan.org/authors/id/J/JF/JFEARN/XML-TreeBuilder-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:	perl(HTML/Element.pm)
BuildRequires:	perl(HTML/Tagset.pm)
BuildRequires:	perl(XML/Parser.pm)
Requires:	perl(HTML/Element.pm) >= 4.1 perl(HTML/Tagset.pm) perl(XML/Parser.pm)
Source44: import.info

%description
perl-XML-TreeBuilder is a Perl module that implements a parser
that builds a tree of XML::Element objects.

%prep
%setup -q -n XML-TreeBuilder-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT create_packlist=0

### Clean up buildroot
find $RPM_BUILD_ROOT -name .packlist -exec %{__rm} {} \;

%files
%doc Changes README
%{perl_vendor_privlib}/XML/

%changelog
* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.3-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_9
- update to new release by fcimport

* Thu Jan 10 2013 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_8
- initial fc import

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.09-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Oct 17 2008 Artem Zolochevskiy <azol@altlinux.ru> 3.09-alt3
- enhanced Fedora patch (perl-XML-TreeBuilder-3.09-11.fc9.src.rpm):
  + Add ErrorContext pass through
  + Fix crash on Entity declaration. (RH #461557)

* Wed Oct 08 2008 Artem Zolochevskiy <azol@altlinux.ru> 3.09-alt2
- applied Fedora patch to allow entities to pass thru un-expanded

* Tue Oct 07 2008 Artem Zolochevskiy <azol@altlinux.ru> 3.09-alt1
- initial build for Sisyphus

