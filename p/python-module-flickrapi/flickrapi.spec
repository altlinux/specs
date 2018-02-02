%define oname flickrapi
Name: python-module-%oname
Version: 1.4.4
Release: alt1.1
Summary: The official Python interface to the Flickr API
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/flickrapi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-docutils
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-epydoc

%description
The easiest to use, most complete, and most actively developed Python
interface to the Flickr API.It includes support for authorized and
non-authorized access, uploading and replacing photos, and all Flickr
API functions.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
The easiest to use, most complete, and most actively developed Python
interface to the Flickr API.It includes support for authorized and
non-authorized access, uploading and replacing photos, and all Flickr
API functions.

This package contains documentation for %oname.

%prep
%setup

%build
%python_build_debug

export PYTHONPATH=$PWD
%make -C doc all apidoc

%install
%python_install

install -p -m644 README UPGRADING \
	%buildroot%_docdir/%oname-%version/

%files
%python_sitelibdir/*
%_docdir/%oname-%version

%files docs
%doc doc/apidoc/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus

