%define oname protorpc

%def_with python3

Name: python-module-%oname
Version: 0.10.0
Release: alt1.git20150723.1.1
Summary: Google Protocol RPC
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/protorpc
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/google/protorpc.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-six python-module-nose
#BuildPreReq: python-module-mox python-module-simplejson
#BuildPreReq: python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-six python3-module-nose
#BuildPreReq: python3-module-mox python3-module-simplejson
#BuildPreReq: python3-module-unittest2
%endif

%py_provides %oname
%py_requires six simplejson

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-linecache2 python-module-pytest python-module-setuptools python-module-six python-module-traceback2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-linecache2 python3-module-pytest python3-module-setuptools python3-module-six python3-module-traceback2 xz
BuildRequires: python-module-mox python-module-nose python-module-setuptools-tests python-module-simplejson python-module-unittest2 python3-module-mox python3-module-nose python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3 time

%description
Google Protocol RPC.

%if_with python3
%package -n python3-module-%oname
Summary: Google Protocol RPC
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
Google Protocol RPC.
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
python setup.py test -v
nosetests -vv protorpc/message_types_test.py protorpc/messages_test.py \
	protorpc/protojson_test.py
%if_with python3
pushd ../python3
python3 setup.py test -v
nosetests3 -vv protorpc/message_types_test.py protorpc/messages_test.py \
	protorpc/protojson_test.py
popd
%endif

%files
%doc *.md experimental demos
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md experimental demos
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.git20150723.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.git20150723.1
- NMU: Use buildreq for BR.

* Tue Aug 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1.git20150723
- Initial build for Sisyphus

