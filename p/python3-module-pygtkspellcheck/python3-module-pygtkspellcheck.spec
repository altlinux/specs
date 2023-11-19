%define modname gtkspellcheck
%define pypi_name py%modname

Name: python3-module-%pypi_name
Version: 5.0.2
Release: alt1

Summary: Python GTK Spellcheck library
Group: Development/Python3
License: GPL-3.0-or-later
Url: https://pypi.python.org/pypi/%pypi_name

Vcs: https://github.com/koehlma/pygtkspellcheck.git
Source: https://pypi.io/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3(wheel) python3(poetry-core)

%description
Python GTK Spellcheck is a simple but quite powerful spellchecking
library for GTK written in pure Python. It's spellchecking component is
based on Enchant and it supports both GTK 3 and 4 via PyGObject.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Sun Nov 19 2023 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- first build for Sisyphus



