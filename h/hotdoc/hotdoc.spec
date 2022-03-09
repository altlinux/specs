%def_enable snapshot
%define ver_major 0.13

%def_disable bootstrap_theme
%def_enable check

Name: hotdoc
Version: %ver_major.7
Release: alt2

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

%define clang_ver 12.0
Requires: clang%clang_ver-devel llvm%clang_ver-devel
Requires: bison flex
Requires: python3-module-appdirs >= 1.4.4
Requires: python3-module-contextlib2 >= 0.6.0
Requires: python3-module-cchardet >= 2.1.7
Requires: python3-module-wheezy.template >= 3.0.3
Requires: python3-module-contextlib2 >= 0.5.5
Requires: python3-module-dbus-deviation >= 0.6.0
Requires: python3-module-decorator >= 4.4.2
Requires: python3-module-lxml >= 4.6.3
Requires: python3-module-toposort >= 1.6
Requires: python3-module-yaml >= 5.4.1
Requires: python3-module-schema >= 0.7.2
Requires: python3-module-networkx-core >= 2.5

BuildRequires(pre): rpm-build-gir rpm-build-python3
BuildRequires: python3-module-setuptools cmake gcc-c++ bison flex
BuildRequires: pkgconfig(libxml-2.0) pkgconfig(gio-2.0) pkgconfig(json-glib-1.0)
# for hotdoc_bootstrap_theme
BuildRequires: meson npm node-gyp
%{?_enable_check:
BuildRequires: python3-module-appdirs python3-module-contextlib2
BuildRequires: python3-module-lxml python3-module-cchardet
BuildRequires: python3-module-schema python3-module-toposort
BuildRequires: python3-module-unittest2 python3-module-wheezy.template
BuildRequires: python3-module-yaml python3-module-dbus-deviation
BuildRequires: python3-module-networkx-core python3-module-feedgen}

%description
Hotdoc is a documentation micro-framework. It provides an interface for
extensions to plug upon, along with some base objects (formatters, ...)
See https://hotdoc.github.io for more unformation.

%prep
%setup %{?_disable_bootstrap_theme:-a1}
%if_enabled bootstrap_theme
pushd %name/%{name}_bootstrap_theme
npm install && npm audit fix && ./node_modules/bower/bin/bower install
popd
tar -cf %name-%version-bootstrap_theme.tar hotdoc/hotdoc_bootstrap_theme/{node_modules,bower_components}/ && \
mv %name-%version-bootstrap_theme.tar %_sourcedir/
%endif

%build
%python3_build

%install
%python3_install

%check
%__python3 setup.py test

%files
%_bindir/%name
%_bindir/%{name}_dep_printer
%python3_sitelibdir/*
%doc README.md

%changelog
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

