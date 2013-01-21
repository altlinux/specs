# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Errno.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(IO/Handle.pm) perl(IO/Seekable.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Parallel-Scoreboard
Version:        0.03
Release:        alt3_7
Summary:        Scoreboard for monitoring status of many processes
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Parallel-Scoreboard/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Parallel-Scoreboard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Class/Accessor/Lite.pm)
BuildRequires:  perl(HTML/Entities.pm)
BuildRequires:  perl(JSON.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Digest/MD5.pm)

Requires:       perl(Class/Accessor/Lite.pm) >= 0.05
# Filter out unversioned R: perl(Class::Accessor::Lite)

Source44: import.info
%filter_from_requires /^^perl\\(Class::Accessor::Lite\\)/d

%description
Parallel::Scoreboard is a pure-perl implementation of a process scoreboard.
By using the module it is easy to create a monitor for many worker process,
like the status module of the Apache HTTP server.

%prep
%setup -q -n Parallel-Scoreboard-%{version}
# Remove bundled modules
for f in inc/Test/More.pm inc/File/Temp.pm; do
  pat=$(echo "$f" | sed 's,/,\\/,g;s,\.,\\.,g')
  rm $f
  sed -i -e "/$pat/d" MANIFEST
done

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
* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_7
- import for Sisyphus (required for RT)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_7
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_5
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_5
- fc import

