# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/Rad.pm) perl(Class/C3.pm) perl(Compress/Bzip2.pm) perl(Daemon/Daemonize.pm) perl(Data/DPath.pm) perl(DateTime.pm) perl(DateTime/Format/Natural.pm) perl(File/ShareDir.pm) perl(File/Slurp.pm) perl(File/Type.pm) perl(Hash/Merge/Simple.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(Kwalify.pm) perl(MRO/Compat.pm) perl(Memoize.pm) perl(Net/OpenSSH.pm) perl(Perl6/Junction.pm) perl(Socket.pm) perl(Template.pm) perl(Test/Exception.pm) perl(UNIVERSAL.pm) perl(YAML/XS.pm) perl(parent.pm) perl(subs.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper-PRC
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Control running test programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App/Daemon.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(English.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Copy.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(IO/Handle.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(IPC/Open3.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Log/Log4perl.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Installer/Base.pm)
BuildRequires: perl(Tapper/Remote/Config.pm)
BuildRequires: perl(Tapper/Remote/Net.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Try/Tiny.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(YAML.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(common/sense.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
Tapper - Program run control for test program automation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*
/usr/bin/tapper-automatic-test.pl
/usr/bin/tapper-client
/usr/share/man/man1/tapper-automatic-test.pl.1.*
/usr/share/man/man1/tapper-client.1.*



%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_2
- mageia import by cas@ requiest

