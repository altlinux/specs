%define modname cairosvg
%define eggname CairoSVG

%def_with check

Name:               python3-module-cairosvg
Version:            2.7.1
Release:            alt1
Summary:            A Simple SVG Converter for Cairo

Group:              Development/Python3
License:            LGPLv3+
URL:                https://pypi.org/project/CairoSVG/
VCS:		    https://github.com/Kozea/CairoSVG.git
Source0:            %name-%version.tar

BuildArch:          noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:      python3-module-setuptools
BuildRequires: 	    python3-module-wheel
%if_with check
BuildRequires: 	    python3-module-pytest
BuildRequires:      python3-module-cairocffi
BuildRequires:      libcairo
BuildRequires:      python3-module-cssselect2
BuildRequires:      python3-module-Pillow
BuildRequires:      python3-module-tinycss2
BuildRequires:      python3-module-defusedxml
%endif
Requires:           python3-module-pycairo

Conflicts: python-module-cairosvg
Obsoletes: python-module-cairosvg

%description
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

For further information, please visit the CairoSVG Website
http://www.cairosvg.org

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

# remove tests
rm -rf %buildroot%python3_sitelibdir/%modname/test_api.py
rm -rf %buildroot%python3_sitelibdir/%modname/__pycache__/test_api.*

%check
%pyproject_run_pytest -v --ignore test_non_regression

%files
%doc README.rst NEWS.rst
%_bindir/cairosvg
%python3_sitelibdir/%modname/
%python3_sitelibdir/%eggname-%version.dist-info

%changelog
* Fri Jan 26 2024 Anton Vyatkin <toni@altlinux.org> 2.7.1-alt1
- New version 2.7.1.

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.20-alt2
- Drop python2 support.

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.20-alt1.2
- Rebuild with python3.7.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.20-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Mon Apr 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.20-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.19-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.19-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.19-alt1
- New version
- Build from upstream Git repository

* Sun Oct 25 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.18-alt1
- New version

* Tue Oct 13 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.17-alt1
- New version

* Sun Sep 20 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.16-alt1
- New version

* Wed Mar 04 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.13-alt1
- New version

* Sun Aug 24 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt1
- New version

* Mon May 12 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version

* Tue Mar 25 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.6-alt1
- New version

* Wed Feb 19 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Import from Fedora
