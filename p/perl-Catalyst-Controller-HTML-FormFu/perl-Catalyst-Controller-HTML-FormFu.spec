Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Aggregate/Nested.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Locale/Maketext.pm)
Name:           perl-Catalyst-Controller-HTML-FormFu
Version:        1.00
Release:        alt1_5
Summary:        HTML::FormFu controller for Catalyst
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Catalyst-Controller-HTML-FormFu/
Source0:        http://search.cpan.org/CPAN/authors/id/C/CF/CFRANKS/Catalyst-Controller-HTML-FormFu-%{version}.tar.gz
# Do not use Test::Aggregate::Nested for running tests, bug #1231204
Patch0:         Catalyst-Controller-HTML-FormFu-1.00-Execute-tests-recusively-under-t.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Catalyst/Action.pm)
BuildRequires:  perl(Catalyst/Component/InstancePerContext.pm)
BuildRequires:  perl(Catalyst/Controller.pm)
# This is a plug-in for Catalyst::Runtime
BuildRequires:  perl(Catalyst/Runtime.pm)
BuildRequires:  perl(Config/Any.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(HTML/FormFu.pm)
BuildRequires:  perl(HTML/FormFu/Deploy.pm)
BuildRequires:  perl(HTML/FormFu/MultiForm.pm)
BuildRequires:  perl(HTML/FormFu/Util.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(MooseX/Attribute/Chained.pm)
BuildRequires:  perl(MRO/Compat.pm)
BuildRequires:  perl(namespace/autoclean.pm)
BuildRequires:  perl(Regexp/Assemble.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
# Task::Weaken for Scalar::Util, see Makefile.PL
BuildRequires:  perl(Task/Weaken.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Catalyst.pm)
BuildRequires:  perl(Catalyst/Action/RenderView.pm)
BuildRequires:  perl(Catalyst/Plugin/ConfigLoader.pm)
BuildRequires:  perl(Catalyst/Plugin/Session.pm)
BuildRequires:  perl(Catalyst/Plugin/Session/State/Cookie.pm)
BuildRequires:  perl(Catalyst/Plugin/Session/Store/File.pm)
BuildRequires:  perl(Catalyst/View/TT.pm)
# Test::Aggregate::Nested disabled
# Config::General not used
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
# Template not used
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/WWW/Mechanize/Catalyst.pm)
# Test::WWW::Mechanize 1.16 for post_ok()
BuildRequires:  perl(Test/WWW/Mechanize.pm)
Requires:       perl(Catalyst/Component/InstancePerContext.pm)
Requires:       perl(Catalyst/Controller.pm)
Requires:       perl(Catalyst/Runtime.pm) >= 5.710.010
Requires:       perl(HTML/FormFu.pm) >= 1.00
Requires:       perl(MooseX/Attribute/Chained.pm) >= 1.0.1
# Task::Weaken for Scalar::Util, see Makefile.PL
Requires:       perl(Task/Weaken.pm)
Source44: import.info
%filter_from_requires /^perl\\((HTML.FormFu|MooseX.Attribute.Chained).pm\\)$/d

%description
This base controller merges the functionality of HTML::FormFu with Catalyst.

# Filter unde-specified dependencies


%prep
%setup -q -n Catalyst-Controller-HTML-FormFu-%{version}
%patch0 -p1
# Do not use Test::Aggregate::Nested for running tests, bug #1231204
rm t/aggregate.t
sed -i -e '/^t\/aggregate\.t/d' MANIFEST
mv t-aggregate/* t
find t -type f -exec sed -i -e 's|\<t-aggregate\>|t|' {} +
sed -i -e 's|^t-aggregate/|t/|' MANIFEST

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
%doc LICENSE
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_5
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_1
- update to new release by fcimport

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.09004-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.09004-alt2_2
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.09004-alt2_1
- moved to Sisyphus (Tapper dep)

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.09004-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1_5
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.09003-alt1_3
- fc import

