%define _unpackaged_files_terminate_build 1
%define oname blessed

%def_with check

Name: python3-module-%oname
Version: 1.17.10
Release: alt1

Summary: A feature-filled fork of Erik Rose's blessings project
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/blessed/
# https://github.com/jquast/blessed.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: /dev/pts
BuildRequires: python3(curses)
BuildRequires: python3(mock)
BuildRequires: python3(pytest)
BuildRequires: python3(six)
BuildRequires: python3(tox)
BuildRequires: python3(wcwidth)
BuildRequires: terminfo-extra
%endif

%py3_requires wcwidth curses

%description
A feature-filled fork of Erik Rose's blessings project.

%prep
%setup
%autopatch -p1

# don't package Windows Terminal
rm blessed/win_terminal.py

sed -i 's|#!/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vv -r

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Oct 14 2020 Stanislav Levin <slev@altlinux.org> 1.17.10-alt1
- 1.17.5 -> 1.17.10.

* Thu May 07 2020 Stanislav Levin <slev@altlinux.org> 1.17.5-alt1
- 1.14.2 -> 1.17.5.
- Enabled testing.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.14.2-alt2
- disable python2

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.14.2-alt1
- Version 1.14.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.9.5-alt1.git20150112.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.5-alt1.git20150112.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.5-alt1.git20150112
- Initial build for Sisyphus
