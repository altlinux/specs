# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(DBIx/Class/Core.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DBIx-Class-IntrospectableM2M
Version:        0.001001
Release:        alt1_6
Summary:        Introspect many-to-many shortcuts
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/DBIx-Class-IntrospectableM2M/
Source0:        http://www.cpan.org/authors/id/G/GR/GRODITI/DBIx-Class-IntrospectableM2M-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(DBIx/Class.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Because the many-to-many relationships are not real relationships, they can
not be introspected with DBIx::Class. Many-to-many relationships are
actually just a collection of convenience methods installed to bridge two
relationships. This DBIx::Class component can be used to store all relevant
information about these non-relationships so they can later be introspected
and examined.

%prep
%setup -q -n DBIx-Class-IntrospectableM2M-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.001001-alt1_1
- fc import

