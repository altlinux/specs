%define oname Naked

%def_disable check

Name: python3-module-%oname
Version: 0.1.32
Release: alt1
Epoch: 1

Summary: A command line application framework

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/Naked/

# https://github.com/chrissimpkins/naked.git
Source: %name-%version.tar

# due commands in bindir
Conflicts: python-module-Naked

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython python3-module-yaml

%py3_use requests
%py3_use yaml

%description
Naked is a new Python command line application framework that is in
development. The current release is a stable, testing release.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%add_optflags -fno-strict-aliasing
%python3_build_debug
pushd lib/%oname/toolshed/c
rm -f *.c
sed 's|cython|cython3|' cythonize.sh
./cythonize.sh
%python3_build_debug
popd

%install
export LC_ALL=en_US.UTF-8
%python3_install
%python3_prune

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -m644 lib/%oname/toolshed/c/build/lib*/*.so \
	 %buildroot%python3_sitelibdir/%oname/toolshed/c/

rm -f %buildroot%python3_sitelibdir/%oname/toolshed/c/*.sh \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/*.c \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/*.pyx \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/setup.py \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/__pycache__/setup.*

%check
export LC_ALL=en_US.UTF-8
export PATH=$PATH:%buildroot%_bindir
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd tests
sed -i 's|nosetests|nosetests3|' test.sh
./test.sh all
popd

%files
%doc *.md docs/*
%_bindir/naked
%python3_sitelibdir/*

%changelog
* Tue Apr 04 2023 Anton Vyatkin <toni@altlinux.org> 1:0.1.32-alt1
- (NMU) New version 0.1.32.

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1:0.1.31-alt2
- build python3 module

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.1.31-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.1.31-alt1
- Updated to upstream version 0.1.31.
- Returned to upstream version naming.
- Updated build dependencies.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.29-alt2.git20140316.1.1.1
- (AUTO) subst_x86_64.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.29-alt2.git20140316.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.0.29-alt2.git20140316.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt2.git20140316
- Added necessary requirements

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt1.git20140316
- Initial build for Sisyphus

