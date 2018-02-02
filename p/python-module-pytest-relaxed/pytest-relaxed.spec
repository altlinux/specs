%define _unpackaged_files_terminate_build 1
%define oname pytest-relaxed

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: Relaxed test discovery/organization for pytest
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/pytest-relaxed

# https://github.com/bitprophet/pytest-relaxed.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest
BuildRequires: python-module-decorator
BuildRequires: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-decorator
BuildRequires: python3-module-six
%endif

%description
pytest-relaxed provides 'relaxed' test discovery for pytest.

It is the spiritual successor to https://pypi.python.org/pypi/spec,
but is built for pytest instead of nosetests,
and rethinks some aspects of the design
(such as increased ability to opt-in to various behaviors.)

%if_with python3
%package -n python3-module-%oname
Summary: Relaxed test discovery/organization for pytest
Group: Development/Python3

%description -n python3-module-%oname
pytest-relaxed provides 'relaxed' test discovery for pytest.

It is the spiritual successor to https://pypi.python.org/pypi/spec,
but is built for pytest instead of nosetests,
and rethinks some aspects of the design
(such as increased ability to opt-in to various behaviors.)
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py build_ext -i
PYTHONPATH=%buildroot%python_sitelibdir py.test -vv
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
PYTHONPATH=%buildroot%python3_sitelibdir py.test3 -vv
popd
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Initial build for ALT.
