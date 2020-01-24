%define oname BlazeForm

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: A library for generating and validating HTML forms
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/BlazeForm/
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-FormEncode
BuildRequires: python3-module-BlazeUtils
BuildRequires: python3-module-WebHelpers2


%description
BlazeForm is a library designed to facilitate the
rendering/processing/validating of HTML forms.

Features:

* validation based on FormEncode
* attempting to have complete HTML spec coverage
* extensible rendering system() (don't have to use it)
* will work with multiple WSGI frameworks (Werkzeug currently supported)
* extensive unit tests
* few dependencies: FormEncode, BlazeUtils, WebHelpers

%prep
%setup -q -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Jan 24 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt1
- Updated to upstream version 0.4.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

