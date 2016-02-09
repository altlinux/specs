%def_disable check

%define mname yieldfrom
%define oname %mname.botocore

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.3
Release: alt3.git20150428
Summary: asyncio port of botocore, the low-level, data-driven core of boto 3
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/yieldfrom.botocore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/rdbhost/yieldfromBotocore.git
# branch: develop
Source: %name-%version.tar

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dateutil
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-dateutil
BuildPreReq: python3-module-nose python3-module-mock
BuildPreReq: python3-module-asyncio
%endif
%py_provides %oname

%description
This is an asyncio port of botocore.

botocore is a low-level interface to a growing number of Amazon Web
Services. The botocore package is the foundation for AWS-CLI.

%if_with python3
%package -n python3-module-%oname
Summary: asyncio port of botocore, the low-level, data-driven core of boto 3
Group: Development/Python3
%py3_provides %oname

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst 
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Feb 09 2016 Sergey Alembekov <rt@altlinux.ru> 0.1.3-alt3.git20150428
- disable sphinx

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 0.1.3-alt2.git20150428
- cleanup buildreq
- disable check

* Fri May 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150428
- New snapshot

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150319
- Version 0.1.3

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150312
- Initial build for Sisyphus

