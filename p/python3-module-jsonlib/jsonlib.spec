%define oname jsonlib
Name: python3-module-%oname
Version: 1.6.1
Release: alt1
Summary: JSON serializer/deserializer for Python
License: GPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/jsonlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute

%description
JSON is a lightweight data-interchange format. It is often used for
exchanging data between a web server and user agent.

This module aims to produce a library for serializing and deserializing
JSON that conforms strictly to RFC 4627.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus

