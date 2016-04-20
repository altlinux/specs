%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build.pm) perl(Test/More.pm) perl(if.pm) perl(parent.pm) perl(Test/Requires.pm)
# END SourceDeps(oneline)
%define module_version 0.05
%define module_name Cwd-Guard
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt1
Summary: Temporary changing working directory (chdir)
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Cwd-Guard

Source: http://www.cpan.org/authors/id/K/KA/KAZEBURO/Cwd-Guard-%{version}.tar.gz
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
%doc README.md Changes LICENSE
%perl_vendor_privlib/C*

%changelog
* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed May 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- moved to Sisyphus as dependency

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

