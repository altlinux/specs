%define mname yieldfrom
%define oname %mname.botocore

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt1.git20150428
Summary: asyncio port of botocore, the low-level, data-driven core of boto 3
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.botocore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rdbhost/yieldfromBotocore.git
# branch: develop
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-jmespath python-module-dateutil
BuildPreReq: python-module-yieldfrom.http.client
BuildPreReq: python-module-yieldfrom.urllib3
BuildPreReq: python-module-yieldfrom.requests
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-jmespath python3-module-dateutil
BuildPreReq: python3-module-yieldfrom.http.client
BuildPreReq: python3-module-yieldfrom.urllib3
BuildPreReq: python3-module-yieldfrom.requests
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-asyncio
%endif
BuildPreReq: python3-module-sphinx-devel

%py_provides %oname
%py_requires %mname jmespath dateutil yieldfrom.http.client asyncio
%py_requires yieldfrom.urllib3 yieldfrom.requests

%description
This is an asyncio port of botocore.

botocore is a low-level interface to a growing number of Amazon Web
Services. The botocore package is the foundation for AWS-CLI.

%if_with python3
%package -n python3-module-%oname
Summary: asyncio port of botocore, the low-level, data-driven core of boto 3
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname jmespath dateutil yieldfrom.http.client asyncio
%py3_requires yieldfrom.urllib3 yieldfrom.requests

%description -n python3-module-%oname
This is an asyncio port of botocore.

botocore is a low-level interface to a growing number of Amazon Web
Services. The botocore package is the foundation for AWS-CLI.
%endif

%prep
%setup

ln -s LICENSE.txt license.txt

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug

%prepare_sphinx docs
ln -s ../objects.inv docs/source/
export PYTHONPATH=$PWD
%make -C docs html
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst docs/build/html
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst ../python3/docs/build/html
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri May 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150428
- New snapshot

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150319
- Version 0.1.3

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150312
- Initial build for Sisyphus

