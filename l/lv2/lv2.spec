%def_enable old_headers
%def_enable check

Name: lv2
Version: 1.18.10
Release: alt1.1

Summary: Audio Plugin Standard
# lv2specgen template.html is CC-AT-SA
License: ISC
Group: System/Libraries
Url: http://lv2plug.in

Vcs: https://github.com/lv2/lv2.git
Source: http://lv2plug.in/spec/lv2-%version.tar.xz
Source1: lv2-1.18.4-include-symlinks
Patch1: %name-1.18.10-alt-codespell.patch

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson
BuildRequires: libsndfile-devel
BuildRequires: libcairo-devel >= 1.8.10
BuildRequires: python3-devel
BuildRequires: python3-module-Pygments
BuildRequires: python3-module-rdflib
BuildRequires: python3-module-markdown
BuildRequires: python3-module-lxml
BuildRequires: doxygen graphviz
BuildRequires: asciidoc-a2x
%{?_enable_check:BuildRequires: codespell /usr/bin/serdi}

# this package replaces lv2core
Provides: lv2core = 6.0-4
Obsoletes: lv2core < 6.0-4
Provides: lv2-ui = 2.4-5
Obsoletes: lv2-ui < 2.4-5

%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.

%package devel
Summary: API for the LV2 Audio Plugin Standard
Group: Development/C
Requires: %name = %EVR
Requires: python3-module-rdflib
Requires: python3-module-markdown
Provides: lv2core-devel = 6.0-4
Obsoletes: lv2core-devel < 6.0-4
Provides: lv2-ui-devel = 2.4-5
Obsoletes: lv2-ui-devel < 2.4-5

%description devel
lv2-devel contains the lv2.h header file and headers for all of the
LV2 specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%package doc
Summary: Documentation for the LV2 Audio Plugin Standard
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version

%description doc
Documentation for the LV2 plugin API.

%package example-plugins
Summary: Examples of the LV2 Audio Plugin Standard
Group: Sound
Requires: %name = %EVR

%description example-plugins
Example LV2 audio plugins

%{!?_pkgdocdir: %global _pkgdocdir %_docdir/%name-%version}

%prep
%setup
%patch1
# Fix wrong interpreter in lv2specgen.py
sed -i '1s|^#!.*|#!%__python3|' lv2specgen/lv2specgen.py

%build
%meson %{?_disable_old_headers:-Dold_headers=false}
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name/
%doc NEWS README*

%exclude %_libdir/%name/eg-*

%files devel
%_bindir/%{name}specgen.py
%_bindir/%{name}_validate
%_datadir/%{name}specgen
%_includedir/%name/atom/
%_includedir/%name/buf-size/
%_includedir/%name/core/
%_includedir/%name/data-access/
%_includedir/%name/dynmanifest/
%_includedir/%name/event/
%_includedir/%name/instance-access/
%_includedir/%name/log/
%_includedir/%name/midi/
%_includedir/%name/morph/
%_includedir/%name/options/
%_includedir/%name/parameters/
%_includedir/%name/patch/
%_includedir/%name/port-groups/
%_includedir/%name/port-props/
%_includedir/%name/presets/
%_includedir/%name/resize-port/
%_includedir/%name/state/
%_includedir/%name/time/
%_includedir/%name/ui/
%_includedir/%name/units/
%_includedir/%name/urid/
%_includedir/%name/uri-map/
%_includedir/%name/worker/
%{?_enable_old_headers:%_includedir/%name.h
%_includedir/%name/lv2plug.in/}
%_pkgconfigdir/%name.pc

%files example-plugins
%_libdir/%name/eg-*

%files doc
%_docdir/%name/

%changelog
* Sat Oct 07 2023 Yuri N. Sedunov <aris@altlinux.org> 1.18.10-alt1.1
- fixed misspellings found by codespell-2.2.6

* Sat Sep 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.10-alt1
- 1.18.8 (ported to Meson build system)

* Fri May 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4

* Tue Sep 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2 (ALT #40919)

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.18.0-alt1_1
- update to new release by fcimport

* Mon Mar 30 2020 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_3
- new version

* Sat Mar 16 2019 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_9
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_7
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_5
- update to new release by fcimport

* Wed Oct 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- update to new release by fcimport

* Thu Jan 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- update to new release by fcimport

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_2
- import

