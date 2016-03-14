%define oname pysvg

Name: python3-module-%oname
Version: 0.2.2
Release: alt1.svn20121111.1
License: BSD
Group: Development/Python3
Summary: Pure Python library to create/load and manipulate SVG documents
# http://pysvg.googlecode.com/svn/trunk/pySVG/
Source: %oname-%version.zip
BuildArch: noarch
URL: http://codeboje.de/pysvg

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel unzip python3-module-setuptools
BuildPreReq: python-tools-2to3

%description
pySVG is a pure Python library to create SVG documents. Essentially it
is a python wrapper around svg with the goal to allow people to "program
svg". pySVG can be used to produce svg as an outcome of algorithms you
implement (like koch curves, Lindenmayr systems etc.)

Working with pySVG is pretty straightforward. There is a small tutorial
in the docs folder but i would suggest refering to the testclasses in
the source.

%prep
%setup -n %oname-%version
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc doc/*
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt1.svn20121111.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.svn20121111
- Initial build for Sisyphus

