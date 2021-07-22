%define oname MultipartPostHandler2

Name: python3-module-%oname
Version: 0.1.5
Release: alt1.git20140925.3
Summary: A handler for urllib2 to enable multipart form uploading
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/MultipartPostHandler2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sergiomb2/MultipartPostHandler2.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%description
A handler for urllib2 to enable multipart form uploading.

Enables the use of multipart/form-data for posting forms
add a fix for utf-8 systems.

%prep
%setup

find . -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt examples/*
%python3_sitelibdir/*

%changelog
* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt1.git20140925.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt1.git20140925.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20140925.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140925
- Initial build for Sisyphus

