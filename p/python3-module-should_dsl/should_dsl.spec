%define oname should_dsl

Name: python3-module-%oname
Version: 2.1.2
Release: alt2

Summary: Should assertions in Python as clear and readable as possible
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/should_dsl/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
The goal of Should-DSL is to write should expectations in Python as
clear and readable as possible, using "almost" natural language (limited
- sometimes - by the Python language constraints).

In order to use this DSL, you need to import should and should_not
objects from should_dsl module.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 run_examples.py

%files
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.1.2-alt2
- disable python2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.2-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.2-alt1.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

