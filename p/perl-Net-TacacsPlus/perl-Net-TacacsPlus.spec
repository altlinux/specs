# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp/Clan.pm) perl(Class/Accessor/Fast.pm) perl(Digest/MD5.pm) perl(English.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(FindBin.pm) perl(IO/Socket.pm) perl(Pod/Usage.pm) perl(Test/Differences.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.10
%define module_name Net-TacacsPlus
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.10
Release: alt2
Summary: Tacacs+ library
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DO/DOUGDUDE/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/N*

%changelog
* Wed Feb 12 2025 Andrew A. Vasilyev <andy@altlinux.org> 1.10-alt2
- build for Sisyphus

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- initial import by package builder

