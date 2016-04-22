%define py_name imagesize

Name: python-module-%py_name
Version: 0.7.0
Release: alt1

Group: Development/Python
%global short_desc Getting image size from png/jpeg/jpeg2000/gif file in pure Python
Summary: %short_desc
License: MIT
Url: https://github.com/shibukawa/imagesize_py

# https://github.com/shibukawa/imagesize_py
#
# The same source is used for both Python{2,3} with a commit from:
# https://github.com/xantares/imagesize_py py2a3
Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

BuildPreReq: python-module-setuptools
BuildPreReq: python3-module-setuptools

# For %%check:
BuildPreReq: python-module-nose
BuildPreReq: python3-module-nose
# To get all the data for the tests:
BuildPreReq: ImageMagick-tools

%global long_desc It parses image files' header and return image size.\
\
* PNG\
* JPEG\
* JPEG2000\
* GIF

%description
%long_desc

This is a pure Python2 library.

%package -n python3-module-%py_name
Group: Development/Python3
Summary: %short_desc

%description -n python3-module-%py_name
%long_desc

This is a pure Python3 library.

%prep
%setup -c
for py in py2 py3; do
	cp -a %name-%version "$py"
done

%build
pushd py2
%python_build
popd

pushd py3
%python3_build
popd

%install
pushd py2
%python_install
popd

pushd py3
%python3_install
popd

%check
cd %name-%version
convert test/images/test.jp{g,2}
# Just in case:
# make sure we test the installed modules from %%buildroot,
rm -rf imagesize

[ -n "$NOSE_PROCESSES" ] || NOSE_PROCESSES=%__nprocs; export NOSE_PROCESSES # like in %%make_build
PYTHONPATH=%buildroot%python_sitelibdir nosetests test
PYTHONPATH=%buildroot%python3_sitelibdir nosetests3 test

%files
%doc py2/{LICENSE,README}.rst
%python_sitelibdir/%py_name
%python_sitelibdir/%py_name-*.egg-info

%files -n python3-module-%py_name
%doc py3/{LICENSE,README}.rst
%python3_sitelibdir/%py_name
%python3_sitelibdir/%py_name-*.egg-info

%changelog
* Thu Apr 21 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1
- Initial build for ALT Sisyphus. (Needed for sphinx-1.4.1.) (ALT#31976)
- The same source is used for both Python{2,3} with a commit from:
  https://github.com/xantares/imagesize_py/tree/py2a3
