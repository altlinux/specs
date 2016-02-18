%define _name apsw
%define rel r1
%def_with python3

Name: python-module-%_name
Version: 3.8.3.1
Release: alt1.%rel.1

Summary: Another Python SQLite Wrapper
License: zlib/libpng License
Group: Development/Python
Url: http://rogerbinns.github.io/apsw
Source: https://github.com/rogerbinns/apsw/releases/download/%version-%rel/%_name-%version-%rel.zip

#BuildPreReq: unzip rpm-build-python
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: libsqlite3-devel python-devel python3-devel rpm-build-python3 unzip

#BuildRequires: libsqlite3-devel
#BuildRequires: python-devel python-module-setuptools
%if_with python3
#BuildPreReq: rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
%endif

%description
APSW is a Python wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%package -n python3-module-%_name
Summary: Another Python SQLite Wrapper Python 3 packages
Group: Development/Python3

%description -n python3-module-%_name
APSW is a Python 3 wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python 3.


%prep
%setup -q -n %_name-%version-%rel

%if_with python3
rm -rf ../python3
cp -a . ../python3
find ../python3 -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*
%doc doc/*

%if_with python3
%files -n python3-module-%_name
%python3_sitelibdir/*
%doc doc/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.8.3.1-alt1.r1.1
- NMU: Use buildreq for BR.

* Wed Jul 09 2014 Alexey Shabalin <shaba@altlinux.ru> 3.8.3.1-alt1.r1
- 3.8.3.1
- add python3 package

* Thu May 23 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.15.2-alt1.r1
- 3.7.15.2-r1

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt1.r1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt1.r1.1
- Rebuild with Python-2.7

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 3.7.4-alt1.r1
- 3.7.4-r1

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 3.7.2-alt1.r1
- 3.7.2-r1

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 3.6.22-alt1.r1
- 3.6.22-r1

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.19-alt1.r1.1
- Rebuilt with python 2.6

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.19-alt1.r1
- 3.6.19

* Thu Aug 27 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.17-alt1.r1
- 3.6.17
- build with system libsqlite

* Thu Jun 04 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.14.2-alt1.r1
- 3.6.14.2
- build statically against libsqlite from sqlite-amalgamation-3.6.14.2

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.11-alt1.r1
- 3.6.11
- build statically against libsqlite from sqlite-amalgamation-3.6.13

* Mon Nov 03 2008 Alexey Shabalin <shaba@altlinux.ru> 3.6.3-alt1.r1
- first build for Sisyphus
- thx to aris@ for spec 
- build statically against libsqlite from sqlite-amalgamation-3.6.4

