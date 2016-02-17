# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Sub/Exporter/Util.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
BuildRequires: /proc
%define upstream_name    Daemon-Daemonize
%define upstream_version 0.0052

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_7

Summary:    An easy-to-use daemon(izing) toolkit
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Daemon/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Path/Class.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Test/Most.pm)
BuildArch: noarch
Source44: import.info

%description
Daemon::Daemonize is a toolkit for daemonizing processes and checking up on
them. It takes inspiration from the
http://www.clapper.org/software/daemonize/ manpage, the MooseX::Daemon
manpage, the Net::Server::Daemon manpage

A note about the 'close' option
    If you're having trouble with IPC in a daemon, try closing only STD*
    instead of everything:

        daemonize( ..., close => std, ... )

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%perl_vendor_privlib/*




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.0052-alt1_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.0052-alt1_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.0052-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.0052-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.0052-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.0052-alt1_1
- mageia import by cas@ requiest

