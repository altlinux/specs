%def_with python3
%define modname cairosvg
%define eggname CairoSVG

Name:               python-module-cairosvg
Version:            1.0.19
Release:            alt1.1
Summary:            A Simple SVG Converter for Cairo

Group:              Development/Python
License:            LGPLv3+
URL:                http://cairosvg.org/
# VCS:		    git://github.com/Kozea/CairoSVG.git
Source0:            http://pypi.python.org/packages/source/C/%{eggname}/%{eggname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires(pre): rpm-build-python
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python3 python3-base
BuildRequires: python-devel rpm-build-python3

#BuildRequires:      python-devel
#BuildRequires:      python-module-pycairo

Provides:	    python-cairosvg = %version-%release

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:      python3-devel
#BuildRequires:      python3-module-pycairo
%endif

%description
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

For further information, please visit the CairoSVG Website
http://www.cairosvg.org

%if_with python3
%package -n python3-module-cairosvg
Summary:            A Simple SVG Converter for Cairo
Group:              Development/Python3

Requires:           python3-module-pycairo

%description -n python3-module-cairosvg
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

For further information, please visit the CairoSVG Website
http://www.cairosvg.org
%endif

%prep
%setup -q -n %{eggname}-%{version}

%build
%python_build

%if_with python3
python3 setup.py build
%endif

%install
%if_with python3
python3 setup.py install --skip-build --root=%buildroot
mv %buildroot%_bindir/{,python3-}cairosvg
%endif

%python_install

%files
%doc README.rst COPYING NEWS.rst TODO.rst
%_bindir/cairosvg
%python_sitelibdir/%modname/
%python_sitelibdir/%{eggname}-%{version}*

%if_with python3
%files -n python3-module-cairosvg
%doc README.rst COPYING NEWS.rst TODO.rst
%_bindir/python3-cairosvg
%python3_sitelibdir/%modname/
%python3_sitelibdir/%{eggname}-%{version}-*
%endif

%changelog
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
