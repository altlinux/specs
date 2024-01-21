%define _unpackaged_files_terminate_build 1
%define pypi_name sphinx-automodapi

%def_with check
Name: python3-module-%pypi_name
Version: 0.16.0
Release: alt1
License: MIT
# https://files.pythonhosted.org/packages/76/f5/b352eee084f2bcebb25f144dece8fd2bd77d6a48c5d5bde083419d4c6ec0/sphinx-automodapi-0.16.0.tar.gz
Source: sphinx-automodapi-%version.tar
Group: Development/Python3
BuildArch: noarch
Summary: A sphinx extension to automatically generate API pages for whole modules
Url: https://github.com/astropy/sphinx-automodapi

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)
BuildRequires: python3(sphinxcontrib.serializinghtml)

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: /usr/bin/dot
BuildRequires: python3(Cython)
BuildRequires: fontconfig fonts-ttf-vera
%endif

%py3_provides %pypi_name

%description
This is a Sphinx extension to automatically generate API pages for whole
modules. It was originally developed for the Astropy project but is now
available as a standalone package since it can be used for any other
package. The documentation can be found on

%prep
%setup -n sphinx-automodapi-%version
for N in $(grep -rl "python': ('https://docs.python.org/" sphinx_automodapi/tests); do
        sed -i "s@'https://docs.python.org/3/'@'/usr/share/python-sphinx/'@" "$N"
done

%build
%pyproject_build
PYTHONPATH=`pwd` make -C docs SPHINXBUILD=sphinx-build-3 html

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc docs/_build/html *.rst
%python3_sitelibdir/sphinx_automodapi/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Jan 20 2024 L.A. Kostis <lakostis@altlinux.ru> 0.16.0-alt1
- 0.16.0.
- BR: add serializinghtml module.

* Sat Aug 05 2023 L.A. Kostis <lakostis@altlinux.ru> 0.15.0-alt1
- 0.15.0.
- BR: add fontconfig and basic ttf fonts (otherwise tests will fail).

* Wed Nov 09 2022 Stanislav Levin <slev@altlinux.org> 0.14.1-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Mon Apr 25 2022 Fr. Br. George <george@altlinux.org> 0.14.1-alt1
- Autobuild version bump to 0.14.1

* Mon Apr 25 2022 Fr. Br. George <george@altlinux.ru> 0.14.10-alt1
- Initial build for ALT
