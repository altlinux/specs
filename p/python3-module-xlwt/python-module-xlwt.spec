%define oname xlwt

Name: python3-module-xlwt
Version: 1.3.0
Release: alt2

Summary: Library to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

License: BSD-style
Group: Development/Python3
Url: http://www.python-excel.org/
BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %oname-%version.tar
#VCS: https://github.com/python-excel/xlwt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools


%description
Provide a library for developers to use to generate spreadsheet
files compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.

%prep
%setup -q -n %oname-%version

%build
%python3_build

%install
%python3_install

mkdir -p %buildroot%_defaultdocdir/%name/
cp -av README.rst docs examples %buildroot%_defaultdocdir/%name/

%files
%doc %_defaultdocdir/%name/
%python3_sitelibdir/%{oname}*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- Build for python2 disabled.

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.0-alt1
- New version

* Fri Jan 06 2017 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Fri Jun 10 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.2-alt1
- new version 1.1.2

* Tue Jun 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2
- NMU: added python3 module

* Thu Jan 07 2016 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version
- Package all docs and examples

* Thu Mar 27 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.5-alt1
- New version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.1
- Rebuilt with python 2.6

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.7.2-alt1
- new version

* Mon May 04 2009 Alexey Morsov <swi@altlinux.ru> 0.7.1-alt1
- initial build for Sisyphus- 

