%define oname pytest-mock

%def_with python3

Name: python-module-%oname
Version: 1.5.0
Release: alt1
Summary: Thin-wrapper around the mock package for easier use with py.test
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname
Packager: Python Development Team <python@packages.altlinux.org>
BuildArch: noarch

Source: https://pypi.python.org/packages/00/ee/07a76dada65cbafa1f5c8802a0cdb07b21615be482e587743da6b2aa97a4/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools-tests python-module-setuptools_scm
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-tests python3-module-setuptools_scm
%endif

%description
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%package -n python3-module-%oname
Summary: Thin-wrapper around the mock package for easier use with py.test
Group: Development/Python3

%description -n python3-module-%oname
Thin-wrapper around the mock package for easier use with py.test

This plugin installs a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package, but with the benefit of not having
to worry about undoing patches at the end of a test

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3-module-%oname-%version
cp -a . ../python3-module-%oname-%version
%endif

%build
%python_build
%if_with python3
pushd ../python3-module-%oname-%version
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3-module-%oname-%version
python3 setup.py test
popd
%endif

%files
%doc LICENSE *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux Sisyphus.
