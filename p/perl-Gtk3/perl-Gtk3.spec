Name: perl-Gtk3
Version: 0.019
Release: alt1

Summary: Perl interface to the 3.x series of the gtk+ toolkit
Group: Development/Perl
License: lgpl

Url: %CPAN Gtk3
Source: %name-%version.tar

BuildArch: noarch
BuildRequires:libgtk+3-devel libgtk+3-gir perl(Glib/Object/Introspection.pm) perl-devel perl(Cairo/GObject.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Gtk3*
%doc LICENSE NEWS README

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- automated CPAN update

* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.016-alt1
- 0.016

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt1
- initial build for ALTLinux

