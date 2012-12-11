# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Catalyst.pm) perl(Catalyst/Action.pm) perl(Config.pm) perl(Fcntl.pm) perl(FindBin.pm) perl(HTML/FormFu/Deploy.pm) perl(HTML/FormFu/MultiForm.pm) perl(HTML/FormFu/Util.pm) perl(MRO/Compat.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Locale/Maketext.pm)
Name:           perl-Catalyst-Controller-HTML-FormFu
Version:        0.09004
Release:        alt2_1
Summary:        HTML::FormFu controller for Catalyst
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Catalyst-Controller-HTML-FormFu/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CF/CFRANKS/Catalyst-Controller-HTML-FormFu-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Catalyst/Action/RenderView.pm)
BuildRequires:  perl(Catalyst/Component/InstancePerContext.pm)
BuildRequires:  perl(Catalyst/Plugin/ConfigLoader.pm)
BuildRequires:  perl(Catalyst/Plugin/Session/State/Cookie.pm)
BuildRequires:  perl(Catalyst/Plugin/Session/Store/File.pm)
BuildRequires:  perl(Catalyst/Runtime.pm)
BuildRequires:  perl(Catalyst/View/TT.pm)
BuildRequires:  perl(Config/Any.pm)
BuildRequires:  perl(Config/General.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/FormFu.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(MooseX/Attribute/Chained.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(Regexp/Assemble.pm)
BuildRequires:  perl(Task/Weaken.pm)
BuildRequires:  perl(Template.pm)
BuildRequires:  perl(Test/WWW/Mechanize.pm)
BuildRequires:  perl(Test/WWW/Mechanize/Catalyst.pm)
Requires:       perl(Catalyst/Component/InstancePerContext.pm)
Requires:       perl(Catalyst/Runtime.pm) >= 5.70
Requires:       perl(HTML/FormFu.pm) >= 0.090.070
Source44: import.info

%description
This base controller merges the functionality of HTML::FormFu with Catalyst.

%prep
%setup -q -n Catalyst-Controller-HTML-FormFu-%{version}

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
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.09004-alt2_1
- moved to Sisyphus (Tapper dep)

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.09004-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1_5
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1_3
- fc import

