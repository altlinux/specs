%define module_version 1.8
%define module_name FindBin-libs
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Cwd.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(FindBin.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Symbol.pm) perl(Test/More.pm) perl(lib.pm) perl(strict.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.8
Release: alt2
Summary: FindBin::libs - locate and a 'use lib' or export 
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LE/LEMBARK/%module_name-%module_version.tar.gz
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
%doc CHANGES README example
%perl_vendor_privlib/F*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2
- build for Sisyphus (required for perl update)

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1
- initial import by package builder

