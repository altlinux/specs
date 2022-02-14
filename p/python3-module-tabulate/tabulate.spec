%define _unpackaged_files_terminate_build 1
%define oname tabulate

%def_with check

Name: python3-module-%oname
Version: 0.8.9
Release: alt1
Summary: Pretty-print tabular data
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tabulate/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

%description
Pretty-print tabular data in Python.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc CHANGELOG README
%_bindir/%oname
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/%oname.*
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Mon Feb 14 2022 Stanislav Levin <slev@altlinux.org> 0.8.9-alt1
- 0.8.7 -> 0.8.9 (closes: #41933).

* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.8.7-alt1
- 0.7.3 -> 0.8.7.
- Stopped Python2 package build.

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.3-alt2
- Fixed build spec with pytest3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.3-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1
- Initial build for Sisyphus

