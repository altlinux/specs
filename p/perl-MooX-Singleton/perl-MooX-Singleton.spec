# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build.pm) perl(Moo.pm) perl(Role/Tiny.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.20
%define module_name MooX-Singleton
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.20
Release: alt2
Summary: turn your Moo class into singleton
Group: Development/Perl
License: perl
URL: http://search.cpan.org/dist/MooX-Singleton

Source0: http://cpan.org.ua/authors/id/A/AJ/AJGB/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Moo extension - Role::Tiny role that provides "instance"
method turning your object into singleton.

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/M*

%changelog
* Thu Aug 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.20-alt2
- Sisyphus build

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1
- rebuild to restore role requires

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- initial import by package builder

