Name: perl-Cairo-GObject
Version: 1.004
Release: alt1.1.1.1.1

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1.1
- rebuild with new perl 5.20.1

* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 1.004-alt1
- 1.004

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 1.001-alt1
- initial build for ALTLinux

