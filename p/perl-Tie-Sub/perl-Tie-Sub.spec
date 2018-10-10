# BEGIN SourceDeps(oneline):
BuildRequires: perl(English.pm) perl(Params/Validate.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/NoWarnings.pm)
# END SourceDeps(oneline)
%define module_version 1.001
%define module_name Tie-Sub
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.001
Release: alt1.1
Summary: Tie::Sub - Tying a subroutine, function or method to a hash
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/ST/STEFFENW/%module_name-%module_version.tar.gz
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
%doc Changes README example
%perl_vendor_privlib/T*

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1.1
- to Sisyphus as perl-Graphics-ColorNames dependency

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- initial import by package builder

