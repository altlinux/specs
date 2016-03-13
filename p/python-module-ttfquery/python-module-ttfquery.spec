%define oname TTFQuery
%define sname ttfquery

%def_with python3

Name: python-module-%sname
Version: 1.0.5
Release: alt1.bzr20120206.1

Summary: FontTools-based package for querying system fonts

Group: Development/Python
License: BSD-like
Url: http://ttfquery.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

%setup_python_module %oname

BuildRequires: python-devel python-module-setuptools python-module-fonttools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-fonttools
BuildPreReq: python-tools-2to3
%endif

%description
TTFQuery builds on the FontTools package to allow the Python programmer
to accomplish a number of tasks:

  * query the system to find installed fonts
  * retrieve metadata about any TTF font file (even those not yet
    installed)
      o abstract family type
      o proper font name
      o glyph outlines
  * build simple metadata registries for run-time font matching

With these functionalities, it is possible to readily
create OpenGL solid-text rendering libraries which
can accept abstract font-family names as font specifiers
and deliver platform-specific TTF files to match those libraries.

TTFQuery doesn't provide rendering services, but a sample
implementation can be found in the OpenGLContext project, from
which TTFQuery was refactored.

%package -n python3-module-%sname
Summary: FontTools-based package for querying system fonts
Group: Development/Python3

%description -n python3-module-%sname
TTFQuery builds on the FontTools package to allow the Python programmer
to accomplish a number of tasks:

  * query the system to find installed fonts
  * retrieve metadata about any TTF font file (even those not yet
    installed)
      o abstract family type
      o proper font name
      o glyph outlines
  * build simple metadata registries for run-time font matching

With these functionalities, it is possible to readily
create OpenGL solid-text rendering libraries which
can accept abstract font-family names as font specifiers
and deliver platform-specific TTF files to match those libraries.

TTFQuery doesn't provide rendering services, but a sample
implementation can be found in the OpenGLContext project, from
which TTFQuery was refactored.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc license.txt doc/index.html
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%sname/
%python_sitelibdir/*egg-info/

%if_with python3
%files -n python3-module-%sname
%doc license.txt doc/index.html
%_bindir/*.py3
%python3_sitelibdir/%sname/
%python3_sitelibdir/*egg-info/
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.bzr20120206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.bzr20120206
- Snapshot from bzr
- Added module for Python 3

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1
- Version 1.0.5

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- build as noarch

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus
