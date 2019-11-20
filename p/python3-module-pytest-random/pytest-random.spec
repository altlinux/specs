%define oname pytest-random

%def_disable check

Name: python3-module-%oname
Version: 0.02
Release: alt3

Summary: py.test plugin to randomize tests
License: MPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/pytest-random/
# https://github.com/klrmn/pytest-random.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides random_plugin


%description
randomize your py.test run.

The randomization algorithm is not the least bit sophisticated, so do
not depend on this plugin for a specific degree of randomness. Please
use the --verbose option to see the randomization for yourself.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.02-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.02-alt2.git20130421.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.02-alt2.git20130421.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.02-alt2.git20130421
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.02-alt1.git20130421
- Initial build for Sisyphus

