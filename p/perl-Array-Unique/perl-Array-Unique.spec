%define _unpackaged_files_terminate_build 1
%define m_distro Array-Unique
Name: perl-Array-Unique
Version: 0.09
Release: alt1
Summary: Array::Unique - Tie-able array that allows only unique values

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Artistic-2.0
Url: http://search.cpan.org/~szabgab/Array-Unique/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Module-Build perl(Tie/IxHash.pm)

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md README
%perl_vendor_privlib/Array/Unique*
%doc Changes README

%changelog
* Tue Jun 13 2023 Igor Vlasenko <viy@altlinux.org> 0.09-alt1
- new version

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
