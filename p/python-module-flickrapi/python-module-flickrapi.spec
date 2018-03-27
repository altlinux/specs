%define oname flickrapi
Name: python-module-%oname
Version: 2.4.0
Release: alt1
Summary: The official Python interface to the Flickr API
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/flickrapi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
Patch0: fix_deps_in_setup.patch
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-setuptools python-devel
BuildRequires: python-module-docutils
BuildRequires: python-module-requests_toolbelt
BuildRequires: python-module-requests
BuildRequires: python-module-requests-oauthlib
BuildPreReq: python-module-sphinx

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-devel
BuildPreReq: python3-module-docutils
BuildPreReq: python3-module-requests_toolbelt
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-requests-oauthlib
BuildPreReq: python3-module-sphinx


%description
The easiest to use, most complete, and most actively developed Python
interface to the Flickr API.It includes support for authorized and
non-authorized access, uploading and replacing photos, and all Flickr
API functions.

%package -n python3-module-%oname
Summary: The official Python interface to the Flickr API
Group: Development/Documentation

%description -n python3-module-%oname
The easiest to use, most complete, and most actively developed Python
interface to the Flickr API.It includes support for authorized and
non-authorized access, uploading and replacing photos, and all Flickr
API functions.

%prep
%setup -n flickrapi-%version
%patch0 -p0

rm -rf ../python3
cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build
popd

export PYTHONPATH=$PWD
%make -C doc html
mkdir man
cp -fR doc/_build/html/* man/

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc *.txt man/
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info

%files -n python3-module-%oname
%doc *.txt man/
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info


%changelog
* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.4.0-alt1
- Version 2.4.0
  Fixed deps in setup.py

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus
