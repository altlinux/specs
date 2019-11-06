%define _unpackaged_files_terminate_build 1
%define oname pygibson

%def_disable check

Name: python3-module-%oname
Version: 0.2.1
Release: alt2

Summary: Python client for gibson cache server
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pygibson/
# https://github.com/bak1an/pygibson.git

Source0: https://pypi.python.org/packages/49/ce/18e324897ae11b3a9f271e3780fe5ffa169ac980a47eb9c14077f586ebda/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: libgibsonclient-devel

%py3_provides %oname


%description
Python client for gibson cache server.

%prep
%setup -q -n %{oname}-%{version}

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
python3 -m tests.run

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- disable python2

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20131001.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20131001.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20131001
- Initial build for Sisyphus

