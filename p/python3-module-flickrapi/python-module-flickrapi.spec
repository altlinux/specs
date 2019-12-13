%define oname flickrapi

Name: python3-module-%oname
Version: 2.4.0
Release: alt2

Summary: The official Python interface to the Flickr API
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/flickrapi/
BuildArch: noarch

Source: %oname-%version.tar
Patch0: fix_deps_in_setup.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docutils
BuildRequires: python3-module-requests
BuildRequires: python3-module-requests-oauthlib
BuildRequires: python3-module-requests_toolbelt
BuildRequires: python3-module-sphinx


%description
The easiest to use, most complete, and most actively developed Python
interface to the Flickr API.It includes support for authorized and
non-authorized access, uploading and replacing photos, and all Flickr
API functions.

%prep
%setup -n flickrapi-%version
%patch0 -p0

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

export PYTHONPATH=$PWD
%make -C doc html
mkdir man
cp -fR doc/_build/html/* man/

%install
%python3_install

%files
%doc *.txt man/
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.4.0-alt2
- build for python2 disabled

* Tue Mar 27 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.4.0-alt1
- Version 2.4.0
  Fixed deps in setup.py

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus
