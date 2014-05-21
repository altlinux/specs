# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build.pm) perl(Test/More.pm) perl(if.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name Cwd-Guard
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt2
Summary: Temporary changing working directory (chdir)
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Cwd-Guard

Source0: http://cpan.org.ua/authors/id/K/KA/KAZEBURO/%module_name-%module_version.tar.gz
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
* Wed May 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- moved to Sisyphus as dependency

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

