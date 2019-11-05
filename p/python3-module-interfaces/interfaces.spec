%define _unpackaged_files_terminate_build 1
%define oname interfaces

Name: python3-module-%oname
Version: 0.0.4
Release: alt2

Summary: Simple decorator implementation of an interface
License: Apache v2
Group: Development/Python3
Url: https://pypi.python.org/pypi/interfaces/
BuildArch: noarch

Source0: https://pypi.python.org/packages/eb/36/2976c3c99aa36ea5a50b60e4f8014a91c20c7561150564abdfd445cb2430/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
This library is a trivial implementation of an interface in Python,
with the following aspects / features:

* It fails at import time, not at construction, so you know
  immediately when you have a problem.
* It's quite simple (very few LOC) and lenient where it counts
* It exclusively uses decorators, so...
* It does not require inheritance (reducing 'forced' subclassing)
* It does not enforce any typing checks
* It is intended to 'enhance' duck typing by avoiding common
  pitfalls (forgot to implement something on your fake duck class,
  overwrote something fundamental, etc.)

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.4-alt2
- disable python2

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus

