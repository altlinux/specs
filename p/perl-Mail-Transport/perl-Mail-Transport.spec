%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Errno.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/Lines.pm) perl(IO/Socket.pm) perl(List/Util.pm) perl(Mail/Reporter.pm) perl(Net/SMTP.pm)
# END SourceDeps(oneline)
%define module_name Mail-Transport
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.002
Release: alt1
Summary: Email message exchange
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
=== README for Mail-Transport version 3.000
=   Generated on Thu Feb  2 15:40:56 2017 by OODoc 2.02

There are various ways to install this module:

 (1) if you have a command-line, you can do:
       perl -MCPAN -e 'install <any package from this distribution>'

 (2) if you use Windows, have a look at http://ppm.activestate.com/

 (3) if you have downloaded this module manually (as root/administrator)
       gzip -d Mail-Transport-3.000.tar.gz
       tar -xf Mail-Transport-3.000.tar

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README ChangeLog README.md
%perl_vendor_privlib/M*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 3.002-alt1
- automated CPAN update

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 3.001-alt1
- automated CPAN update

* Thu Sep 28 2017 Igor Vlasenko <viy@altlinux.ru> 3.000-alt1
- to Sisyphus

