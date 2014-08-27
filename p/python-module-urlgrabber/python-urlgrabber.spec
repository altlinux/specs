%define real_name urlgrabber

%def_without python3

Summary: High-level cross-protocol url-grabber
Name: python-module-urlgrabber
Version: 3.10.1
Release: alt1.git20140204
License: LGPL
Group: Development/Python
URL: http://urlgrabber.baseurl.org/
# git://yum.baseurl.org/urlgrabber.git
Source: urlgrabber-%{version}.tar
Patch: python-urlgrabber-2.9.6-reget.patch
BuildArch: noarch
Provides: urlgrabber
# Automatically added by buildreq on Mon Dec 17 2007
BuildRequires: python-devel python-modules-compiler python-modules-email python-modules-logging

BuildPreReq: python-module-pycurl
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-pycurl
BuildPreReq: python-tools-2to3 python3-module-rfc822py3
%endif

%description
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%package -n python3-module-%real_name
Summary: High-level cross-protocol url-grabber
Group: Development/Python3

%description -n python3-module-%real_name
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%prep
%setup -n %real_name-%version
#patch0 -p1 -b .reget

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install --prefix="%_prefix"
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install --prefix="%_prefix"
mv %buildroot/usr/libexec/urlgrabber-ext-down %buildroot%_bindir/

%files
%doc ChangeLog README TODO
%_docdir/%real_name-%version/*
%_bindir/%real_name
%_bindir/urlgrabber-ext-down
%python_sitelibdir/%real_name/*

%if_with python3
%files -n python3-module-%real_name
%doc ChangeLog README TODO
%_bindir/%real_name.py3
%python3_sitelibdir/%real_name/*
%endif

%changelog
* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt1.git20140204
- Version 3.10.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.0-alt1.1.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1.1
- Rebuilt with python 2.6

* Tue Apr 29 2008 Mikhail Pokidko <pma@altlinux.org> 3.1.0-alt1
- Version up

* Mon Dec 17 2007 Mikhail Pokidko <pma@altlinux.org> 2.9.7-alt1
- Initial ALT build
