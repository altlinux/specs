Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-MooseX-AttributeHelpers
Version:        0.23
Release:        alt3_11
Summary:        Extended Moose attribute interfaces
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/MooseX-AttributeHelpers/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/MooseX-AttributeHelpers-%{version}.tar.gz
# Perl 5.18 compatibility, CPAN RT#81564
Patch0:         MooseX-AttributeHelpers-0.23-Fix-tests-to-cope-radnomized-hash-keys.patch
BuildArch:      noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Moose.pm)
BuildRequires:  perl(Test/More.pm)

### auto-added reqs!
Requires:  perl(Moose.pm) >= 0.56


Source44: import.info

%description
While Moose attributes provide you with a way to name your accessors,
readers, writers, clearers and predicates, this library provides commonly
used attribute helper methods for more specific types of data.

%prep
%setup -q -n MooseX-AttributeHelpers-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog README t/
%{perl_vendor_privlib}/*

%changelog
* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt3_11
- moved to Sisyphus as dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_11
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_8
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_6
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6
- fc import

* Mon Dec 15 2008 Michael Bochkaryov <misha@altlinux.ru> 0.14-alt1
- 0.14 version

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.11-alt1
- first build for ALT Linux Sisyphus

