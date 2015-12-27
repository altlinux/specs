# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Digest/MD5.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(FileHandle.pm) perl(HTTP/Date.pm) perl(HTTP/Request.pm) perl(HTTP/Request/Common.pm) perl(HTTP/Status.pm) perl(IO/Socket/UNIX.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Plack/HTTPParser.pm) perl(Plack/Runner.pm) perl(Plack/TempBuffer.pm) perl(Plack/Test/Suite.pm) perl(Plack/Util.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Time/HiRes.pm) perl(Try/Tiny.pm) perl(YAML/Tiny.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Starlet
Version:        0.28
Release:        alt1_1
Summary:        Simple, high-performance PSGI/Plack HTTP server
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Starlet/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  /usr/bin/start_server
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(Net/EmptyPort.pm)
BuildRequires:  perl(Parallel/Prefork.pm)
BuildRequires:  perl(Plack.pm)
BuildRequires:  perl(Plack/Loader.pm)
BuildRequires:  perl(Plack/Test.pm)
BuildRequires:  perl(Server/Starter.pm)
BuildRequires:  perl(Socket.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/TCP.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

# Eliminate inc/*
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/ReadmeFromPod.pm)
Source44: import.info


%description
Starlet is a standalone HTTP/1.0 server with support for keep-alive, prefork,
graceful shutdown, hot deploy, fast HTTP processing, and is suitable for
running HTTP application servers behind a reverse proxy.

%prep
%setup -q -n Starlet-%{version}

# Remove bundled modules
for f in $(find inc/Module -name *.pm); do
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

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_1
- update to new release by fcimport

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_3
- update to new release by fcimport

* Wed Jul 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_2
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_1
- import for Sisyphus (required for RT)

* Tue Jan 15 2013 Andrew Kornilov <hiddenman@altlinux.ru> 0.16-alt1
- initial build for ALT Linux Sisyphus

