%define oname fb

Name: python3-module-%oname
Version: 0.4.0
Release: alt2

Summary: Python SDK for the Facebook Graph Api
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/fb/
# https://github.com/blaklites/fb.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
fb is a python sdk for the Facebook Graph Api. The sdk provides three
methods for interacting largely with facebook. publish(), get_object()
and delete() In addtion to the three, there is one helper method to view
the structure of objects returned from facebook, show_fields()

%prep
%setup

%install
install -d %buildroot%python3_sitelibdir
cp -fR %oname %buildroot%python3_sitelibdir/

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.0-alt2
- disable python2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20141005.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.git20141005.1
- NMU: Use buildreq for BR.

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141005
- Initial build for Sisyphus

