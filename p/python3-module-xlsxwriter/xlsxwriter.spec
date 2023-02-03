%define oname xlsxwriter

Name:    python3-module-%oname
Version: 3.0.8
Release: alt1
Summary: A Python module for creating Excel XLSX files
License: BSD
Group:   Development/Python3
Url:     https://github.com/jmcnamara/XlsxWriter
Packager: Python Development Team <python@packages.altlinux.org>

Source: %oname-%version.tar
#VCS: https://github.com/jmcnamara/XlsxWriter
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: time
# Provides py.test3 for us without the minor version:
BuildRequires: python3-module-pytest >= 3.0.5-alt2

Provides: python-module-%oname = %EVR
Obsoletes: python-module-%oname < %EVR

%description
XlsxWriter is a Python module for writing files in the Excel 2007+ XLSX
file format.

XlsxWriter can be used to write text, numbers, formulas and hyperlinks
to multiple worksheets and it supports features such as formatting and
many more.

%prep
%setup -q -n %oname-%version
# Set correct interpreter for tests
subst "s|'python'|'%__python3'|" setup.py

%build
%python3_build_debug

%install
%python3_install
pushd %buildroot%_bindir
for i in *; do
       cp "$i" "${i}3"
done
popd

%check
%__python3 setup.py test
py.test3 -vv

%files
%doc Changes *.md *.rst examples dev/performance
%_bindir/*.py*
%python3_sitelibdir/*

%changelog
* Fri Feb 03 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.8-alt1
- New version.

* Sat Jan 14 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.7-alt1
- New version.

* Thu Jan 05 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.6-alt1
- New version.

* Sun Jan 01 2023 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- New version.

* Thu Dec 29 2022 Andrey Cherepanov <cas@altlinux.org> 3.0.4-alt1
- New version.

* Mon Feb 28 2022 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- New version.

* Tue Nov 02 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Tue Aug 10 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- New version.

* Tue Aug 10 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Sat Jul 31 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.5-alt1
- New version.

* Mon Jul 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt2
- Conflicts with python-module-%oname.

* Mon Jul 05 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- New version.

* Sun Jul 04 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt2
- Spec cleanup, build only python3 module.
- FTBFS: use versioned python interpreter for tests.

* Wed May 12 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.3-alt1
- New version.

* Fri May 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.2-alt1
- New version.

* Fri Apr 23 2021 Andrey Cherepanov <cas@altlinux.org> 1.4.0-alt1
- New version.

* Fri Apr 16 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.9-alt1
- New version.

* Tue Mar 30 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.8-alt1
- New version.

* Tue Oct 13 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.7-alt1
- New version.

* Thu Sep 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.6-alt1
- New version.

* Wed Sep 23 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.5-alt1
- New version.

* Sat Sep 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.4-alt1
- New version.

* Wed Aug 19 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- New version.

* Fri Aug 07 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.2-alt1
- New version.

* Fri Jul 31 2020 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version.

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.9-alt1
- New version.

* Thu Mar 12 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.8-alt1
- New version.

* Tue Jan 21 2020 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt2
- Build only with Python3.

* Mon Dec 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.7-alt1
- New version.

* Thu Dec 12 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.6-alt1
- New version.

* Thu Nov 14 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version.

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version.

* Mon Sep 16 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.1-alt1
- New version.

* Tue Aug 27 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.9-alt1
- New version.

* Mon May 06 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.8-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- New version.

* Sat Feb 23 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.5-alt1
- New version.

* Sun Feb 10 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.4-alt1
- New version.

* Mon Oct 22 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- New version.

* Mon Sep 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- New version.

* Sat May 19 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- New version.

* Sun Apr 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- New version.

* Tue Apr 10 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- New version.

* Sun Oct 15 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- New version

* Sat Oct 14 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version

* Sat Sep 16 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version

* Wed Sep 06 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.9-alt1
- New version

* Tue Jul 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.8-alt1
- New version

* Sun Jun 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.7-alt1
- New version

* Sun Jan 29 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.6-alt1
- new version 0.9.6

* Sun Jan 29 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt3
- (.spec) simplify: drop %%py{3,}_provides which have no additional value
  (to see clearly whether python.prov fails on a package).

* Sat Jan 28 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt2
- (.spec) adapt build to python3-module-pytest-3.0.5-alt2:
  py.test3 without minor version.

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.3-alt1.git20150806.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.3-alt1.git20150806.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20150806
- Version 0.7.3

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150324
- Version 0.7.1

* Fri Feb 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.git20150223
- Initial build for Sisyphus

