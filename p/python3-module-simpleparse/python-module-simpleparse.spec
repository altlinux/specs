%define oname simpleparse
Name: python3-module-%oname
Version: 3.0.0
Release: alt1.a1.bzr20140102.1

Summary: A Parser Generator for Python (w/mxTextTools derivative)

Group: Development/Python3
License: BSD-like
Url: https://code.launchpad.net/~mcfletch/simpleparse/pure-python

# bzr branch lp:~mcfletch/simpleparse/pure-python
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python-modules

%description
Provides a moderately fast parser generator for use with Python,
includes a forked version of the mxTextTools text-processing library
modified to eliminate recursive operation and fix a number of
undesirable behaviours.

Converts EBNF grammars directly to single-pass parsers for many
largely deterministic grammars.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Provides a moderately fast parser generator for use with Python,
includes a forked version of the mxTextTools text-processing library
modified to eliminate recursive operation and fix a number of
undesirable behaviours.

Converts EBNF grammars directly to single-pass parsers for many
largely deterministic grammars.

This package contains documentation for %oname

%prep
%setup

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
pushd doc/pydoc
python builddocs.py
popd

%files
%doc license.txt
%python3_sitelibdir/simpleparse/
%python3_sitelibdir/*.egg-info

%files docs
%doc doc/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.0-alt1.a1.bzr20140102.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0-alt1.a1.bzr20140102
- Initial build for Sisyphus

