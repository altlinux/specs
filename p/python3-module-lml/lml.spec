%define _unpackaged_files_terminate_build 1

Name: python3-module-lml
Version: 0.2.0
Release: alt1

Summary: A lazy plugin management system
Group: Development/Python3
License: BSD-3-Clause
URL: https://github.com/python-lml/lml
VCS: https://github.com/python-lml/lml.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: fdupes
BuildRequires: python3-module-isort
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
LML is "Load me later". lml seamlessly finds the lml-based
plugins from the current Python environment but loads plugins on
demand. It supports plugins that have external dependencies,
especially bulky and/or memory hungry ones. lml provides the plugin
management system only and the plugin interface is for the developer
to do.

Plugins loaded by lml may be installed packages or standalone
Python modules in a supplied directory.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/lml
%python3_sitelibdir/%{pyproject_distinfo lml}

%changelog
* Sun Apr 05 2026 Ilya Muhamadeev <nicourced@altlinux.org> 0.2.0-alt1
- Initial build.
