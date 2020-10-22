%define _unpackaged_files_terminate_build 1
%define oname tabulate

%def_with check

Name: python3-module-%oname
Version: 0.8.7
Release: alt1
Summary: Pretty-print tabular data
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/tabulate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(nose)
BuildRequires: python3(tox)
%endif

%description
Pretty-print tabular data in Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
sed -i '/^\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
setenv =\
    py3: _NOSE_BIN=%_bindir\/nosetests3\
commands_pre =\
    \/bin\/cp {env:_NOSE_BIN:} \{envbindir\}\/nosetests\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/nosetests' tox.ini
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc CHANGELOG README
%_bindir/%oname
%python3_sitelibdir/*

%changelog
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

