%define _unpackaged_files_terminate_build 1
%define oname path

%def_with check

Name: python3-module-%oname
Version: 13.2.0
Release: alt1

Summary: A module wrapper for os.path
License: MIT
Group: Development/Python
Url: https://github.com/jaraco/path

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(appdirs)
BuildRequires: python3(packaging)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%py3_provides %oname
Provides: python3-module-path.py = %EVR
Obsoletes: python3-module-path.py < %EVR

%description
path implements a path objects as first-class entities, allowing
common operations on files to be invoked on those path objects directly.

%prep
%setup
%patch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

# don't package tests
rm -f %buildroot%python3_sitelibdir/test_path.py

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
sed -i -e '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
tox.ini

export LC_ALL=C.UTF-8
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='LC_ALL'
export TOXENV=py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -vv -r

%files
%doc *.rst
%python3_sitelibdir/path/
%python3_sitelibdir/path-%version-py%_python3_version.egg-info/

%changelog
* Tue Apr 21 2020 Stanislav Levin <slev@altlinux.org> 13.2.0-alt1
- 12.0.1 -> 13.2.0.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 12.0.1-alt2
- Fixed testing against Pytest 5.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 12.0.1-alt1
- 11.5.0 -> 12.0.1.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 11.5.0-alt1
- 7.2 -> 11.5.0.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 7.2-alt1.git20150122.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 7.2-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.2-alt1.git20150122
- Version 7.2

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.3-alt1.git20140823
- Version 5.3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.2.990-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.2.2.990-alt1
- Initial build for Sisyphus.
