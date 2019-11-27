%define _unpackaged_files_terminate_build 1
%define oname tblib

Name: python3-module-%oname
Version: 1.3.0
Release: alt2

Summary: Traceback fiddling library. Allows you to pickle tracebacks
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tblib/
BuildArch: noarch

# https://github.com/ionelmc/python-tblib.git
Source0: https://pypi.python.org/packages/52/aa/aefcbf6b2976fc91d5c32c4014f40e2202654279654cc509b613d7cf5568/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires six


%description
Traceback fiddling library. For now allows you to pickle tracebacks and
raise exceptions with pickled tracebacks in different processes. This
allows better error handling when running code over multiple processes
(imagine multiprocessing, billiard, futures, celery etc).

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst tests
%python3_sitelibdir/*


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20150727.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.git20150727.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150727
- Version 1.1.0

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150112
- Initial build for Sisyphus

