%define oname multidict

Name: python-module-%oname
Version: 3.1.3
Release: alt1
Summary: Multidicts are useful for working with HTTP headers, URL query args etc

License: ASL 2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/multidict
Packager: Anton Midyukov <antohami@altlinux.org>

Source: https://pypi.python.org/packages/2a/df/eaea73e46a58fd780c35ecc304ca42364fa3c1f4cd03568ed33b9d2c7547/%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests python3-module-Cython python3-module-pytest

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
%setup -n %oname-%version
rm -f multidict/_istr.cpython-35m-x86_64-linux-gnu.so

%build
%python3_build

%install
%python3_install

%files -n python3-module-%oname
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 3.1.3-alt1
- New version 3.1.3

* Sun Jan 15 2017 Anton Midyukov <antohami@altlinux.org> 2.1.4-alt1
- New version 2.1.4

* Fri Aug 05 2016 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux Sisyphus.
