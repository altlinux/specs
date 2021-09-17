%define _unpackaged_files_terminate_build 1
%define oname parse_type

%def_with check

Name: python3-module-%oname
Version: 0.5.6
Release: alt2
Summary: parse_type extends the parse module (opposite of string.format())
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.org/project/parse-type/

# https://github.com/jenisys/parse_type.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(parse)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%py3_requires parse

%description
Simplifies to build parse types based on the parse module.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/parse_type/
%python3_sitelibdir/parse_type-%version-py%_python3_version.egg-info/

%changelog
* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 0.5.6-alt2
- Fixed FTBFS (setuptools 58).

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 0.5.6-alt1
- 0.4.2 -> 0.5.6.
- Stopped build for Python2.

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt3
- Fixed testing against Pytest 5.

* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2
- Dropped BR on argparse.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt1
- Updated to upstream version 0.4.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1.dev.git20140505.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt1.dev.git20140505.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.dev.git20140505.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.dev.git20140505
- Initial build for Sisyphus

