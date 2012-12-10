# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/Daemon.pm) perl(Class/C3.pm) perl(Compress/Bzip2.pm) perl(DateTime.pm) perl(DateTime/Format/Natural.pm) perl(English.pm) perl(File/ShareDir.pm) perl(File/Slurp.pm) perl(File/Type.pm) perl(Hash/Merge/Simple.pm) perl(IO/Handle.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(IPC/Open3.pm) perl(MRO/Compat.pm) perl(Memoize.pm) perl(Net/OpenSSH.pm) perl(Perl6/Junction.pm) perl(Template.pm) perl(Test/Deep.pm) perl(Test/Exception.pm) perl(Try/Tiny.pm) perl(UNIVERSAL.pm) perl(YAML.pm) perl(YAML/XS.pm) perl(common/sense.pm) perl(parent.pm) perl(subs.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Tapper-Remote
%define upstream_version 4.1.0

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Tapper - Common functionality for remote automation libs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(IO/Socket/INET.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Moose/Role.pm)
BuildRequires: perl(Net/TFTP.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Socket.pm)
BuildRequires: perl(Sys/Hostname.pm)
BuildRequires: perl(Tapper/Base.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
This module contains functions that are common for all remote Tapper projects
(currently Tapper::PRC and Tapper::Installer). Tapper::Remote itself does not
export functionality but instead is the base image for all modules of the
project.

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




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  4.1.0-alt1_2
- mageia import by cas@ requiest

