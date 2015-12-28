# BEGIN SourceDeps(oneline):
BuildRequires: perl(AutoLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(Sys/Hostname.pm) perl(Test.pm) perl(Time/HiRes.pm)
# END SourceDeps(oneline)
%define module_version 0.12
%define module_name Data-Uniqid
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.12
Release: alt2
Summary: Perl extension for simple genrating of unique id's
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MW/MWX/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Data::Uniqid provides three simple routines for generating unique ids..These ids are coded with a Base62 systen to make them short and handy
(e.g. to use it as part of a URL).

  suinqid
    genrates a very short id valid only for the localhost and with a 
    liftime of 1 day
  
  uniqid
    generates a short id valid on the local host 

  luniqid 
    generates a long id valid everywhere and ever



%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/D*
%perl_vendor_privlib/auto/*
%changelog
* Mon Dec 28 2015 Lenar Shakirov <snejok@altlinux.ru> 0.12-alt2
- build for Sisyphus

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

