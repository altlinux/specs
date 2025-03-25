%define pypi_name sphinxcontrib-programoutput
%define modulename %pypi_name

# https://github.com/python/cpython/issues/94741
%def_without check

Name:    python3-module-%modulename
Version: 0.18
Release: alt1

Summary: Sphinx extension for capturing program output

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://github.com/NextThought/sphinxcontrib-programoutput

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-pytest python3-module-docutils
BuildRequires: python3-module-sphinx strace
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
A Sphinx extension to literally insert the output of arbitrary commands into
documents, helping you to keep your command examples up to date.

%prep
%setup -n %modulename-%version
sed -r -i 's/python/python3/' src/sphinxcontrib/programoutput/tests/{test_directive.py,test_command.py,test_cache.py}

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -s src/sphinxcontrib

%files
%python3_sitelibdir/sphinxcontrib/programoutput/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc *.rst

%changelog
* Tue Mar 25 2025 Grigory Ustinov <grenka@altlinux.org> 0.18-alt1
- Automatically updated to 0.18.

* Tue Oct 15 2024 Stanislav Levin <slev@altlinux.org> 0.17-alt2
- Migrated from removed setuptools' test command (see #50996).

* Mon May 17 2021 Grigory Ustinov <grenka@altlinux.org> 0.17-alt1
- Automatically updated to 0.17.
- Enabled tests back.

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt2
- NMU: disable tests, drop tests packing

* Wed Jun 03 2020 Grigory Ustinov <grenka@altlinux.org> 0.16-alt1
- Build new version.
- Build without specsubst scheme.
- Build with check.

* Mon Oct 14 2019 Grigory Ustinov <grenka@altlinux.org> 0.15-alt1
- Build new version.

* Thu Aug 15 2019 Grigory Ustinov <grenka@altlinux.org> 0.14-alt1
- Build new version.
- Build for python3.
- Transfer to specsubst scheme.

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt1.1
- (NMU) rebuild with python3.6

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus
