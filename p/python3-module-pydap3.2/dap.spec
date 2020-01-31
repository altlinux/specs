%define oname pydap3.2

Name: python3-module-%oname
Version: 3.2
Release: alt3

Summary: A Python library implementing the Data Access Protocol (DAP, aka OPeNDAP or DODS)
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/dap/
BuildArch: noarch

# https://github.com/lukecampbell/pydap.git
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-genshi python3-module-httplib2
BuildRequires: python3-module-pytest python-tools-2to3

Conflicts: python3-module-pydap
%py3_requires rfc822py3


%description
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.2-alt3
- Build for python2 disabled.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.2-alt2.1
- fix requires

* Thu May 17 2018 Andrey Bychkov <mrdrew@altlinux.org> 3.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2-alt1.git20121211.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.2-alt1.git20121211.1
- NMU: Use buildreq for BR.

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1.git20121211
- Initial build for Sisyphus

