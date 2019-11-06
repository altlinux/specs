%define _unpackaged_files_terminate_build 1
%define oname haven

Name: python3-module-%oname
Version: 1.1.111
Release: alt2

Summary: flask's style binary server framework
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/haven/
# https://github.com/dantezhu/haven.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-events python3-module-netkit python3(setproctitle)
BuildRequires: python-tools-2to3 python3(gevent) python3(geventwebsocket)

%py3_provides %oname
%py3_requires events netkit


%description
flask's style binary server framework.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md examples
%python3_sitelibdir/*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.111-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.111-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.111-alt1
- Updated to upstream version 1.1.111.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.88-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.65-alt1.git20141127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.65-alt1.git20141127.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.65-alt1.git20141127
- Version 1.1.65

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.60-alt1.git20141120
- Initial build for Sisyphus

