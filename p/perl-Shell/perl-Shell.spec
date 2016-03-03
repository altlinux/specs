%define m_distro Shell
Name: perl-Shell
Version: 0.73
Release: alt1
Summary: Shell - run shell commands transparently within perl

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~ferreira/Shell/

Source: %m_distro-%version.tar
BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Shell*
%doc Changes README 

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Tue Nov 02 2010 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1
- initial build
