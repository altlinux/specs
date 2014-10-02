%define oname jmbo-downloads

%def_with python3

Name: python-module-%oname
Version: 0.0.8
Release: alt1.git20131121
Summary: Trackable downloads for Jmbo
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jmbo-downloads/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/jmbo-downloads.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Jmbo Downloads allows you to easily create and serve downloadable
content on your Jmbo sites. Files are uploaded via the admin interface,
or generated per request, and served by your webserver. These downloads
can then be tracked - Jmbo Downloads, by default, tracks the total
downloads for each item.

To add or modify downloadable content, navigate to Downloads in the
admin interface. A basic download lets you specify the file to be
downloaded and, optionally, a file name to serve the file with. Users
can view all downloads by navigating to www.yoursite.com/downloads.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jmbo Downloads allows you to easily create and serve downloadable
content on your Jmbo sites. Files are uploaded via the admin interface,
or generated per request, and served by your webserver. These downloads
can then be tracked - Jmbo Downloads, by default, tracks the total
downloads for each item.

To add or modify downloadable content, navigate to Downloads in the
admin interface. A basic download lets you specify the file to be
downloaded and, optionally, a file name to serve the file with. Users
can view all downloads by navigating to www.yoursite.com/downloads.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Trackable downloads for Jmbo
Group: Development/Python3

%description -n python3-module-%oname
Jmbo Downloads allows you to easily create and serve downloadable
content on your Jmbo sites. Files are uploaded via the admin interface,
or generated per request, and served by your webserver. These downloads
can then be tracked - Jmbo Downloads, by default, tracks the total
downloads for each item.

To add or modify downloadable content, navigate to Downloads in the
admin interface. A basic download lets you specify the file to be
downloaded and, optionally, a file name to serve the file with. Users
can view all downloads by navigating to www.yoursite.com/downloads.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jmbo Downloads allows you to easily create and serve downloadable
content on your Jmbo sites. Files are uploaded via the admin interface,
or generated per request, and served by your webserver. These downloads
can then be tracked - Jmbo Downloads, by default, tracks the total
downloads for each item.

To add or modify downloadable content, navigate to Downloads in the
admin interface. A basic download lets you specify the file to be
downloaded and, optionally, a file name to serve the file with. Users
can view all downloads by navigating to www.yoursite.com/downloads.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20131121
- Initial build for Sisyphus

