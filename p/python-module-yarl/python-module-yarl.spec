%define oname yarl

Name: python-module-%oname
Version: 0.8.1
Release: alt1
Summary: Yet another URL library http://yarl.readthedocs.io
License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/%oname

Source: https://pypi.python.org/packages/10/1b/be30529bde22c85c2975a4e21cf7f13edbcb291350fbbde8bc13938620c8/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests python3-module-pytest-runner python3-module-multidict

%description
The module provides handy URL class for url parsing and changing.

%package -n python3-module-%oname
Summary: Yet another URL library http://yarl.readthedocs.io
Group: Development/Python3

%description -n python3-module-%oname
The module provides handy URL class for url parsing and changing.

%prep
%setup -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files -n python3-module-%oname
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux Sisyphus.
