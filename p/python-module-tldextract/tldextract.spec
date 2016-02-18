%define oname tldextract

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.5.1
Release: alt1.git20141205.1
Summary: Accurately separate the TLD from the registered domain and subdomains of a URL
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/tldextract/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/john-kurkowski/tldextract.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Accurately separate the TLD from the registered domain and subdomains of a URL
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

This package contains tests for %oname.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md tldextract_app
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md tldextract_app
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.1-alt1.git20141205.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20141205
- Initial build for Sisyphus

