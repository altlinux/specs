Name: python3-module-defusedxml
Version: 0.7.1
Release: alt1

Summary: XML bomb protection for Python stdlib modules
License: Python-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/defusedxml/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
defusedxml -- defusing XML bombs and other exploits.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
%__python3 tests.py

%files
%python3_sitelibdir/defusedxml
%python3_sitelibdir/defusedxml-%version-*-info

%changelog
* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7.1-alt1
- 0.7.1 released

* Thu Jun 20 2019 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Autobuild version bump to 0.6.0

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

