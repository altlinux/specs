%define pypi_name pypandoc

# online tests included
%def_disable check

Name: python3-module-%pypi_name
Version: 1.15
Release: alt1

Summary: Thin wrapper for pandoc
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pypandoc/
BuildArch: noarch

Vcs: https://github.com/JessicaTegner/pypandoc.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 python3(wheel) python3(poetry-core)
BuildRequires: pandoc
%{?_enable_check:BuildRequires: python3(pandocfilters) /usr/bin/pdflatex}

%py3_provides %pypi_name
Requires: pandoc

%description
Thin wrapper for "pandoc" (MIT).

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 tests.py

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%doc README.md


%changelog
* Mon Oct 20 2025 Yuri N. Sedunov <aris@altlinux.org> 1.15-alt1
- 1.15 (ALT #56289)

* Mon Jun 29 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Version updated to 1.5.

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

