%define oname django-friends

%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20130126.1
Summary: Friendship, contact and invitation management for the Django web framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/django-friends/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jtauber/django-friends.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Friendship, contact and invitation management for the Django web
framework.

%package -n python3-module-%oname
Summary: Friendship, contact and invitation management for the Django web framework
Group: Development/Python3
%add_python3_req_skip gdata vobject ybrowserauth

%description -n python3-module-%oname
Friendship, contact and invitation management for the Django web
framework.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20130126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20130126
- Initial build for Sisyphus

