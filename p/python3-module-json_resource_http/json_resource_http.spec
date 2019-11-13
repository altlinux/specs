%define oname json_resource_http

Name: python3-module-%oname
Version: 0.1.3
Release: alt2

Summary: HTTP queryset backend for json resources
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/json_resource_http/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-json_resource python3-module-nose
BuildRequires: python3-module-requests python3-module-mock
BuildRequires: python3-module-json_patch

%py3_provides %oname


%description
HTTP queryset backend for json resources. Makes it possible to use
json-schema api's as if they were local.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.3-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus

