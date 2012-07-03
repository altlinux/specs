%define m_distro Locale-Msgfmt
Name: perl-Locale-Msgfmt
Version: 0.15
Release: alt1
Summary: Compile .po files to .mo files

Group: Development/Perl
License: Artistic
Url: http://search.cpan.org/~szabgab/Locale-Msgfmt

BuildArch: noarch
Source: %m_distro-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: perl-devel perl-Module-Build perl-Module-Install

%description
Locale::Msgfmt is a pure Perl reimplementation of msgfmt from GNU
gettext-tools.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/Msgfmt.pm
%perl_vendor_privlib/Locale/Msgfmt*
%doc Changes README

%changelog
* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15
- Dropped script msgfmt.pl

* Sun Nov 21 2010 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- Fixed generation of man1 pages

* Wed Nov 04 2009 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- initial build

