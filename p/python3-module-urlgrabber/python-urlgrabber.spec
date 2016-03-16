%define real_name urlgrabber

Summary: High-level cross-protocol url-grabber
Name: python3-module-urlgrabber
Version: 3.10.1
Release: alt1.git20140204.1
License: LGPL
Group: Development/Python3
URL: http://urlgrabber.baseurl.org/
# git://yum.baseurl.org/urlgrabber.git
Source: urlgrabber-%{version}.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-pycurl
BuildPreReq: python-tools-2to3 python3-module-six

%description
python-urlgrabber is a high-level cross-protocol url-grabber for python
supporting HTTP, FTP and file locations. Features include keepalive, byte
ranges, throttling, authentication, proxies and more.

%prep
%setup -n %real_name-%version

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install --prefix="%_prefix"
mv %buildroot/usr/libexec/urlgrabber-ext-down %buildroot%_bindir/

pushd %buildroot%_bindir
for i in $(ls); do
	sed -i 's|#! /usr/bin/python|#! /usr/bin/python3|' $i
	2to3 -w -n $i
	mv $i $i.py3
done
popd

%files
%doc ChangeLog README TODO
%_docdir/%real_name-%version/*
%_bindir/*
%python3_sitelibdir/%real_name/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.10.1-alt1.git20140204.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.1-alt1.git20140204
- Initial build for Sisyphus

