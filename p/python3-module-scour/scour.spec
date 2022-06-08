%define oname scour

%def_with check

Name: python3-module-%oname
Version: 0.38.2
Release: alt1

Summary: Scour SVG Optimizer

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/scour/
# https://github.com/oberstet/scour.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-six
%endif

BuildArch: noarch

%py3_provides %oname

%description
Scour is a SVG optimizer/sanitizer that can be used to produce SVGs for
Web deployment.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Wed Jun 08 2022 Grigory Ustinov <grenka@altlinux.org> 0.38.2-alt1
- Automatically updated to 0.38.2.

* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.29-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.29-alt1.git20140726.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.29-alt1.git20140726.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.29-alt1.git20140726.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29-alt1.git20140726
- Initial build for Sisyphus

