%def_with check

Name:    tlpui
Version: 1.7.1
Release: alt1

Summary: A GTK user interface for TLP written in Python
License: GPL-2.0
Group:   Development/Python3
URL:     https://github.com/d4nj1/TLPUI

Packager: Leonid Znamenok <respublica@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(gi)
BuildRequires: python3(yaml)
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk+3-gir-devel
%endif

Requires: tlp

BuildArch: noarch

Source: %name-%version.tar

Source100: %name.watch

%description
The Python scripts in this project generate a GTK-UI to change TLP
configuration files easily. It has the aim to protect users from
setting bad configuration and to deliver a basic overview
of all the valid configuration values.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_desktopdir
install -m0644 tlpui.desktop %buildroot%_desktopdir/tlpui.desktop

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/tlpui
%python3_sitelibdir/tlpui/
%python3_sitelibdir/tlp_ui-%version.dist-info
%_desktopdir/tlpui.desktop


%changelog
* Tue Jan 14 2025 Leonid Znamenok <respublica@altlinux.org> 1.7.1-alt1
- New version 1.7.1.
- Added watch file.

* Wed Jan 10 2024 Leonid Znamenok <respublica@altlinux.org> 1.6.1-alt1
- New release 1.6.1

* Fri Oct 06 2023 Leonid Znamenok <respublica@altlinux.org> 1.6.0-alt1
- New release 1.6.0

* Tue Mar 28 2023 Leonid Znamenok <respublica@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
