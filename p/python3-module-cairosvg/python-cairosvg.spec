%define modname cairosvg
%define eggname CairoSVG

Name:               python3-module-cairosvg
Version:            1.0.20
Release:            alt2
Summary:            A Simple SVG Converter for Cairo

Group:              Development/Python3
License:            LGPLv3+
URL:                http://cairosvg.org/
# VCS:		    git://github.com/Kozea/CairoSVG.git
Source0:            http://pypi.python.org/packages/source/C/%{eggname}/%{eggname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires(pre): rpm-build-python3
Requires:           python3-module-pycairo

Conflicts: python-module-cairosvg
Obsoletes: python-module-cairosvg

%description
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

For further information, please visit the CairoSVG Website
http://www.cairosvg.org

%prep
%setup -n %{eggname}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root=%buildroot

%files
%doc README.rst COPYING NEWS.rst TODO.rst
%_bindir/cairosvg
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{eggname}-%{version}-*

%changelog
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
