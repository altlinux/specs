%define m_distro Module-Install-AuthorTests
Name: perl-Module-Install-AuthorTests
Version: 0.002
Release: alt1
Summary: Module::Install::AuthorTests designate tests only run by module authors

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~rjbs/Module-Install-AuthorTests/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Module-Install

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/AuthorTests.pm
%doc Changes README 

%changelog
* Thu Feb 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.002-alt1
- initial build
