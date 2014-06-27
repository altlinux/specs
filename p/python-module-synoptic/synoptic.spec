%define oname synoptic
Name: python-module-%oname
Version: 2013.1
Release: alt1
Summary: An AJAXy notes manager
License: MIT
Group: Development/Python
Url: http://mathema.tician.de/software/synoptic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools

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

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc README.rst doc/*
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1
- Initial build for Sisyphus

