%define m_distro Test-Block
Name: perl-Test-Block
Version: 0.11
Release: alt1
Summary: Test::Block - Specify fine granularity test plans

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adie/Test-Block/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-pod perl-Module-Build perl-Test-Exception

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Block*
%doc Changes README 

%changelog
* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
