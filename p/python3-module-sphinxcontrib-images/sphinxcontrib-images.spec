%define mname sphinxcontrib
%define oname %mname-images

%def_without docs

Name: python3-module-%oname
Version: 0.9.4
Release: alt1

Summary: Sphinx "images" extension
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/sphinxcontrib-images/
# https://github.com/spinus/sphinxcontrib-images.git

Source: %name-%version.tar
# https://github.com/lokesh/lightbox2.git
Source1: lightbox2-0.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests
BuildRequires: python3-module-tox
BuildRequires: python3-module-wheel
%if_with docs
BuildRequires: python3-module-sphinx-devel
%endif

%py3_provides %mname.images
%py3_requires %mname sphinx requests json


%description
sphinxcontrib-images (formerly sphinxcontrib-fancybox).

Features:

* Show thumbnails instead of full size images inside documentation.
* Ability to zoom/enlarge picture using LightBox2 (or any other backend)
* Ability to group pictures
* Download remote pictures (if requested)

%prep
%setup
tar xf %SOURCE1 -C sphinxcontrib_images_lightbox2

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
export LC_ALL=en_US.UTF-8

%python3_build_debug

%install
export LC_ALL=en_US.UTF-8
%python3_install

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html
%endif

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/%mname/*
%python3_sitelibdir/sphinxcontrib_images*


%changelog
* Thu Apr 20 2023 Fr. Br. George <george@altlinux.org> 0.9.4-alt1
- Submajor version upgrade

* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt2
- disable python2

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7.0-alt1.2
- (NMU) rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Updated to upstream version 0.7.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150324.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150324
- Initial build for Sisyphus

