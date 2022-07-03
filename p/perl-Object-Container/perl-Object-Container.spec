%define _unpackaged_files_terminate_build 1
Epoch: 1
Name: perl-Object-Container
Version: 0.16
Release: alt1
Summary: Object::Container - simple object container

Group: Development/Perl
License: Perl
Url: %CPAN Object-Container
VCS: git+https://github.com/typester/object-container-perl

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Test-Requires perl-parent perl-Class-Accessor perl-Test-Base perl(Exporter/AutoClean.pm) perl(Class/Singleton.pm) perl(Any/Moose.pm) perl(Moo.pm) perl(Moose.pm)
#BuildRequires: perl-Module-Install perl-Module-Install-Repository perl-Module-Install-AuthorTests perl-Module-Install-TestBase
BuildRequires: perl(Module/Build/Pluggable.pm) perl(Module/Build/Pluggable/CPANfile.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Object/Container*
%doc Changes README

%changelog
* Sun Jul 03 2022 Igor Vlasenko <viy@altlinux.org> 1:0.16-alt1
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1:0.15-alt1
- new version

* Thu Jun 30 2022 Igor Vlasenko <viy@altlinux.org> 0.05001-alt1
- new version 0.05001

* Thu Oct 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- Fixed FTBFS

* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
