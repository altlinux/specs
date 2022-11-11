%define _unpackaged_files_terminate_build 1
%define pypi_name sphinx-automodapi

%def_with check
Name: python3-module-%pypi_name
Version: 0.14.1
Release: alt2
License: MIT
Source: sphinx-automodapi-%version.tar
Group: Development/Python3
BuildArch: noarch
Summary: A sphinx extension to automatically generate API pages for whole modules

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: /usr/bin/dot
BuildRequires: python3(Cython)
%endif

%py3_provides %pypi_name

%description
This is a Sphinx extension to automatically generate API pages for whole
modules. It was originally developed for the Astropy project but is now
available as a standalone package since it can be used for any other
package. The documentation can be found on
http://sphinx-automodapi.readthedocs.io/en/latest/

%prep
%setup -n sphinx-automodapi-%version
for N in $(grep -rl "python': ('https://docs.python.org/" sphinx_automodapi/tests); do
        sed -i "s@'https://docs.python.org/{0}/'.format(sys.version_info.0.)@'/usr/share/python-sphinx/'@" "$N"
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
* Wed Nov 09 2022 Stanislav Levin <slev@altlinux.org> 0.14.1-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Mon Apr 25 2022 Fr. Br. George <george@altlinux.org> 0.14.1-alt1
- Autobuild version bump to 0.14.1

* Mon Apr 25 2022 Fr. Br. George <george@altlinux.ru> 0.14.10-alt1
- Initial build for ALT
