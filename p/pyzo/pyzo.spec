%define _unpackaged_files_terminate_build 1

%def_with check

Name: pyzo
Version: 4.20.0
Release: alt1

Summary: interactive editor for scientific Python
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/pyzo/pyzo

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(flit_core)
BuildRequires: /usr/bin/sphinx-build

%filter_from_requires /python3(codeeditor)/d
%filter_from_requires /python3(pyzo.*)/d
%filter_from_requires /python3(yoton.*)/d

%if_with check
BuildRequires: python3-module-qtpy
BuildRequires: python3-module-pyside6
BuildRequires: /usr/bin/xvfb-run
%endif

Requires: python3-module-qtpy
Requires: python3-module-pyside6

BuildArch: noarch

Source: %name-%version.tar

%description
Pyzo is a cross-platform Python IDE focused on interactivity and introspection,
which makes it very suitable for scientific computing. Its practical design is
aimed at simplicity and efficiency.

It consists of two main components, the editor and the shell, and uses a set of
pluggable tools to help the programmer in various ways. Some example tools are
source structure, project manager, interactive help, workspace...

Pyzo is written in (pure) Python 3 and uses the Qt GUI toolkit. Binaries are
provided for all major operating system. After installing Pyzo, it can be used
to execute code on any Python version available on your system
(CPython or Pypy).

This package provides the Pyzo IDE.

%package doc
Summary: documentation for Pyzo
Group: Documentation
BuildArch: noarch

%description doc
Pyzo is a cross-platform Python IDE focused on interactivity and introspection,
which makes it very suitable for scientific computing. Its practical design is
aimed at simplicity and efficiency.

It consists of two main components, the editor and the shell, and uses a set of
pluggable tools to help the programmer in various ways. Some example tools are
source structure, project manager, interactive help, workspace...

Pyzo is written in (pure) Python 3 and uses the Qt GUI toolkit. Binaries are
provided for all major operating system. After installing Pyzo, it can be used
to execute code on any Python version available on your system
(CPython or Pypy).

This package provides the documentation for the Pyzo IDE.

%prep
%setup
sed -i "s/Categories=.*/Categories=Development;IDE;Qt;/" pyzo/resources/org.pyzo.Pyzo.desktop
sed -i "s/GenericName=.*/GenericName=Integrated Development Environment for scientific Python/" pyzo/resources/org.pyzo.Pyzo.desktop

%build
%pyproject_build

%install
make -C doc html man
%pyproject_install

install -Dm644 pyzo.appdata.xml -t %buildroot%_datadir/metainfo/

install -Dm644 pyzo/resources/org.pyzo.Pyzo.desktop -t %buildroot%_desktopdir/
for i in 16 32 48 64 128 256 ; do
    install -Dm644 pyzo/resources/appicons/pyzologo${i}.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/pyzologo.png
done

mkdir -pv %buildroot%_man1dir/
mv -v doc/_build/man/pyzo.1 %buildroot%_man1dir/pyzo.1

mkdir -pv %buildroot%_datadir/doc/pyzo/
mv -v doc/_build/html %buildroot%_datadir/doc/pyzo/

%check
%tox_check_pyproject
%pyproject_run_pytest -v tests
xvfb-run --auto-servernum %__python3 pyzolauncher.py --test
%__python3 tests/check_log.py

%files
%doc LICENSE.md README.md RELEASE_NOTES.md TRANSLATIONS.md
%_bindir/pyzo
%_man1dir/pyzo.1.*
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_desktopdir/org.pyzo.Pyzo.desktop
%_iconsdir/hicolor/*/apps/pyzologo.png
%_datadir/metainfo/pyzo.appdata.xml

%files doc
%dir %_datadir/doc/pyzo/
%_datadir/doc/pyzo/*

%changelog
* Wed Dec 24 2025 Nikolay Strelkov <snk@altlinux.org> 4.20.0-alt1
- Initial build for Sisyphus
