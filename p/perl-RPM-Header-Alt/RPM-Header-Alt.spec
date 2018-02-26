%define m_distro RPM-Header-Alt
Name: perl-%m_distro
Version: 1.0.0
Release: alt1

Summary: Alternative pure perl RPM header reader for ALTLinux fork of RPM
License: Artistic
Group: Development/Perl
Url: http://www.sisyphus.ru/srpm/perl-RPM-Header-Alt

Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %m_distro-%version.tar
BuildArch: noarch

BuildRequires: perl-devel

%description
RPM::Header::Alt is alternative implementation of RPM::Header written in only Perl.
Its based on RPM::Header::PurePerl, but adopted to ALTLinux fork of RPM

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/RPM/Header/Alt.pm
%doc Changes

%changelog
* Sat May 16 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1
- initial build

