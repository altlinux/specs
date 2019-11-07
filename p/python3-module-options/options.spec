%define oname options

Name: python3-module-%oname
Version: 1.4.8
Release: alt2

Summary: Simple, super-flexible options. Does magic upon request.
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/options
BuildArch: noarch

Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-chainmap python3-module-combomethod
BuildRequires: python3-module-stuf python3-module-six python3-module-pytest
BuildRequires: python3-module-nulltype python3-module-tox
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme

%py3_provides %oname
%py3_requires stuf six nulltype


%description
options helps represent option and configuration data in a clean,
high-function way. Changes to options can "overlay" earlier or default
settings.

%prep
%setup
%patch1 -p1

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%check
export PYTHONPATH=$PWD
py.test3 --assert=plain -vv

%files
%doc *.rst docs/_build/html
%python3_sitelibdir/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.8-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.8-alt1
- Updated to upstream version 1.4.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.2-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus

