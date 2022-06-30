Name: perl-Object-Container
Version: 0.05001
Release: alt1
Summary: Object::Container - simple object container

Group: Development/Perl
License: Perl
Url: %CPAN Object-Container
VCS: git+https://github.com/typester/object-container-perl

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Test-Requires perl-parent perl-Class-Accessor perl-Module-Install perl-Test-Base perl-Module-Install-Repository perl-Module-Install-AuthorTests perl-Module-Install-TestBase perl(Exporter/AutoClean.pm) perl(Class/Singleton.pm) perl(Any/Moose.pm) perl(Moo.pm) perl(Moose.pm)

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
%doc LICENSE Changes README 

%changelog
* Thu Jun 30 2022 Igor Vlasenko <viy@altlinux.org> 0.05001-alt1
- new version 0.05001

* Thu Oct 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- Fixed FTBFS

* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
