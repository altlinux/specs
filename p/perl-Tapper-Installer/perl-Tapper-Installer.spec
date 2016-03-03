%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Devel/AssertOS.pm) perl(Devel/CheckOS.pm) perl(Exporter.pm) perl(File/Find/Rule.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist /usr/bin/tapper-installer-*.pl
%define upstream_name    Tapper-Installer
%define upstream_version 5.0.0

Name:       perl-%{upstream_name}
Version:    5.0.0
Release:    alt1

Summary:    Tapper - Install everything needed for a test
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-Installer-%{version}.tar.gz

BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Daemon/Daemonize.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(File/Type.pm)
BuildRequires: perl(Hash/Merge/Simple.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IO/Select.pm)
BuildRequires: perl(Linux/Personality.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
BuildRequires: perl(Socket.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Tapper/Remote/Config.pm)
BuildRequires: perl(Tapper/Remote/Net.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(YAML.pm)
BuildRequires: perl(common/sense.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(subs.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch

%global __requires_exclude /sbin/runscript
Source44: import.info

%description
A learned sage once wrote on IRC:

   $^O is stupid and ugly, it wears its pants as a hat

Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS "families" such as "Unix", which includes things like
Linux, Solaris, AIX etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

pushd %buildroot%perl_vendor_privlib/auto/Tapper/Installer/startfiles/
        rm -rf debian gentoo suse ubuntu
        sed -i -e s,portmap,rpcbind,g `grep -rl portmap .`
popd


%files
%doc Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*
/usr/bin/tapper-installer-client.pl
/usr/bin/tapper-installer-simnow.pl
/usr/share/man/man1/tapper-installer-client.pl.1*
/usr/share/man/man1/tapper-installer-simnow.pl.1*

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

