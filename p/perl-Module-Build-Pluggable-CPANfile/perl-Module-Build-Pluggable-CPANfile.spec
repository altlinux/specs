# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Capture/Tiny.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Module/Build/Pluggable.pm) perl(Module/Build/Pluggable/Base.pm) perl(Module/CPANfile.pm) perl(Test/Module/Build/Pluggable.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(parent.pm) perl(version.pm)
# END SourceDeps(oneline)
%define module_version 0.05
%define module_name Module-Build-Pluggable-CPANfile
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Include cpanfile
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Module-Build-Pluggable-CPANfile

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
%doc Changes LICENSE README.md
%perl_vendor_privlib/M*

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt2
- to Sisyphus as perl-Object-Container build dep

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

