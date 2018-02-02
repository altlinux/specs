%define mname sphinxcontrib
%define oname %mname-images

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.1
Summary: Sphinx "images" extension
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sphinxcontrib-images/

# https://github.com/spinus/sphinxcontrib-images.git
Source: %name-%version.tar
# https://github.com/lokesh/lightbox2.git
Source1: lightbox2.tar

Patch1: %oname-%version-alt-build.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-requests python-module-sphinx-devel
BuildRequires: python-module-tox python-modules-json
BuildRequires: python-module-wheel
BuildRequires: python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-requests python3-module-sphinx-devel
BuildRequires: python3-module-tox
BuildRequires: python3-module-wheel
%endif

%py_provides %mname.images
%py_requires %mname sphinx requests json

%description
sphinxcontrib-images (formerly sphinxcontrib-fancybox).

Features:

* Show thumbnails instead of full size images inside documentation.
* Ability to zoom/enlarge picture using LightBox2 (or any other backend)
* Ability to group pictures
* Download remote pictures (if requested)

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx "images" extension
Group: Development/Python3
%py3_provides %mname.images
%py3_requires %mname sphinx requests json

%description -n python3-module-%oname
sphinxcontrib-images (formerly sphinxcontrib-fancybox).

Features:

* Show thumbnails instead of full size images inside documentation.
* Ability to zoom/enlarge picture using LightBox2 (or any other backend)
* Ability to group pictures
* Download remote pictures (if requested)
%endif

%prep
%setup
%patch1 -p1

pushd sphinxcontrib_images_lightbox2
tar -xf %SOURCE1
popd

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=$PWD
%make -C docs html

%files
%doc *.rst docs/build/html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%mname/*
%python_sitelibdir/sphinxcontrib_images*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/build/html
%_bindir/*.py3
%python3_sitelibdir/%mname/*
%python3_sitelibdir/sphinxcontrib_images*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Updated to upstream version 0.7.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150324.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150324
- Initial build for Sisyphus

