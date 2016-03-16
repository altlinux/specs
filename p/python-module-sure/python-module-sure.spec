%define modname sure
%def_with python3

Name: python-module-%modname

Version: 1.2.12
Release: alt2.git20150625.1.1

Summary: Assertion toolbox for python

Group: Development/Python
License: GPLv3+
URL: https://github.com/gabrielfalcao/sure

BuildArch: noarch

%setup_python_module %modname

Source: %modname-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-funcsigs python-module-pbr python-module-setuptools python-module-six python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-mock python-module-nose python3-module-html5lib python3-module-nose python3-module-pbr python3-module-unittest2 rpm-build-python3 time

#BuildRequires: python-module-setuptools python-module-nose
#BuildPreReq: python-module-six python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-module-setuptools python3-module-nose
#BuildPreReq: python3-module-six python3-module-mock
#BuildPreReq: python-tools-2to3
%endif

%description
A Python assertion toolbox that works fine with nose.

%package -n python3-module-%modname
Summary: Assertion toolbox for python
Group: Development/Python3
%add_python3_req_skip UserDict

%description -n python3-module-%modname
A Python assertion toolbox that works fine with nose.

%prep
%setup -n %modname-%version

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
nosetests -v
#if_with python3
%if 0
pushd ../python3
nosetests3 -v
popd
%endif

%files
%doc README.md COPYING
%python_sitelibdir/%modname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modname
%doc README.md COPYING
%python3_sitelibdir/%modname
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.12-alt2.git20150625.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.12-alt2.git20150625.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt2.git20150625
- Fixed for new mock

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt1.git20150625
- Version 1.2.12

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.8-alt1.git20141223
- Version 1.2.8
- Added module for Python 3

* Sat Feb 09 2013 Ivan A. Melnikov <iv@altlinux.org> 1.1.7-alt1
- New version.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus.

