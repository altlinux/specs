# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Test/More.pm) perl(Test/Settings.pm)
# END SourceDeps(oneline)
%define module_version 0.004
%define module_name Test-DescribeMe
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.004
Release: alt2
Summary: Tell test runners what kind of test you are
Group: Development/Perl
License: perl
URL: https://github.com/wolfsage/Test-DescribeMe

Source0: http://cpan.org.ua/authors/id/W/WO/WOLFSAGE/%module_name-%module_version.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
* Thu Apr 10 2025 Igor Vlasenko <viy@altlinux.org> 0.004-alt2
- to Sisyphus as Array-Iterator dep

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- initial import by package builder

