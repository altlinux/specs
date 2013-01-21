# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(HTTP/Date.pm) perl(HTTP/Request/Common.pm) perl(HTTP/Status.pm) perl(IO/Socket/INET.pm) perl(LWP/UserAgent.pm) perl(List/Util.pm) perl(Plack/HTTPParser.pm) perl(Plack/Loader.pm) perl(Plack/Runner.pm) perl(Plack/TempBuffer.pm) perl(Plack/Test.pm) perl(Plack/Test/Suite.pm) perl(Plack/Util.pm) perl(Socket.pm) perl(Time/HiRes.pm) perl(Try/Tiny.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Starlet
Version:        0.16
Release:        alt2_1
Summary:        Simple, high-performance PSGI/Plack HTTP server
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Starlet/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Starlet-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  /usr/bin/start_server
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Parallel/Prefork.pm)
BuildRequires:  perl(Plack.pm)
BuildRequires:  perl(Server/Starter.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/TCP.pm)
Source44: import.info

%description
Starlet is a standalone HTTP/1.0 server with support for keep-alive, prefork,
graceful shutdown, hot deploy, fast HTTP processing, and is suitable for
running HTTP application servers behind a reverse proxy.

%prep
%setup -q -n Starlet-%{version}

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
* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_1
- import for Sisyphus (required for RT)

* Tue Jan 15 2013 Andrew Kornilov <hiddenman@altlinux.ru> 0.16-alt1
- initial build for ALT Linux Sisyphus

