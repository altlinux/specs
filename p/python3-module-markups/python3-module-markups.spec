%define oname   pymarkups
%def_without tests

Name:           python3-module-markups
Version:        3.1.3
Release:        alt1
License:        MIT
Summary:        Wrapper around various text markups
Group:          Development/Python3
URL: 		https://github.com/retext-project/pymarkups

Source0:        %oname-%version.tar

BuildArch:      noarch

BuildPreReq:	rpm-build-python3
BuildPreReq: 	python3-devel python3-module-setuptools /dev/pts

%if_with tests
BuildRequires:  python3-module-docutils
BuildRequires:  python3-module-markdown
BuildRequires:  python3-module-markdown-math
BuildRequires:  python3-module-textile
%endif

BuildArch:      noarch

%description
This module provides a wrapper around various text markup languages.

Available by default are Markdown, reStructuredText and Textile, but you
can easily add your own markups.

%prep
%setup -q -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%if_with tests
python3 setup.py test
%endif

%files
%doc README.rst
%python3_sitelibdir/markups
%python3_sitelibdir/*egg-info

%changelog
* Mon Nov 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.3-alt1
- New version.

* Tue Sep 07 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.

* Sat Mar 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- New version.

* Mon Feb 01 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.
- Build without tests.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version

* Mon Jun 06 2016 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 21 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build in Sisyphus

