%define oname xlwt
%def_with python3
Name: python-module-xlwt
Version: 1.2.0
Release: alt1

Summary: Library to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.

License: BSD-style
Group: Development/Python
Url: http://www.python-excel.org/
BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %oname-%version.tar
#VCS: https://github.com/python-excel/xlwt

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif


Requires: python >= 2.4

%description
Provide a library for developers to use to generate spreadsheet
files compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.

%if_with python3
%package -n python3-module-%oname
Summary: Library to generate spreadsheet files compatible with Microsoft Excel versions 95 to 2003.
Group: Development/Python3

%description -n python3-module-%oname
Provide a library for developers to use to generate spreadsheet
files compatible with Microsoft Excel versions 95 to 2003.

The package itself is pure Python with no dependencies on modules or
packages outside the standard Python distribution.
%endif

%prep
%setup -q -n %oname-%version

%if_with python3
rm -rf ../python3
cp -a . ../python3
#pushd ../python3
#find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' + ||:
%endif


%build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES

mkdir -p %buildroot%_defaultdocdir/%name/
cp -av README.rst docs examples %buildroot%_defaultdocdir/%name/

%files -f INSTALLED_FILES
%doc %_defaultdocdir/%name/

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%{oname}*
%endif

%changelog
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

