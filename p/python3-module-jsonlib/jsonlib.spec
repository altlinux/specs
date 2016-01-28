%define oname jsonlib
Name: python3-module-%oname
Version: 1.6.1
Release: alt1.1.1
Summary: JSON serializer/deserializer for Python
License: GPL
Group: Development/Python3
Url: http://pypi.python.org/pypi/jsonlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-distribute

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python3 python3-base
BuildRequires: python3-devel rpm-build-python3

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
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1.6.1-alt1.1.1
- NMU: Use buildreq for BR.

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.6.1-alt1.1
- Rebuild with Python-3.3

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus

