%define m_distro Devel-Dumpvar
Name: perl-Devel-Dumpvar
Version: 1.06
Release: alt1
Summary: Devel::Dumpvar - A pure-OO reimplementation of dumpvar.pl

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/Devel-Dumpvar/

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
%perl_vendor_privlib/Devel/Dumpvar*
%doc Changes README 

%changelog
* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt1
- initial build
