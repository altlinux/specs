Name: perl-Gtk3
Version: 0.033
Release: alt1

Summary: Perl interface to the 3.x series of the gtk+ toolkit
Group: Development/Perl
License: lgpl

Url: %CPAN Gtk3
Source: %name-%version.tar

BuildArch: noarch
BuildRequires:libgtk+3-devel libgtk+3-gir perl(Glib/Object/Introspection.pm) perl-devel perl(Cairo/GObject.pm)

Requires: libgtk+3-gir

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
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.033-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.032-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.030-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.028-alt1
- automated CPAN update

* Wed Jun 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.026-alt2
- added Requires: libgtk+3-gir (closes: #32152)

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.026-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.020-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.019-alt1
- automated CPAN update

* Thu May 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.016-alt1
- 0.016

* Mon Oct 07 2013 Vladimir Lettiev <crux@altlinux.ru> 0.013-alt1
- initial build for ALTLinux

