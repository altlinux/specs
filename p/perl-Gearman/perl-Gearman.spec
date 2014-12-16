# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(FindBin.pm) perl(IO/Socket/INET.pm) perl(List/Util.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Storable.pm) perl(Time/HiRes.pm) perl(base.pm) perl(fields.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/Gearman/Task.pm
Name:           perl-Gearman
Version:        1.12
Release:        alt1
Summary:        Distributed job system
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://danga.com/gearman/
Source:        http://www.cpan.org/authors/id/D/DO/DORMANDO/Gearman-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(String/CRC32.pm)
Source44: import.info


%description
Gearman is a system to farm out work to other machines,
dispatching function calls to machines that are better suited to do work,
to do work in parallel, to load balance lots of function calls,
or to call functions between languages.

%prep
%setup -q -n Gearman-%{version}

# Filter double proved for Gearman::Client:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
  sed -e '/^perl(Gearman::Client)$/d'
EOF

%define __perl_provides %{_builddir}/Gearman-%{version}/%{name}-prov
chmod +x %{__perl_provides}


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
%doc CHANGES HACKING TODO
%{perl_vendor_privlib}/Gearman

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_11
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2_10
- build for Sisyphus (required for perl update)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_9
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_7
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_5
- fc import

