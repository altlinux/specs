Name:           python-module-xlrd
Version:        1.0.0
Release:        alt1
Summary:        Library to extract data from Microsoft Excel (TM) spreadsheet files

Group:          Development/Python
License:        BSD
URL:            http://www.python-excel.org/
Source0:        xlrd-%version.tar
# VCS:		https://github.com/python-excel/xlrd

BuildArch:      noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Provides:	python-xlrd = %version-%release

%description
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0
onwards) on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strong
support for Excel dates.  Unicode-aware.

%package -n python3-module-xlrd
Summary:        Library to extract data from Microsoft Excel (TM) spreadsheet files
Group:          Development/Python3
Provides:	python3-xlrd = %version-%release

%description -n python3-module-xlrd
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0
onwards) on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strongr
support for Excel dates.  Unicode-aware.

%prep
%setup -q -n xlrd-%{version}
mkdir -p ../python3
cp -a * ../python3 ||:

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

# add shebang and remove .py extension
(
  echo '#!/usr/bin/python'
  cat %buildroot%_bindir/runxlrd.py
) >> %buildroot%_bindir/runxlrd
rm -rf %buildroot%_bindir/runxlrd.py* \
  %buildroot/%python_sitelibdir/xlrd/doc \
  %buildroot/%python_sitelibdir/xlrd/examples \
  %buildroot/%python3_sitelibdir/xlrd/doc \
  %buildroot/%python3_sitelibdir/xlrd/examples

%files
%doc xlrd/doc/* xlrd/examples
%_bindir/*
%python_sitelibdir/xlrd/*
%python_sitelibdir/*egg-info

%files -n python3-module-xlrd
%doc xlrd/doc/* xlrd/examples
%python3_sitelibdir/xlrd/*
%python3_sitelibdir/*egg-info

%changelog
* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Mon Mar 31 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt2
- Increase release to prevent Fedoraimport/Sisyphus warning

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Import package to ALT Linux from Fedora

