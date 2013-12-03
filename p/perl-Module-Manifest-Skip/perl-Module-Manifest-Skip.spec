# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Data/Dumper.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(IO/All.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(YAML/Tiny.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Module-Manifest-Skip
Version:        0.17
Release:        alt2_3
Summary:        MANIFEST.SKIP Manangement for Modules
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Module-Manifest-Skip/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Module-Manifest-Skip-%{version}.tar.gz
BuildArch:      noarch
# Bundled Module::Install does not more than EU::MM and few perl-only modules
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(File/ShareDir.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Moo.pm)
# Tests:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Test/More.pm)
Requires:       perl(File/ShareDir.pm)
Requires:       perl(File/Spec.pm)
Source44: import.info

%description
CPAN module authors use a MANIFEST.SKIP file to exclude certain well known
files from getting put into a generated MANIFEST file, which would cause them
to go into the final distribution package.

The packaging tools try to automatically skip things for you, but if you add
one of your own entries, you have to add all the common ones yourself.  This
module attempts to make all of this boring process as simple and reliable as
possible.


%prep
%setup -q -n Module-Manifest-Skip-%{version}
# XXX: Do not unbundle build-time modules to break dependency cycle on
# Module::Package and because upstream uses old 'name' attribute.

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
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2_3
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_3
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_2
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- fc import

