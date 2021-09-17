%define _unpackaged_files_terminate_build 1
%define oname nose

%def_with check

Name: python3-module-%oname
Epoch: 1
Version: 1.3.7
Release: alt9.git20160316

Summary: A unittest-based testing framework for python that makes writing and running tests easier

Group: Development/Python3
License: LGPL
Url: https://nose.readthedocs.io/en/latest/

BuildArch: noarch

Source: %name-%version.tar

# https://github.com/nose-devs/nose/pull/1004
Patch1: %oname-%version-alt-coverage4.patch

# Fix UnicodeDecodeError with captured output
# https://github.com/nose-devs/nose/pull/988
Patch2: python-nose-fedora-unicode.patch

# Allow docutils to read utf-8 source
Patch3: python-nose-fedora-readunicode.patch

# Fix Python 3.6 compatibility
# Python now returns ModuleNotFoundError instead of the previous ImportError
# https://github.com/nose-devs/nose/pull/1029
Patch4: python-nose-fedora-py36.patch

# Fix Python 3.8 compatibility
# Remove a SyntaxWarning (other projects may treat it as error)
Patch5: python-nose-fedora-py38.patch

# setuptools 58
Patch6: nose-1.3.7-2to3-Replace-dynamic-conversion-with-the-static-one.patch
Patch7: nose-1.3.7-build-Migrate-to-setuptools-58.patch
Patch8: nose-1.3.7-tests-Fix-assumptions-for-coverage5.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-coverage

%description
nose provides an alternate test discovery and running process for
unittest, one that is intended to mimic the behavior of py.test as much
as is reasonably possible without resorting to too much magic.

%prep
%setup
%autopatch -p1

sed -i "s|man/man1|share/man/man1|g" setup.py

%build
%python3_build

%install
%python3_install

ln -s nosetests-%_python3_version %buildroot%_bindir/nosetests3
ln -s nosetests-%_python3_version %buildroot%_bindir/nosetests-3

# was packaged in python2-nose, I don't want to add conflict for now
rm %buildroot%_bindir/nosetests

%check
python3 setup.py build_tests
python3 ./selftest.py

%files
%_bindir/nosetests3
%_bindir/nosetests-3
%_bindir/nosetests-%_python3_version
%_man1dir/nosetests.1.*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Sep 16 2021 Stanislav Levin <slev@altlinux.org> 1:1.3.7-alt9.git20160316
- Fixed FTBFS (setuptools 58).

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.3.7-alt8.git20160316
- Drop python2 support.

* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.3.7-alt7.git20160316
- add python 3.8 fix from Fedora
- disable selftest (failed on coverage plugin test, there is not patch)

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1:1.3.7-alt6.git20160316
- Fixed FTBFS.

* Tue Apr 07 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.3.7-alt5.git20160316
- NMU: rebuilt with python 3.8 to update nosetests-%%pyver -> nosetests-3.8

* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.3.7-alt4.git20160316
- added nosetests-2/nosetests-3 for fedora compatibility

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.3.7-alt3.git20160316
- Rebuilt with python-3.6.

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
