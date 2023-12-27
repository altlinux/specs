%define oname mf2py

%def_with check

Name: python3-module-%oname
Version: 2.0.1
Release: alt1

Summary: Python Microformats2 parser
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mf2py
VCS: https://github.com/microformats/mf2py
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-mock
%endif

%py3_provides %oname

%description
Python parser for microformats 2. Full-featured and mostly stable.
Implements the full mf2 spec, including backward compatibility with
microformats1.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Wed Dec 27 2023 Anton Vyatkin <toni@altlinux.org> 2.0.1-alt1
- New version 2.0.1.

* Thu Jun 29 2023 Anton Vyatkin <toni@altlinux.org> 1.1.3-alt1
- New version 1.1.3

* Thu Mar 09 2023 Anton Vyatkin <toni@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1.git20170715.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1.git20170715
- Updated to current upstream version.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150205
- Initial build for Sisyphus

