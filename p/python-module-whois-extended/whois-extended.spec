%define mname whois
%define oname %mname-extended

%def_with python3

Name: python-module-%oname
Version: 0.6.10
Release: alt1.git20150529.1.1
Summary: Python module/library for retrieving WHOIS information of domains
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-whois-extended
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gen1us2k/python-whois.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests whois
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %mname
Conflicts: python-module-%mname < %EVR
Conflicts: python-module-%mname > %EVR
Provides: python-module-%mname = %EVR
Requires: whois

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3

%description
Python module/library for retrieving WHOIS information of domains. Able
to extract data for all the popular TLDs (com, net, org, uk, pl, ru, lv,
jp, co_jp, de, at, eu, biz, info, name, us, co, me, be, nz, cz, it, fr,
kg, vc, fm, tv, edu, ca)

%if_with python3
%package -n python3-module-%oname
Summary: Python module/library for retrieving WHOIS information of domains
Group: Development/Python3
%py3_provides %mname
Conflicts: python3-module-%mname < %EVR
Conflicts: python3-module-%mname > %EVR
Provides: python3-module-%mname = %EVR
Requires: whois

%description -n python3-module-%oname
Python module/library for retrieving WHOIS information of domains. Able
to extract data for all the popular TLDs (com, net, org, uk, pl, ru, lv,
jp, co_jp, de, at, eu, biz, info, name, us, co, me, be, nz, cz, it, fr,
kg, vc, fm, tv, edu, ca)
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.10-alt1.git20150529.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.10-alt1.git20150529.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.10-alt1.git20150529
- Initial build for Sisyphus

