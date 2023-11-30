%define _unpackaged_files_terminate_build 1
%def_without bootstrap

BuildRequires: perl-podlators
Name: perl-Glib-Object-Introspection
Version: 0.051
Release: alt3

Summary: Dynamically create Perl language bindings
Group: Development/Perl
License: LGPL-2.1+

Url: %CPAN Glib-Object-Introspection
Source: %name-%version.tar

BuildRequires: gobject-introspection-devel libcairo-gobject-devel perl-devel perl-ExtUtils-Depends perl-Glib-devel perl-ExtUtils-PkgConfig perl(XML/LibXML.pm)
# dependency loop
%if_with bootstrap
%add_findreq_skiplist %_bindir/perli11ndoc
%else
BuildRequires: perl-Gtk3
%endif

%description
%summary

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description scripts
scripts for %name

%prep
%setup -q

%build
# some Glib functions fail with LANG=C
export LANG=ru_RU.UTF-8
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md
%perl_vendor_autolib/Glib/Object/Introspection*
%perl_vendor_archlib/Glib/Object/Introspection*

%files scripts
%_bindir/perli11ndoc
%_man1dir/perli11ndoc.1*

%changelog
* Thu Nov 30 2023 Igor Vlasenko <viy@altlinux.org> 0.051-alt3
- unbootstrap

* Fri Nov 24 2023 Igor Vlasenko <viy@altlinux.org> 0.051-alt2.1
- rebuild with new perl 5.38.0 (bootstrapped)

* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 0.051-alt2
- added bootstrap sdupport for circular dep on perl-Gtk3

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.051-alt1
- new version

* Wed Apr 19 2023 Igor Vlasenko <viy@altlinux.org> 0.050-alt1
- new version

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1
- new version

* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2
- fixed warning: scripts should be .noarch

* Wed Dec 11 2019 Igor Vlasenko <viy@altlinux.ru> 0.048-alt1
- new version

* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1.1
- rebuild with new perl 5.28.1

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1
- automated CPAN update

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.045-alt1
- automated CPAN update

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

