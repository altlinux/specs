%define modulename mwclient

%def_without python3

Name: python-module-mwclient
Version: 0.8.0
Release: alt1

Summary: mwclient is a framework to MediaWiki's API

Group: Development/Python

License: MIT
Url: http://sourceforge.net/projects/mwclient/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# https://github.com/mwclient/mwclient.git
Source: %modulename-%version.tar
BuildArch: noarch

BuildPreReq: rpm-build-python python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %modulename
%py_requires simplejson

%description
Mwclient is a client to the MediaWiki API
and allows access to almost most implemented API functions.

%package -n python3-module-%modulename
Summary: mwclient is a framework to MediaWiki's API
Group: Development/Python3

%description -n python3-module-%modulename
Mwclient is a client to the MediaWiki API
and allows access to almost most implemented API functions.

%prep
%setup -n %modulename-%version

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
%doc *.rst *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc *.rst *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev.git20140622
- Version 0.7dev

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.6.5-alt1
- initial build for ALT Linux Sisyphus
