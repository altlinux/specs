%define oname ladon

Name: python3-module-%oname
Version: 0.9.40
Release: alt2

Summary: Several web service interfaces at once, including JSON-WSP, SOAP and JSON-RPC
License: LGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/ladon/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jinja2
BuildRequires: python3(sphinx_bootstrap_theme)

%py3_provides %oname
%py3_requires jinja2 json


%description
Ladon is a framework for exposing python methods to several internet
service protocols. Once a method is ladonized it is automatically served
through all the interfaces that your ladon installation contains. Ladon
is easily extendable. Adding a new service interface is as easy as
adding a single module containing a class inheriting the BaseInterface
class.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	$(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
	$(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

rm -rf %buildroot%python3_sitelibdir/*/test.* ||:
rm -rf %buildroot%python3_sitelibdir/*/*/test.* ||:

%check
python3 setup.py test

%files
%doc *.rst examples
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.40-alt2
- disable python2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.40-alt1.1.qa1
- NMU: applied repocop patch

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.40-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.40-alt1
- Updated to upstream version 0.9.40.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.10-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.10-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1
- Initial build for Sisyphus

