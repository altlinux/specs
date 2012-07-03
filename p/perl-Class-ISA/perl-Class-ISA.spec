%define m_distro Class-ISA
Name: perl-Class-ISA
Version: 0.36
Release: alt1
Summary: report the search path for a class's ISA tree

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~smueller/Class-ISA/

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
%perl_vendor_privlib/Class/ISA*
%doc ChangeLog README 

%changelog
* Tue Nov 02 2010 Vladimir Lettiev <crux@altlinux.ru> 0.36-alt1
- initial build
