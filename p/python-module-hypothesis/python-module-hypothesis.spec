%define oname hypothesis

%def_with python3

Name: python-module-%oname
Version: 3.6.1
Release: alt1
Summary: A library for property based testing
License: MPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname
Packager: Python Development Team <python@packages.altlinux.org>
BuildArch: noarch

Source: https://pypi.python.org/packages/a8/87/b7ca49efe52d2b4169f2bfc49aa5e384173c4619ea8e635f123a0dac5b75/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools-tests
%endif

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%package -n python3-module-%oname
Summary: A library for property based testing for Python 3
Group: Development/Python3

%description -n python3-module-%oname
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup -n %oname-%version
%if_with python3
rm -rf ../python3-module-%oname-%version
cp -a . ../python3-module-%oname-%version
%endif

%if_with docs
%prepare_sphinx doc
ln -s ../objects.inv doc/en/
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
python3 setup.py test
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
