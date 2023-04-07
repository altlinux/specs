%define _unpackaged_files_terminate_build 1
%define pypi_name chevron

Name: python3-module-%pypi_name
Version: 0.14.0
Release: alt1

Summary: Mustache templating language renderer
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/chevron/
Vcs: https://github.com/noahmorrison/chevron.git

BuildArch: noarch

#Source: http://pypi.io/packages/source/c/%pypi_name/%pypi_name-%version.tar.gz
Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %pypi_name

%description
A python implementation of the mustache templating language.

%prep
%setup -n %pypi_name-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Apr 07 2023 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.11.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.1-alt1
- Updated to upstream version 0.11.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1
- Version 0.8.4

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.6-alt1
- Version 0.7.6

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

