%define _unpackaged_files_terminate_build 1
BuildRequires: python3-tools
%define oldname python-module-urljr
Name: python3-module-urljr
Version: 1.0.1
Release: alt1

Summary: URL-related utilites

Group: Development/Python3
License: LGPL
Url: http://www.openidenabled.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

%global modulename urljr
%global packagename python3-module-%{modulename}
BuildRequires(pre): rpm-build-python3

Source: http://openidenabled.com/files/python-openid/files/python-urljr-%version.tar.bz2

# Automatically added by buildreq on Sat Nov 11 2006
BuildRequires: python3-devel python-modules-encodings

%description
URL-related utilites, including a common interface to HTTP fetchers for
PycURL and urllib2.

%prep
%setup -n python-%modulename-%version

%build
2to3-3.3 -w -n .
2to3-3.3 -w -d -n .
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*

%changelog
* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.1.1
- python3 copycat import

