%define _unpackaged_files_terminate_build 1
%define oname numexpr

%def_with check

Name: python3-module-%oname
Version: 2.10.1
Release: alt1
Epoch: 1

Summary: Fast numerical array expression evaluator for Python and NumPy

Group: Development/Python3
License: MIT
URL: https://pypi.org/project/numexpr
VCS: https://github.com/pydata/numexpr

Source: %name-%version.tar
Source1: site.cfg
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel

BuildRequires: gcc-c++ liblapack-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: /proc
BuildRequires: python3(tox)
BuildRequires: python3(numpy.testing)
%endif

%description
The numexpr package evaluates multiple-operator array expressions many
times faster than NumPy can. It accepts the expression as a string,
analyzes it, rewrites it more efficiently, and compiles it to faster
Python code on the fly. It's the next best thing to writing the
expression in C and compiling it with a specialized just-in-time (JIT)
compiler, i.e. it does not require a compiler at runtime.

Also, numexpr has support for the Intel VML (Vector Math Library) --
integrated in Intel MKL (Math Kernel Library) --, allowing nice
speed-ups when computing transcendental functions (like trigonometrical,
exponentials...) on top of Intel-compatible platforms. This support also
allows to use multiple cores in your computations.

%prep
%setup
%autopatch -p1

install -p -m644 %SOURCE1 ./
sed -i 's|@LIBDIR@|%_libdir|' site.cfg
%ifnarch %ix86 x86_64 armh aarch64 ppc64le %e2k
sed -i 's@ openblas,@ blas,@' site.cfg
%endif
sed -i 's|@PYVER@|%_python3_version%_python3_abiflags|' \
	site.cfg

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    # must be synced with CI config (e.g. travis)
    python -c 'import sys, numexpr; sys.exit(0 if numexpr.test().wasSuccessful() else 1)'
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Jul 09 2024 Grigory Ustinov <grenka@altlinux.org> 1:2.10.1-alt1
- Automatically updated to 2.10.1.

* Mon Dec 18 2023 Grigory Ustinov <grenka@altlinux.org> 1:2.8.3-alt2
- Moved on pyproject macros.

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 1:2.8.3-alt1
- new version 2.8.3

* Mon Jun 20 2022 Michael Shigorin <mike@altlinux.org> 1:2.8.1-alt4
- E2K: build with openblas too

* Fri Feb 04 2022 Grigory Ustinov <grenka@altlinux.org> 1:2.8.1-alt3
- Build with check again.

* Sun Jan 23 2022 Grigory Ustinov <grenka@altlinux.org> 1:2.8.1-alt2
- Bootstrap for python3.10.

* Mon Jan 17 2022 Stanislav Levin <slev@altlinux.org> 1:2.8.1-alt1
- 2.7.3 -> 2.8.1.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1:2.7.3-alt1
- new version 2.7.3 (with rpmrb script)

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1:2.6.2-alt6
- Fixed Build Requires.

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1:2.6.2-alt5
- build python3 separately, without tests subpackage

* Wed Feb 20 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.2-alt4
- exclude armh from crippled arches

* Tue Feb 19 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:2.6.2-alt3
- Fixed build on aarch64 and ppc64le.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.6.2-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Feb 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:2.6.2-alt2
- fix build on arm

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:2.6.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.6.2-alt1
- Updated to upstream release 2.6.2

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.4.4-alt1.dev0.git20150815.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:2.4.4-alt1.dev0.git20150815.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.4-alt1.dev0.git20150815
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.4-alt1.dev0.git20150427
- Version 2.4.4.dev0

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.4.1-alt1.git20141130
- Version 2.4.1

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3-alt2.hg20140104
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3-alt1.hg20140104
- New snapshot

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.3-alt1.hg20130908
- Version 2.3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.2-alt1.hg20121113
- New snapshot

* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.2-alt1.hg20120301
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1-alt1.hg20111127.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.hg20111127
- Version 2.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1.svn20110225.1
- Rebuild with Python-2.7

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.svn20110225
- New snapshot

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.svn20101116.1
- Rebuilt for debuginfo

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.svn20101116
- Version 1.5

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100615.1
- Fixed underlinking

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.svn20100615
- Initial build for Sisyphus

