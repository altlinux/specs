Name: perl-Object-Container
Version: 0.14
Release: alt2
Summary: Object::Container - simple object container

Group: Development/Perl
License: Perl
Url: %CPAN Object-Container

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Test-Requires perl-parent perl-Class-Accessor perl-Module-Install perl-Test-Base perl-Module-Install-Repository perl-Module-Install-AuthorTests perl-Module-Install-TestBase

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
* Thu Oct 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- Fixed FTBFS

* Fri Aug 12 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build
