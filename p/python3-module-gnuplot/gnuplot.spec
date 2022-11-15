%define origname gnuplot-py
%define oname gnuplot

Name: python3-module-%oname
Version: 1.8
Release: alt1.git20120706.1.3

Summary: Python interface to Gnuplot

License: LGPLv2.1
Group: Development/Python3
Url: http://%origname.sourceforge.net/
# https://github.com/oblalex/gnuplot.py-py3k.git
Source: %origname-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: fakeroot fontconfig fonts-bitmap-misc gnuplot-common gnuplot-common-x11 libX11-locales libgdk-pixbuf libpdflib-lite libwayland-client libwayland-server python-base python-modules python3 python3-base python3-module-numpy xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb
BuildRequires: gnuplot python3-module-numpy-testing rpm-build-python3 xvfb-run

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: libnumpy-py3-devel gnuplot xvfb-run

%py3_provides Gnuplot
Requires: gnuplot

%add_python3_self_prov_path %buildroot%python3_sitelibdir/Gnuplot

%description
Gnuplot.py is a Python package that allows you to create graphs
from within Python using the gnuplot plotting program.

%package tests
Summary: Tests for Gnuplot.py
Group: Development/Python3
Requires: %name = %EVR

%description tests
Gnuplot.py is a Python package that allows you to create graphs
from within Python using the gnuplot plotting program.

This package contains tests for Gnuplot.py.

%package doc
Summary: Documentation for Gnuplot.py
Group: Development/Documentation
BuildArch: noarch

%description doc
Gnuplot.py is a Python package that allows you to create graphs
from within Python using the gnuplot plotting program.

This package contains documentation for Gnuplot.py.

%prep
%setup -n %origname-%version

%build
# remove crap
rm -f gp_cygwin.py gp_java.py gp_mac* gp_win32.py gnuplot_Suites.py

%python3_build
chmod 644 *.txt

%install
%python3_install

install -d %buildroot%_docdir/%name
cp -fR doc/Gnuplot/* %buildroot%_docdir/%name/

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
xvfb-run python3 test.py -v

%files
%doc *.txt *.html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*

%files doc
%_docdir/%name

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.8-alt1.git20120706.1.3
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.8-alt1.git20120706.1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8-alt1.git20120706.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.8-alt1.git20120706.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.git20120706
- Initial build.

