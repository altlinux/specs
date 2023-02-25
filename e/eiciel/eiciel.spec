Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: eiciel
Version: 0.10.0
%global tar_version %{version}

Release: alt1_2
Summary: Graphical editor for ACLs and xattr
License: GPLv2+
URL: http://rofi.roger-ferrer.org/eiciel
Source0: http://rofi.roger-ferrer.org/eiciel/files/eiciel-%{tar_version}.tar.xz

BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: pkgconfig(gtkmm-4.0)
BuildRequires: pkgconfig(libnautilus-extension-4)
BuildRequires: libacl-devel
BuildRequires: itstool
BuildRequires: desktop-file-utils

Requires: icon-theme-hicolor

%global ext_dir %(eval "pkg-config --variable=extensiondir libnautilus-extension-4")

# don't "provide" a private shlib
%global __provides_exclude_from ^%{ext_dir}/.*\\.so$
Source44: import.info


%description
Graphical editor for access control lists (ACLs) and extended attributes
(xattr), either as an extension within Nautilus, or as a standalone
utility.


%prep
%setup -q -n %{name}-%{tar_version}



%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc AUTHORS
%doc --no-dereference COPYING
%{_bindir}/%{name}
%{_datadir}/help/C/%{name}/
%{_datadir}/applications/*.desktop
%{ext_dir}/lib%{name}*.so
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*%{name}.*
%{_mandir}/man1/%{name}.*


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.10.0-alt1_2
- update to new release by fcimport

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 0.10.0-alt1_0.2.rc2
- new version

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.9.13.1-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.13-alt1_1
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt2_8
- update to new release by fcimport

* Wed Apr 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt2_5
- to Sisyphus (closes: #35839)

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt1_5
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.12.1-alt1_4
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_7
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_5
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_4
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_3
- update to new release by fcimport

* Sat Oct 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_1
- new update

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_1
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.8.2-alt1_2
- update to new release by fcimport

* Sat Dec 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.2-alt1_1
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_10
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_9
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_8
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_7
- update to new release by fcimport

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.8.1-alt1_6
- fc import

