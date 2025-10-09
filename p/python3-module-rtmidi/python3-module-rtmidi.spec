%define _unpackaged_files_terminate_build 1
%define pypi_name rtmidi

Name: python3-module-%pypi_name
Version: 2.5.0
Release: alt1.1

Summary: Realtime MIDI I/O for python
License: GPL-2.0-or-later
Group: Development/Python3

Url: https://github.com/patrickkidd/pyrtmidi
Vcs: https://github.com/patrickkidd/pyrtmidi
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: python3(pytest)
BuildRequires: python3(setuptools)

%description
%summary.

%prep
%setup
%patch -p1

# Hot fix for python3.13
sed -i 's/PyEval_CallObject/PyObject_CallObject/'  src/rtmidimodule.cpp

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/pkechomidi.py
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info
%doc README.md DOC.txt CHANGELOG.txt

%changelog
* Thu Sep 11 2025 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1.1
- NMU: fixed build with python3.13.

* Sun Apr 13 2025 David Sultaniiazov <x1z53@altlinux.org> 2.5.0-alt1
- Initial build
