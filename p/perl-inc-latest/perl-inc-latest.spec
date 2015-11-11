%define module_version 0.500
%define module_name inc-latest
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/Installed.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Copy.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(IO/File.pm) perl(Test/More.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.500
Release: alt2
Summary: use modules bundled in inc/ if they are newer than installed ones
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/inc-latest

Source0: http://cpan.org.ua/authors/id/D/DA/DAGOLDEN/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/i*

%changelog
* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.500-alt2
- moved to Sisyphus

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.500-alt1
- initial import by package builder

