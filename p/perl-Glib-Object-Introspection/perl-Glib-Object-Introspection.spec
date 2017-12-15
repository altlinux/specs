Name: perl-Glib-Object-Introspection
Version: 0.044
Release: alt1.1

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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1.1
- rebuild with new perl 5.26.1

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.044-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1.1
- rebuild with new perl 5.24.1

* Thu Jan 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.041-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.040-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1.1
- rebuild with new perl 5.20.1

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- automated CPAN update

* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.022-alt1
- 0.022

* Tue Feb 25 2014 Vladimir Lettiev <crux@altlinux.ru> 0.020-alt1
- 0.016 -> 0.020

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.016-alt1
- initial build for ALTLinux

