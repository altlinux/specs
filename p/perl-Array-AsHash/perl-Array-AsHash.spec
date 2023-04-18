# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Clone.pm) perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.32
%define module_name Array-AsHash
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.32
Release: alt2
Summary: Treat arrays as a hashes, even if you need references for keys.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/O/OV/OVID/%module_name-%module_version.tar.gz
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
%doc Changes README
%perl_vendor_privlib/A*

%changelog
* Tue Apr 18 2023 Igor Vlasenko <viy@altlinux.org> 0.32-alt2
- to Sisyphus as perl-User-Identity dep

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- initial import by package builder

