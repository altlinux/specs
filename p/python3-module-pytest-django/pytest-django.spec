%define _unpackaged_files_terminate_build 1
%define oname pytest-django

%def_with check

Name: python3-module-%oname
Version: 4.5.2
Release: alt1

Summary: A Django plugin for py.test

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/pytest-django/

# https://github.com/pytest-dev/pytest-django.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)

%if_with check
# install_requires=
BuildRequires: python3(pytest)

BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3(pytest-xdist)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_provides %oname

# we have several versions of Django
# so, we cannot rely on auto-requires
%filter_from_requires /^python3(django\(\..*\)\?)/d

%description
pytest-django allows you to test your Django project/applications with
the pytest testing tool.

%prep
%setup
%autopatch -p1

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --console-scripts

%files
%doc AUTHORS *.rst
%python3_sitelibdir/pytest_django/
%python3_sitelibdir/pytest_django-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 25 2022 Stanislav Levin <slev@altlinux.org> 4.5.2-alt1
- 4.0.0 -> 4.5.2.

* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt2
- fix BR

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 4.0.0-alt1
- 3.9.0 -> 4.0.0.

* Thu Jun 04 2020 Stanislav Levin <slev@altlinux.org> 3.9.0-alt1
- 3.5.1 -> 3.9.0.

* Fri Aug 16 2019 Stanislav Levin <slev@altlinux.org> 3.5.1-alt1
- 2.8.0 -> 3.5.1.
- Enabled testing for Python3.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3.1
- rebuild with all requires

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.8.0-alt3
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.0-alt2.git20150303.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 2.8.0-alt2.git20150303
- cleanup buildreq
- disable tests

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.0-alt1.git20150303
- Version 2.8.0

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.0-alt1.git20141012
- Initial build for Sisyphus

