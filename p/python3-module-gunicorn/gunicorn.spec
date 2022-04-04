%define _unpackaged_files_terminate_build 1
%define oname gunicorn

%def_with check

Name: python3-module-%oname
Version: 20.1.0
Release: alt2

Summary: WSGI HTTP Server for UNIX

License: Mit
Group: Development/Python3
Url: https://pypi.org/project/gunicorn/

Source: %name-%version.tar
Patch1: gunicorn_fix_eventlet_0.30.3+_breaking_changes.patch

BuildArch: noarch

Conflicts: python-module-%oname
Provides: %oname = %version-%release

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%if_with check
BuildRequires: python3-module-gevent
BuildRequires: python3-module-eventlet
BuildRequires: python3-module-coverage
BuildRequires: pytest3
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-mock
%endif

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

%package docs
Summary: Documentation for gunicorn
Group: Development/Documentation
BuildArch: noarch

%description docs
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a
pre-fork worker model ported from Ruby's Unicorn project. The Gunicorn
server is broadly compatible with various web frameworks, simply
implemented, light on server resource usage, and fairly speedy.

This package contains documentation for gunicorn.

%prep
%setup
%autopatch -p1

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build

%install
%python3_install

# compibility
ln -s gunicorn %buildroot%_bindir/gunicorn.py3

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html SPHINXBUILD=sphinx-build-3

%check
PYTHONPATH=$(pwd) py.test3

%files
%doc LICENSE NOTICE THANKS *.rst
%_bindir/gunicorn
%_bindir/gunicorn.py3
%python3_sitelibdir/*

%files docs
%doc docs/build/html examples

%changelog
* Mon Apr 04 2022 Danil Shein <dshein@altlinux.org> 20.1.0-alt2
- fix FTBFS
- spec clean up

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 20.1.0-alt1
- new version 20.1.0 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 20.0.4-alt2
- drop setuptools requires

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 20.0.4-alt1
- new version 20.0.4 (with rpmrb script)
- add gunicorn provides

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 19.9.0-alt3
- build python3 module separately
- cleanup spec, build from tarball

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 19.9.0-alt2
- Fixed testing against Pytest 5.

* Sun Apr 28 2019 Anton Midyukov <antohami@altlinux.org> 19.9.0-alt1
- Updated to upstream version 19.9.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 19.7.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 19.7.1-alt2
- Skip pyrequires aiohttp.wsgi
- Added deprecate gaiohttp worker patch.

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 19.7.1-alt1
- Updated to upstream version 19.7.1.

* Tue Nov 29 2016 Alexey Shabalin <shaba@altlinux.ru> 19.6.0-alt1
- 19.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 19.2.1-alt1.git20150206.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 19.2.1-alt1.git20150206.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.2.1-alt1.git20150206
- Version 19.2.1

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.2.0-alt1.git20141222
- Version 19.2.0

* Mon Aug 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.1.0-alt1.git20140730
- New snapshot

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 19.1.0-alt1.git20140703
- Version 19.1.0

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.1-alt1.git20131125
- Version 18.1

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 18.0-alt1.git20130831
- Version 18.0

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.2-alt1.git20130210
- Version 0.17.2
- Added pickles

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20120604
- Initial build for Sisyphus

