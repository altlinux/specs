Name: perl-Cairo-GObject
Version: 1.001
Release: alt1

Summary: Integrate Cairo into the Glib type system
Group: Development/Perl
License: Perl

Url: %CPAN Cairo-GObject
Source: %name-%version.tar

BuildRequires: libcairo-gobject-devel perl-devel perl-ExtUtils-Depends perl-Glib-devel perl-Cairo-devel perl-ExtUtils-PkgConfig

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Cairo/GObject*
%perl_vendor_archlib/Cairo/GObject*
%doc LICENSE NEWS README

%changelog
* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 1.001-alt1
- initial build for ALTLinux

