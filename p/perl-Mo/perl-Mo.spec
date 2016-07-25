%define _unpackaged_files_terminate_build 1
%define module_version 0.40
%define module_name Mo
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/XSAccessor.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/All.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Moose.pm) perl(Mouse.pm) perl(PPI.pm) perl(Pod/Wordlist.pm) perl(Test/CPAN/Meta.pm) perl(Test/More.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl(Test/Spelling.pm) perl(YAML.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.40
Release: alt1
Summary: Micro Objects. Mo is less.
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/mo-pm

Source: http://www.cpan.org/authors/id/T/TI/TINITA/Mo-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README ReadMe.pod Changes LICENSE
%perl_vendor_privlib/M*
%perl_vendor_privlib/R*

%files scripts
%_bindir/*

%changelog
* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.39-alt2
- to Sisyphus as dependency

* Mon Sep 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- regenerated from template by package builder

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- regenerated from template by package builder

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- initial import by package builder

