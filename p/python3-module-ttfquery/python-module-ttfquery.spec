%define oname TTFQuery
%define sname ttfquery

Name: python3-module-%sname
Version: 1.0.5
Release: alt4

Summary: FontTools-based package for querying system fonts

Group: Development/Python3
License: BSD
Url: http://ttfquery.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/mindw/ttfquery
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-fonttools
BuildPreReq: python-tools-2to3

Conflicts: python-module-%sname < %EVR
Obsoletes: python-module-%sname < %EVR

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

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc license.txt doc/index.html
%_bindir/*
%python3_sitelibdir/%sname/
%python3_sitelibdir/*egg-info/

%changelog
* Thu Aug 27 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt4
- Fix obsoletes tag.

* Fri Feb 28 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.5-alt3
- Drop python2 support.

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt2
- build from latest https://github.com/mindw/ttfquery

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
