%def_enable snapshot
%define ver_major 0.17

%def_disable bootstrap_theme
%def_enable check

Name: hotdoc
Version: %ver_major
Release: alt1

Summary: Hotdoc is a documentation framework
License: LGPL-2.1-or-later
Group: Text tools
Url: https://github.com/%name/%name

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-bootstrap_theme.tar

# provided by hotdoc/parsers/c_comment_scanner/c_comment_scanner.cpython-3*.so
%py3_provides hotdoc.parsers.c_comment_scanner.c_comment_scanner
# for old python
%filter_from_requires /backports.entry_points_selectable/d

Requires: clang-devel llvm-devel
Requires: bison flex
Requires: python3-module-appdirs >= 1.4.4
Requires: python3-module-contextlib2 >= 0.6.0
Requires: python3-module-charset-normalizer >= 2.1.1
Requires: python3-module-faust-cchardet >= 2.1.18
Requires: python3-module-wheezy.template >= 3.1.0
Requires: python3-module-contextlib2 >= 0.5.5
Requires: python3-module-dateutil >= 2.8.2
Requires: python3-module-dbus-deviation >= 0.6.1
Requires: python3-module-feedgen >= 0.9.0
Requires: python3-module-lxml >= 4.9.1
Requires: python3-module-pkgconfig >= 1.5.1
Requires: python3-module-toposort >= 1.6
Requires: python3-module-yaml >= 6
Requires: python3-module-schema >= 0.7.2
Requires: python3-module-six >= 1.16.0
Requires: python3-module-networkx-core >= 2.8.8

BuildRequires(pre): rpm-build-gir rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: cmake gcc-c++ bison flex
BuildRequires: pkgconfig(libxml-2.0) pkgconfig(gio-2.0) pkgconfig(json-glib-1.0)
# for hotdoc_bootstrap_theme
BuildRequires: meson npm node-gyp
%{?_enable_check:
BuildRequires: python3-module-appdirs python3-module-contextlib2
BuildRequires: python3-module-lxml python3-module-charset-normalizer
BuildRequires: python3-module-dateutil python3-module-feedgen
BuildRequires: python3-module-schema python3-module-toposort
BuildRequires: python3-module-wheezy.template python3-module-six
BuildRequires: python3-module-yaml python3-module-dbus-deviation
BuildRequires: python3-module-networkx-core}

%description
Hotdoc is a documentation micro-framework. It provides an interface for
extensions to plug upon, along with some base objects (formatters, ...)
See https://hotdoc.github.io for more unformation.

%prep
%setup %{?_disable_bootstrap_theme:-a1}
%if_enabled bootstrap_theme
pushd %name/%{name}_bootstrap_theme
npm install || npm audit fix --force &&
./node_modules/bower/bin/bower install &&
popd
tar -cf %name-%version-bootstrap_theme.tar hotdoc/hotdoc_bootstrap_theme/{node_modules,bower_components}/ && \
mv %name-%version-bootstrap_theme.tar %_sourcedir/
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
#export PYTHONPATH=%buildroot%python3_sitelibdir
#py.test3 %name/tests
%__python3 setup.py test

%files
%_bindir/%name
%_bindir/%{name}_dep_printer
%python3_sitelibdir/*
%doc README.md

%changelog
* Tue Jun 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.17-alt1
- 0.17

* Fri Nov 10 2023 Yuri N. Sedunov <aris@altlinux.org> 0.16-alt1
- 0.16

* Fri Nov 03 2023 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Thu Apr 27 2023 Yuri N. Sedunov <aris@altlinux.org> 0.15-alt1
- 0.15

* Thu Apr 13 2023 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Fri Apr 07 2023 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0-7-g29901af

* Mon May 30 2022 Yuri N. Sedunov <aris@altlinux.org> 0.13.7-alt2.2
- fixed BR

* Tue Apr 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.13.7-alt2.1
- drop versions from clang/llvm dependencies

* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 0.13.7-alt2
- updated BR

* Fri Oct 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.7-alt1
- 0.13.7

* Sun Sep 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.5-alt1
- 0.13.5

* Thu Jul 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.4-alt1
- 0.13.4

* Tue Jun 08 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt2
- updated c-extension dependencies

* Wed Mar 10 2021 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- first build for Sisyphus (0.12.2-12-g83d0c70)

