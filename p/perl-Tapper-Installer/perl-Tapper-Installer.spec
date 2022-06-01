# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Devel/AssertOS.pm) perl(Devel/CheckOS.pm) perl(File/Find/Rule.pm) perl(Test/EOL.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist /usr/bin/tapper-installer-*.pl
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Tapper-Installer
%define upstream_version 5.0.1

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Tapper - Install everything needed for a test
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://cpan.metacpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

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
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%makeinstall_std

pushd %buildroot%perl_vendor_privlib/auto/Tapper/Installer/startfiles/
        rm -rf debian gentoo suse ubuntu
        sed -i -e s,portmap,rpcbind,g `grep -rl portmap .`
popd


%files
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*
/usr/bin/tapper-installer-client.pl
/usr/bin/tapper-installer-simnow.pl
%{_mandir}/man1/tapper-installer-client.pl.1*
%{_mandir}/man1/tapper-installer-simnow.pl.1*

%changelog
* Wed Jun 01 2022 Igor Vlasenko <viy@altlinux.org> 5.0.1-alt1_1
- update by mgaimport

* Tue May 24 2022 Igor Vlasenko <viy@altlinux.org> 5.0.1-alt1
- automated CPAN update

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_1
- update by mgaimport

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

