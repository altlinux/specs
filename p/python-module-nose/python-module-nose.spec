%define oname nose

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 1.1.2
Release: alt1

Summary: A unittest-based testing framework for python that makes writing and running tests easier

Group: Development/Python
License: LGPL
#Url: http://code.google.com/p/python-nose/
Url: http://www.somethingaboutorange.com/mrl/projects/nose/

BuildArch: noarch

%setup_python_module %oname

Source: %oname-%version.tar
Patch1: nose-1.1.2-alt-syntax-error-patch_py.patch

BuildRequires: python-module-setuptools python-module-coverage

%description
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.

%if_with python3
%package -n python3-module-%oname
Summary: A unittest-based testing framework for python3 that makes writing and running tests easier
Group: Development/Python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute python3-module-coverage

%description -n python3-module-%oname
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.
%endif

%prep
%setup -n %oname-%version
%patch1 -p2

sed -i "s|man/man1|share/man/man1|g" setup.py
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
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

rm -f %buildroot%_bindir/nosetests
ln -s nosetests-%__python_version %buildroot%_bindir/nosetests
%if_with python3
ln -s nosetests-%__python3_version %buildroot%_bindir/nosetests3
%endif

%check
./selftest.py
%if_with python3
pushd ../python3
python3 setup.py build_tests
python3 ./selftest.py
popd
%endif

%files
%doc AUTHORS CHANGELOG NEWS README.txt examples/
%_bindir/nosetests
%_bindir/nosetests-%__python_version
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info
%_man1dir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/nosetests3
%_bindir/nosetests-%__python3_version
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Wed Feb 08 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.1.2-alt1
- fix version typo
- build with Python3

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.11.2-alt1
- new version 1.11.2

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.3-alt1.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.11.3-alt1
- 0.11.3
- run tests

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.1-alt1.1
- Rebuilt with python 2.6

* Thu Aug 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.11.1-alt1
- new version 0.11.1 (with rpmrb script)

* Wed Jun 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10.3-alt1
- new version 0.10.3 (with rpmrb script)
- packaging .egg-info too (fix bug #15968)

* Fri May 30 2008 Vitaly Lipatov <lav@altlinux.ru> 0.10.2-alt1
- use python_build/install macroses
- use noarch

* Thu May 29 2008 Andrey Khavryuchenko <akhavr@altlinux.org> 0.10.2-alt0.1
- updated version

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.10.0b1-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 0.10.0b1-alt2
- Build as noarch.

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 0.10.0b1-alt1
- initial build for ALT Linux Sisyphus
