Name: perl-Gtk3-WebKit
Version: 0.04
Release: alt1

Summary: WebKit bindings for Perl
Group: Development/Perl
License: Perl

Url: %CPAN Gtk3-WebKit
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: libgtk+3-gir libwebkitgtk3-gir perl(Glib/Object/Introspection.pm) perl(Gtk3.pm) perl-devel xvfb-run

%description
%summary

%prep
%setup -q
sed -i '/Test::NeedsDisplay/d' Makefile.PL t/webkit.t

%build
%def_without test
%perl_vendor_build
xvfb-run -a make test

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Gtk3/WebKit*
%doc README Changes

%changelog
* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build for ALTLinux

