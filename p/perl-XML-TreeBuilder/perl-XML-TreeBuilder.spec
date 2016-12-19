# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Summary:	Parser that builds a tree of XML::Element objects
Name:		perl-XML-TreeBuilder
Version:	5.4
Release:	alt1_6
License:	GPL+ or Artistic
Group:		Development/Other
URL:		http://search.cpan.org/dist/XML-TreeBuilder/
# have to:
#  push the patch upstream
Source:		http://www.cpan.org/modules/by-module/XML/XML-TreeBuilder-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(HTML/Element.pm)
BuildRequires:	perl(HTML/Tagset.pm)
BuildRequires:	perl(Module/Build.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Test/Perl/Critic.pm)
BuildRequires:	perl(vars.pm)
BuildRequires:	perl(warnings.pm)
BuildRequires:	perl(XML/Catalog.pm)
BuildRequires:	perl(XML/Parser.pm)
Source44: import.info

%description
perl-XML-TreeBuilder is a Perl module that implements a parser
that builds a tree of XML::Element objects.

%prep
%setup -q -n XML-TreeBuilder-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%check
./Build test

%install
./Build pure_install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'

%files
%doc Changes README
%{perl_vendor_privlib}/XML/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1_6
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.4-alt1_5
- update to new release by fcimport

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

