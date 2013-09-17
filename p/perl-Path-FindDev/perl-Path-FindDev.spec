# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(Module/Build.pm) perl(Moo.pm) perl(Path/IsDev/Object.pm) perl(Path/Tiny.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.2.0
%define module_name Path-FindDev
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.2.0
Release: alt1
Summary: Find a development path somewhere in an upper hierarchy.
Group: Development/Perl
License: perl
URL: https://github.com/kentfredric/Path-FindDev

Source0: http://cpan.org.ua/authors/id/K/KE/KENTNL/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/P*

%changelog
* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- initial import by package builder

