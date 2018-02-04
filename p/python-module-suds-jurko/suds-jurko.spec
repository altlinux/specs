%define oname suds-jurko

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1.dev0.hg20140629.1.1
Summary: Lightweight SOAP client (Jurko's fork)
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/suds-jurko/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/jurko/suds
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides suds
Conflicts: python-module-suds

%description
Based on the original 'suds' project by Jeff Ortel (jortel at redhat
dot com) hosted at 'http://fedorahosted.org/suds'.

'Suds' is a lightweight SOAP-based web service client for Python
licensed under LGPL (see the LICENSE.txt file included in the
distribution).

This is hopefully just a temporary fork of the original suds Python
library project created because the original project development seems
to have stalled. Should be reintegrated back into the original project
if it ever gets revived again.

%package -n python3-module-%oname
Summary: Lightweight SOAP client (Jurko's fork)
Group: Development/Python3
%py3_provides suds
Conflicts: python3-module-suds

%description -n python3-module-%oname
Based on the original 'suds' project by Jeff Ortel (jortel at redhat
dot com) hosted at 'http://fedorahosted.org/suds'.

'Suds' is a lightweight SOAP-based web service client for Python
licensed under LGPL (see the LICENSE.txt file included in the
distribution).

This is hopefully just a temporary fork of the original suds Python
library project created because the original project development seems
to have stalled. Should be reintegrated back into the original project
if it ever gets revived again.

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

%files
%doc *.rst *.txt notes/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.txt notes/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7-alt1.dev0.hg20140629.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.dev0.hg20140629.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev0.hg20140629
- Initial build for Sisyphus

