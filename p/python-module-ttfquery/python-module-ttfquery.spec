%define oname TTFQuery
Name: python-module-ttfquery
Version: 1.0.1
Release: alt2.1.1

Summary: FontTools-based package for querying system fonts

Group: Development/Python
License: BSD-like
Url: http://ttfquery.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/ttfquery/%oname-%version.tar.gz

BuildArch: noarch

%setup_python_module %oname

BuildPreReq: rpm-build-compat >= 1.2

BuildRequires: python-devel python-module-setuptools python-module-fonttools

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
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc license.txt
%python_sitelibdir/ttfquery/
%python_sitelibdir/*egg-info/

%changelog
* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1.1
- Rebuild with Python-2.7

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.1
- Rebuilt with python 2.6

* Fri Feb 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- build as noarch

* Mon Dec 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Linux Sisyphus
