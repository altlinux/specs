%define oname nose

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 1.3.7
Release: alt2.git20160316.1

Summary: A unittest-based testing framework for python that makes writing and running tests easier

Group: Development/Python
License: LGPL
#Url: http://code.google.com/p/python-nose/
#Url: https://github.com/nose-devs/nose
Url: http://www.somethingaboutorange.com/mrl/projects/nose/

BuildArch: noarch

%setup_python_module %oname

Source: %name-%version.tar
Patch1: %oname-%version-alt-coverage4.patch

BuildRequires: python-module-setuptools python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildRequires: python3-devel python3-module-coverage
%endif

%description
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.

%if_with python3
%package -n python3-module-%oname
Summary: A unittest-based testing framework for python3 that makes writing and running tests easier
Group: Development/Python3

%description -n python3-module-%oname
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.
%endif

%prep
%setup
%patch1 -p1

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
ln -s nosetests-%_python_version %buildroot%_bindir/nosetests
%if_with python3
ln -s nosetests-%_python3_version %buildroot%_bindir/nosetests3
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
%_bindir/nosetests-%_python_version
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info
%_man1dir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/nosetests3
%_bindir/nosetests-%_python3_version
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:1.3.7-alt2.git20160316.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Oct 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.3.7-alt2.git20160316
- Fixed build with new coverage.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.3.7-alt1.git20160316.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Wed Mar 16 2016 Denis Medvedev <nbr@altlinux.org> 1:1.3.7-alt1.git20160316
- Git upstream merged.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.3.7-alt1.git20150818.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.7-alt1.git20150818
- New snapshot

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.7-alt1.git20150617
- Version 1.3.7

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.4-alt1.git20150217
- New snapshot

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.4-alt1.git20140929
- Version 1.3.4

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.3-alt1.git20140506
- Version 1.3.3

* Wed Sep 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.1-alt1.git20130317.1
- Fixed build

* Sun Mar 17 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.2.1-alt1.git20130317
- new version 1.2.1 (git describe: release_1.2.1-112-g846382d)

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
