%define m_distro Array-Unique
Name: perl-Array-Unique
Version: 0.08
Release: alt1
Summary: Array::Unique - Tie-able array that allows only unique values

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Artistic
Url: http://search.cpan.org/~szabgab/Array-Unique/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Module-Build

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Array/Unique*
%doc Changes README 

%changelog
* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
