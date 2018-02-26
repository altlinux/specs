%define m_distro Text-FindIndent
Name: perl-Text-FindIndent
Version: 0.10
Release: alt1
Summary: Text::FindIndent - Heuristically determine the indent style

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~smueller/Text-FindIndent/

BuildArch: noarch
Source: %m_distro-%version.tar
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
%perl_vendor_privlib/Text/FindIndent*
%doc Changes README 

%changelog
* Tue Jan 11 2011 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- New version 0.10

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- New version 0.09

* Tue Jan 26 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- initial build
