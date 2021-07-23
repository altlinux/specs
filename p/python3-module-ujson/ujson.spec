%define _unpackaged_files_terminate_build 1
%define oname ujson

Name: python3-module-%oname
Version: 1.35
Release: alt2
Summary: Ultra fast JSON encoder and decoder for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/ujson/

# https://github.com/esnme/ultrajson.git
Source0: https://pypi.python.org/packages/16/c4/79f3409bc710559015464e5f49b9879430d8f87498ecdc335899732e5377/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.5+ and 3.

%prep
%setup -n %{oname}-%{version}

%install
%add_optflags -fno-strict-aliasing
%python3_build_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.35-alt2
- Drop python2 support.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.35-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.34-alt1.git20140416.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.34-alt1.git20140416
- Initial build for Sisyphus

