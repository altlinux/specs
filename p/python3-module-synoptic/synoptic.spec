%define oname synoptic

Name: python3-module-%oname
Version: 2013.1
Release: alt3

Summary: An AJAXy notes manager
License: MIT
Group: Development/Python3
Url: http://mathema.tician.de/software/synoptic/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


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

## py2 -> py3
find ./ -type f \( -name '*.py' -o -name '%oname' \) -exec 2to3 -w -n '{}' +

sed -i 's|#!.*/usr/bin/env python.*|#!/usr/bin/env python3|' \
    $(find ./ -type f \( -name '*.py' -o -name '%oname' \))

# losed import after 2to3
sed -i '1i import sys' %oname/query.py
##

%build
%python3_build_debug

%install
%python3_install

%files
%doc README.rst doc/*
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 2013.1-alt3
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2013.1-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2013.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt2
- Added module for Python 3

* Fri Jun 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.1-alt1
- Initial build for Sisyphus

