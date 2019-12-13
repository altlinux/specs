%define oname pypandoc

Name: python3-module-%oname
Version: 0.9.3
Release: alt4

Summary: Thin wrapper for pandoc
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pypandoc/
BuildArch: noarch

# https://github.com/bebraw/pypandoc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: pandoc

%py3_provides %oname
Requires: pandoc


%description
Thin wrapper for "pandoc" (MIT).

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.3-alt4
- build for python3 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.3-alt3.git20150226.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 0.9.3-alt3.git20150226
- Recompile for changed site-packages for python3.5

* Wed Feb 24 2016 Denis Medvedev <nbr@altlinux.org> 0.9.3-alt2.git20150226
- back to sisyphus

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20150226
- Version 0.9.3

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150204
- Version 0.9.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.git20140529
- Initial build for Sisyphus

