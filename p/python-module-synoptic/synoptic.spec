%define oname synoptic

%def_with python3

Name: python-module-%oname
Version: 2013.1
Release: alt2.1
Summary: An AJAXy notes manager
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/synoptic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Synoptic is "GMail for your notes". It gives you an efficient and
friendly interface that makes it possible to keep and categorize a large
number of small-ish notes and tidbits of information.

The following features set it apart:

* Fully versioned. Never deletes anything, ever. If you want to go back
  to a previous version of something, just drag that slider up there in
  the top-left corner.

* Super-simple Navigation. Adaptive tag clouds, support for the
  forward/back button on your browser, query links, support for browser
  bookmarks. All to make sure you can find that note when you need it.

* Powerful searching. Synoptic is meant to keep large note collections
  manageable and accessible. You can search for items based on tags,
  their creation time, or even search through their full text. Plus
  arbitrary logical combinations of them, using the logical operatos
  and, or, and not.

* Easy Markup. Synoptic uses Markdown to allow you to type formatted
  notes easily and quickly. Plus, there are a few extensions to
  facilitate typing math.

* Advanced Features. A lot of refinement work has gone into making
  Synoptic work as seamlessly as possible. You may never notice many of
  these refinements, because they're meant to make stuff work like it's
  supposed to.

%package -n python3-module-%oname
Summary: An AJAXy notes manager
Group: Development/Python3

%description -n python3-module-%oname
Synoptic is "GMail for your notes". It gives you an efficient and
friendly interface that makes it possible to keep and categorize a large
number of small-ish notes and tidbits of information.

The following features set it apart:

* Fully versioned. Never deletes anything, ever. If you want to go back
  to a previous version of something, just drag that slider up there in
  the top-left corner.

* Super-simple Navigation. Adaptive tag clouds, support for the
  forward/back button on your browser, query links, support for browser
  bookmarks. All to make sure you can find that note when you need it.

* Powerful searching. Synoptic is meant to keep large note collections
  manageable and accessible. You can search for items based on tags,
  their creation time, or even search through their full text. Plus
  arbitrary logical combinations of them, using the logical operatos
  and, or, and not.

* Easy Markup. Synoptic uses Markdown to allow you to type formatted
  notes easily and quickly. Plus, there are a few extensions to
  facilitate typing math.

* Advanced Features. A lot of refinement work has gone into making
  Synoptic work as seamlessly as possible. You may never notice many of
  these refinements, because they're meant to make stuff work like it's
  supposed to.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
2to3 -w -n ../python3/bin/%oname
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%doc README.rst doc/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst doc/*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1
- Initial build for Sisyphus

