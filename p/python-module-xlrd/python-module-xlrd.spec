
Name:           python-module-xlrd
Version:        0.9.4
Release:        alt1.1
Summary:        Library to extract data from Microsoft Excel (TM) spreadsheet files

Group:          Development/Python
License:        BSD
URL:            http://www.python-excel.org/
Source0:        http://pypi.python.org/packages/source/x/xlrd/xlrd-%{version}.tar.gz

BuildArch:      noarch

BuildRequires(pre): rpm-build-python
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python3 python3-base
BuildRequires: python-devel rpm-build-python3

#BuildRequires:  python-devel
BuildRequires(pre): rpm-build-python3
#BuildRequires:  python3-devel

Provides:	python-xlrd = %version-%release

%description
Extract data from Excel spreadsheets (.xls and .xlsx, versions 2.0
onwards) on any platform.  Pure Python (2.6, 2.7, 3.2+).  Strongr
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.4-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Version 0.9.4

* Mon Mar 31 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt2
- Increase release to prevent Fedoraimport/Sisyphus warning

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- Import package to ALT Linux from Fedora

