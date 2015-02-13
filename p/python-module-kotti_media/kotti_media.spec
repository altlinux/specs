%define oname kotti_media
Name: python-module-%oname
Version: 0.7
Release: alt1.dev.git20150122
Summary: Add media content to your Kotti site
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/kotti_media/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/disko/kotti_media.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-kotti python-module-js.jquery_form
BuildPreReq: python-module-js.mediaelement python-module-fanstatic
BuildPreReq: python-module-pyramid python-module-SQLAlchemy
BuildPreReq: python-module-zope.sqlalchemy python-module-waitress
BuildPreReq: python-module-pyramid_zcml python-module-pyramid_tm
BuildPreReq: python-module-pyramid_debugtoolbar
BuildPreReq: python-module-pyramid_chameleon python-module-kotti_tinymce
BuildPreReq: python-module-pyramid_mako

%py_provides %oname
%py_requires kotti js.jquery_form js.mediaelement fanstatic pyramid
%py_requires sqlalchemy

%description
This is an extension to the Kotti CMS that allows you to add audio and
video to your Kotti site.

kotti_media uses MediaElementJS for video and audio views and thus
supports native HTML5 playback on all platforms that support this. Each
video can have multiple formats (MP4 (.h264 baseline profile), WebM,
Ogg/Theora) to achieve this goal. For audio, supported formats include
mp3 and wav. For older Platforms MediaElementJS includes a Adobe Flash /
MS Silverlight plugin fallback, so that every resopurce can be played on
every platform if all supported formats are uploaded.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is an extension to the Kotti CMS that allows you to add audio and
video to your Kotti site.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev.git20150122
- Initial build for Sisyphus

