Name: perl-Glib-Object-Introspection
Version: 0.016
Release: alt1

Summary: Dynamically create Perl language bindings
Group: Development/Perl
License: lgpl

Url: %CPAN Glib-Object-Introspection
Source: %name-%version.tar

BuildRequires: gobject-introspection-devel libcairo-gobject-devel perl-devel perl-ExtUtils-Depends perl-Glib-devel perl-ExtUtils-PkgConfig

%description
%summary

%prep
%setup -q

%build
# some Glib functions fail with LANG=C
export LANG=ru_RU.UTF-8
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Glib/Object/Introspection*
%perl_vendor_archlib/Glib/Object/Introspection*
%doc LICENSE NEWS README

%changelog
* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.016-alt1
- initial build for ALTLinux

