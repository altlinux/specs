%define oname ybrowserauth
Name: python-module-%oname
Version: 1.2
Release: alt1.svn20080919
Summary: A class for accessing Yahoo! Mail and Photos using BBauth
License: BSD
Group: Development/Python
Url: https://code.google.com/p/django-hotclub/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://django-hotclub.googlecode.com/svn/trunk/external_libs/ybrowserauth/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%description
Lets you add Yahoo! Browser-Based authentication to your applications.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.svn20080919
- Initial build for Sisyphus

