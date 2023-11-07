%def_with check

Name:    tlpui
Version: 1.6.0
Release: alt1

Summary: A GTK user interface for TLP written in Python
License: GPL-2.0
Group:   Development/Python3
URL:     https://github.com/d4nj1/TLPUI

Packager: Leonid Znamenok <respublica@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(gi)
BuildRequires: gobject-introspection-devel
BuildRequires: libgtk+3-gir-devel
%endif

Requires: tlp

BuildArch: noarch

Source: %name-%version.tar
Patch0: tlpui-1.6.0-alt-correct-test-case.patch

%description
The Python scripts in this project generate a GTK-UI to change TLP
configuration files easily. It has the aim to protect users from
setting bad configuration and to deliver a basic overview
of all the valid configuration values.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/tlpui
%python3_sitelibdir/tlpui/
%python3_sitelibdir/TLPUI-%version.dist-info
%_desktopdir/tlpui.desktop


%changelog
* Fri Oct 06 2023 Leonid Znamenok <respublica@altlinux.org> 1.6.0-alt1
- New release 1.6.0

* Tue Mar 28 2023 Leonid Znamenok <respublica@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus
