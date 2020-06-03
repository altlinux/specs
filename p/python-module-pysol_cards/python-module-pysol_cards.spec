%define  modulename pysol_cards

Name:    python-module-%modulename
Version: 0.8.18
Release: alt1

Summary: Python library for dealing cards like PySol FC, MS Freecell/Freecell Pro, or PySol legacy
License: MIT
Group:   Development/Python
URL:     https://github.com/shlomif/pysol_cards

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr

BuildArch: noarch

Source:  %modulename-%version.tar

%description
The pysol-cards python modules allow the python developer to generate
the initial deals of some PySol FC games. It also supports PySol legacy
deals and Microsoft FreeCell / Freecell Pro deals.

%prep
%setup -n %modulename-%version

%build
export PBR_VERSION=%version
%python_build

%install
export PBR_VERSION=%version
%python_install
rm -rf %buildroot%python_sitelibdir/%modulename/tests

%files
%doc README.rst
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 0.8.18-alt1
- Initial build for Sisyphus.
