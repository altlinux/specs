%define oname pydap3.2

%def_with python3
%def_without bootstrap

Name: python-module-%oname
Version: 3.2
Release: alt2
Summary: A Python library implementing the Data Access Protocol (DAP, aka OPeNDAP or DODS)
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/dap/
# https://github.com/lukecampbell/pydap.git
BuildArch: noarch

Source: %oname-%version.tar.gz

Requires: python-modules-email
%if_with bootstrap
%py_requires paste.deploy
%py3_requires paste.deploy
%endif
Conflicts: python-module-pydap

BuildRequires: python-module-PasteDeploy python-module-PasteScript 
BuildRequires: python-module-docutils python-module-html5lib python-module-httplib2 
BuildRequires: python-module-matplotlib python-module-pytest 

BuildRequires(pre): rpm-build-python3
%if_with bootstrap
BuildPreReq: python3-module-PasteDeploy python3-module-PasteScript
%endif
BuildPreReq: python3-module-genshi python3-module-httplib2 
BuildPreReq: python3-module-pytest rpm-build-python3 time


%description
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%package -n python3-module-%oname
Summary: Python implementation of the Data Access Protocol (DAP)
Group: Development/Python3
%py3_requires rfc822py3
Conflicts: python3-module-pydap

%description -n python3-module-%oname
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%prep
%setup

%if_with python3
cp -fR . ../python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
popd
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

%files
%doc *.txt *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2-alt1.git20121211.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.2-alt1.git20121211.1
- NMU: Use buildreq for BR.

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.git20121211
- Initial build for Sisyphus

