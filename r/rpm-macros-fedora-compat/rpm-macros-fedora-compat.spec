%define module fedora-compat
Name: rpm-macros-%module
Summary: Fedora compatibility set of macro
Version: 0.11
Release: alt1
License: GPL
Group: System/Base
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>

Source: %name-%version.tar
Patch: macros.systemd-alt.patch
Requires: rpm-macros-kde-common-devel

%description
%summary

%prep
%setup
%patch -p1
%install
install -D -m644 %module -p %buildroot%_rpmmacrosdir/%module-base
for ext in cmake kde4 qt4 perl systemd; do
    install -D -m644 macros.$ext -p %buildroot%_rpmmacrosdir/%module-$ext
done

%files
%_rpmmacrosdir/*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added perl_testdir

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- updated systemd

* Fri Oct 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added _jsdir

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt5
- added GNAT_arches

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- added _cups_serverbin

* Wed Oct 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt3
- fc sugar macros fix

* Tue Oct 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- added sugar libdir

* Wed Oct 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added sugar activity dir

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- fixes in systemd macros

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added __python3

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added fc systemd compat macros

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added fc compatible kde4 macros

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt4
- dropped unitdir (in main rpm now)

* Fri Jun 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3
- added _datarootdir

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- added __id_u

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added perl compat macros

* Mon May 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- more fc macros

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added qt4 compat macros

* Thu Jul 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
