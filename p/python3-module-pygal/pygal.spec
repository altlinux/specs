%define _unpackaged_files_terminate_build 1
%define oname pygal

%def_with check

Name: python3-module-%oname
Version: 3.0.0
Release: alt1
Summary: A python svg graph plotting library
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/pygal/

# https://github.com/Kozea/pygal.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(cairosvg)
BuildRequires: python3(lxml)
BuildRequires: python3(pyquery)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
pygal is a dynamic SVG charting library written in python. All the
documentation is on http://pygal.org

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install
mv %buildroot%_bindir/pygal_gen.py{,3}

# don't package tests
rm -r %buildroot%python3_sitelibdir/%oname/test/

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc CHANGELOG README*
%_bindir/pygal_gen.py3
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.4.0 -> 3.0.0.

* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 2.4.0-alt2
- Fixed FTBFS(Pytest 6).

* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 2.4.0-alt1
- 1.6.1 -> 2.4.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.1-alt2.git20141121.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.6.1-alt2.git20141121
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141121
- Initial build for Sisyphus

