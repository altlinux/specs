Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Locale/Maketext.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Catalyst-Controller-HTML-FormFu
Version:        2.04
Release:        alt1_6
Summary:        HTML::FormFu controller for Catalyst
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Catalyst-Controller-HTML-FormFu
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIGELM/Catalyst-Controller-HTML-FormFu-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
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
Requires:       perl(HTML/FormFu.pm) >= 2.060
Requires:       perl(MooseX/Attribute/Chained.pm) >= 1.0.1
# Task::Weaken for Scalar::Util, see Makefile.PL
Requires:       perl(Task/Weaken.pm)
Source44: import.info
%filter_from_requires /^perl(\(HTML.FormFu\|MooseX.Attribute.Chained\).pm)/d

%description
This base controller merges the functionality of HTML::FormFu with Catalyst.

# Filter unde-specified dependencies


%prep
%setup -q -n Catalyst-Controller-HTML-FormFu-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1_6
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1_2
- update to new release by fcimport

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1_1
- update to new release by fcimport

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1_2
- update to new release by fcimport

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

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

