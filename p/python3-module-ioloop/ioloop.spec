%define oname ioloop

Name: python3-module-%oname
Version: 0.1
Release: alt3

Summary: Simple IOloop by epoll or kqueue
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ioloop/
# https://github.com/mengzhuo/ioloop.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Simple IOloop by epoll or kqueue.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
2to3 -w -n test.py
%__python3 setup.py test
%__python3 test.py

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.a.git20141215.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.a.git20141215
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.a.git20141215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.a.git20141215
- Initial build for Sisyphus

