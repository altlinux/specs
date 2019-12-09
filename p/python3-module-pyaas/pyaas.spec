%define _unpackaged_files_terminate_build 1
%define oname pyaas

Name: python3-module-%oname
Version: 0.6.1
Release: alt2

Summary: Python-as-a-Service is a set of utilities for creating Tornado applications
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyaas
BuildArch: noarch

# https://github.com/moertle/pyaas.git
Source0: https://pypi.python.org/packages/79/f6/6e3c535a1387e3f0a495568d51921ab65a94fb3a8fe1c79565d82a9c8087/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-zope

%py3_provides %oname
%py3_requires tornado motor


%description
PyaaS, or pyaas, or Python-as-a-Service, is a simple wrapper around
Tornado that makes it quick and easy to rapid deploy new web
applications. It has a settings parser, storage engine, and
authentication modules.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.rst docs
%python3_sitelibdir/*


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.0-alt1.git20150805.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.0-alt1.git20150805.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20150805
- Initial build for Sisyphus

