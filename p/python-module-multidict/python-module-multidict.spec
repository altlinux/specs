%define oname multidict

Name: python-module-%oname
Version: 2.0.1
Release: alt1
Summary: Multidicts are useful for working with HTTP headers, URL query args etc

License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/multidict
#Url: https://github.com/aio-libs/multidict
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: gcc python3-devel python3-module-setuptools-tests python3-module-Cython python3-module-pytest

%description
HTTP Headers and URL query string require specific data structure: multidict.
It behaves mostly like a dict but it can have several values for the same key.

%package -n python3-module-%oname
Summary: Multidicts are useful for working with HTTP headers, URL query args etc
Group: Development/Python
%py3_provides %oname

%description -n python3-module-%oname
HTTP Headers and URL query string require specific data structure: multidict.
It behaves mostly like a dict but it can have several values for the same key.
Python 3 version.

%prep
%setup

cp -fR . ../python3

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir py.test-3.5 -v

%files -n python3-module-%oname
%doc LICENSE README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux Sisyphus.
