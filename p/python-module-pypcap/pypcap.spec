%define _unpackaged_files_terminate_build 1
%define oname pypcap
Name: python-module-%oname
Epoch: 1
Version: 1.1.5
Release: alt1
Summary: Python/C bindings for the libpcap library 
License: BSD
Group: Development/Python
Url: https://github.com/kbandla/pypcap
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kbandla/pypcap.git
Source0: https://pypi.python.org/packages/83/25/dab6b3fda95a5699503c91bf722abf9d9a5c960a4480208e4bad8747dd0c/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools-tests libpcap-devel

%py_provides %oname
Provides: python-module-kbandla-%oname = %EVR
Obsoletes: python-module-kbandla-%oname < %EVR

%description
Python/C bindings for the libpcap library. Most of the functions are 1:1
mapped to the libpcap library.

%prep
%setup -q -n %{oname}-%{version}

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_install

%files
%doc README PKG-INFO
%python_sitelibdir/*

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.1.5-alt1
- automated PyPI update

* Wed Mar 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.3-alt2.git20150224
- Renamed kbandla-%oname -> %oname

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150224
- Initial build for Sisyphus

