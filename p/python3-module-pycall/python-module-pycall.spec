%define _unpackaged_files_terminate_build 1
%define module_name pycall

Name: python3-module-%module_name
Version: 2.3.0
Release: alt2

Summary: flexible python library for creating and using Asterisk call files
License: Public Domain
Group: Development/Python3
Url: http://pycall.org/
# https://github.com/rdegges/pycall.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/f7/e6/2b3bd63b4b59cd6b3825950ffc80719fb6d5c90a697db73ac03053dd4336/%{module_name}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc AUTHORS README* CHANGES UNLICENSE docs/_build/html
%python3_sitelibdir/pycall
%python3_sitelibdir/*.egg-info


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1-alt1.git20121125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1-alt1.git20121125.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.git20121125
- Version 2.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0-alt1
- Initial build for Sisyphus.
