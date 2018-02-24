# we do not have python3(gtk)
%def_without python3bin
%def_with python3
%define oname fonttools
%define modulename fontTools

Name: %oname
Version: 3.22.0
Release: alt1

Summary: Converts OpenType and TrueType fonts to and from XML

Group: Development/Tools
License: LGPL
URL: https://github.com/fonttools/fonttools/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/fonttools/fonttools/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-compat >= 1.2
BuildRequires: xorg-sdk
# python-module-PyXML python-module-ctypes
BuildRequires: python-devel python-module-setuptools python-module-numpy

%if_with python3
%add_python3_req_skip Res calldll macfs
BuildRequires(pre): rpm-build-python3
# python3-module-PyXML python3-module-ctypes
BuildRequires: python3-devel python3-module-setuptools python3-module-numpy
%endif

%if_with python3bin
Requires: python3-module-%oname = %EVR
%else
Requires: python-module-%oname = %EVR
%endif

%global desc \
FontTools/TTX is a library to manipulate font files from Python. It supports \
reading and writing of TrueType/OpenType fonts, reading and writing of AFM \
files, reading (and partially writing) of PS Type 1 fonts. The package also \
contains a tool called TTX which converts TrueType/OpenType fonts to and \
from an XML-based format.

%description
%desc

%package -n python-module-%oname
Group: Development/Python
Summary: Python 2 fonttools library

%description -n python-module-%oname
%desc

%if_with python3
%package -n python3-module-%oname
Group: Development/Python3
Summary: Python 3 fonttools library

%description -n python3-module-%oname
%desc
%endif

%prep
%setup

sed -i '1d' Lib/fontTools/mtiLib/__init__.py

# macOS
#rm Lib/fontTools/ttLib/test/ttBrowser.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3bin
%python_install
pushd ../python3
%python3_install
popd
%else
%if_with python3
pushd ../python3
%python3_install
popd
# we do not have python3(gtk)
rm -f %buildroot/%python3_sitelibdir/%modulename/inspect.py*
rm -f %buildroot/%python3_sitelibdir/%modulename/__pycache__/inspect.*
%endif
%python_install
%endif

%files
%_bindir/ttx
%_bindir/pyft*
%_bindir/fonttools
%_man1dir/*

%files -n python-module-%oname
%python_sitelibdir/%modulename/
%python_sitelibdir/%oname-%version-py%__python_version.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%oname-%version-py%__python3_version.egg-info
%endif

%changelog
* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.22.0-alt1
- new version 3.22.0 (with rpmrb script)

* Wed Feb 07 2018 Vitaly Lipatov <lav@altlinux.ru> 3.21.2-alt1
- new version 3.21.2 (with rpmrb script)

* Mon Dec 04 2017 Igor Vlasenko <viy@altlinux.ru> 3.20.0-alt1
- new version 3.20.0
- added python3 subpackage
- renamed to fonttools

* Tue Nov 07 2017 Vitaly Lipatov <lav@altlinux.ru> 3.18.0-alt1
- new version 3.18.0 (with rpmrb script)

* Sun Oct 08 2017 Vitaly Lipatov <lav@altlinux.ru> 3.15.1-alt1
- new version 3.15.1 (with rpmrb script)

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- new version 3.0

* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version (2.5) with rpmgs script

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4 (with rpmrb script)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 21 2011 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- updated to 2.3

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1.1.1
- Rebuild with Python-2.7

* Mon Jul 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.1
- Rebuild with python 2.6

* Sun Nov 30 2008 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Linux Sisyphus
