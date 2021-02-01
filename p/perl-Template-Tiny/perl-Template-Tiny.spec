%define _unpackaged_files_terminate_build 1
%define m_distro Template-Tiny
Name: perl-Template-Tiny
Version: 1.13
Release: alt1
Summary: Template::Tiny - Template Toolkit reimplemented in as little code as possible

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/Template-Tiny/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Capture-Tiny

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes CONTRIBUTING README
%perl_vendor_privlib/Template/Tiny*
%doc Changes README

%changelog
* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- new version

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Sat Jan 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- initial build
