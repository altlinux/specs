%define module_version 1.4
%define module_name Devel-Caller-Perl
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.4
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/C/CW/CWEST/%module_name-%module_version.tar.gz
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
%doc README
%perl_vendor_privlib/D*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2
- build for Sisyphus (required for perl update)

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- initial import by package builder

