%define oname cloud_sptheme
Name: python-module-%oname
Version: 1.6
Release: alt1
Summary: A nice sphinx theme named 'Cloud', and some related extensions
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/cloud_sptheme/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

%description
This is a small package containing a Sphinx theme named "Cloud", along
with some related Sphinx extensions.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc CHANGES README
%python_sitelibdir/*

%changelog
* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Initial build for Sisyphus

