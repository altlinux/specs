Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Regexp-Common-net-CIDR
Version:        0.03
Release:        alt1_3
Summary:        Provide patterns for CIDR blocks
License:        GPLv2

URL:            http://search.cpan.org/dist/Regexp-Common-net-CIDR/
Source0:        http://www.cpan.org/authors/id/B/BP/BPS/Regexp-Common-net-CIDR-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(Regexp/Common.pm)
Source44: import.info

%description
Patterns for CIDR blocks.

Now only next IPv4 formats are supported:
  xxx.xxx/xx
  xxx.xxx.xxx/xx
  xxx.xxx.xxx.xxx/xx

%prep
%setup -q -n Regexp-Common-net-CIDR-%{version}

# Remove bundled modules
for f in $(find inc/Module -name *.pm); do
  pat=$(echo "$f" | sed 's,/,\\/,g;s,\.,\\.,g')
  rm $f
  sed -i -e "/$pat/d" MANIFEST
done

%build
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing
# missing modules
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_6
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- fc import

