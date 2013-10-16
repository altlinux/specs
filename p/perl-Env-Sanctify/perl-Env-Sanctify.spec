# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Env-Sanctify
Summary:	Lexically scoped sanctification of %%ENV
Version:	1.10
Release:	alt2_1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Env-Sanctify/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/Env-Sanctify-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Test suite
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(IO/Handle.pm)
BuildRequires:	perl(IPC/Open3.pm)
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info
# Runtime

%description
Env::Sanctify is a module that provides lexically-scoped manipulation and
sanctification of %%ENV. You can specify that it alter or add additional
environment variables or remove existing ones according to a list of matching
regexen. You can then either restore the environment back manually or let the
object fall out of scope, which automagically restores. It's useful for
manipulating the environment that forked processes and sub-processes will
inherit.

%prep
%setup -q -n Env-Sanctify-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%check
make test AUTHOR_TESTING=1 RELEASE_TESTING=1

%files
%doc Changes LICENSE README examples/
%{perl_vendor_privlib}/Env/

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_1
- Sisyphus build

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_5
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.06-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- fc import

