%define oname defusedxml

Name: python-module-%oname
Version: 0.5.0
Release: alt1
Summary: XML bomb protection for Python stdlib modules
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/defusedxml/

Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
defusedxml -- defusing XML bombs and other exploits.

%package -n python3-module-%oname
Summary: XML bomb protection for Python stdlib modules
Group: Development/Python3

%description -n python3-module-%oname
defusedxml -- defusing XML bombs and other exploits.

%prep
%setup -n %oname-%version

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.txt CHANGES.txt LICENSE
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.txt CHANGES.txt LICENSE
%python3_sitelibdir/*

%changelog
* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt1.hg20130328.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.hg20130328.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1.hg20130328.1
- NMU: Use buildreq for BR.

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.hg20130328
- Initial build for Sisyphus

