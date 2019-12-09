%define _unpackaged_files_terminate_build 1
%define oname argparse_tools

Name: python3-module-%oname
Version: 1.0.6
Release: alt2

Summary: Share a standardized set of argparse arguments within your codebase
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/argparse_tools/
BuildArch: noarch

# https://github.com/adgaudio/argparse_tools.git
Source0: https://pypi.python.org/packages/2a/e3/71c4febc0bcf2d37ead2da1fe584ebf0d9f33c889f3d8d8f06d8de16bb05/%{oname}-%{version}.zip

BuildRequires(pre): rpm-build-python3
BuildRequires: unzip
BuildRequires: python3-module-nose python3-module-pytest

%py3_provides %oname


%description
This package wraps argparse to facilitate sharing a standardized set of
arguments across various scripts and applications that may use argparse.

%package examples
Summary: Examples for %oname
Group: Development/Python3
Requires: %name = %EVR

%description examples
This package wraps argparse to facilitate sharing a standardized set of
arguments across various scripts and applications that may use argparse.

This package contains examples for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
nosetests3
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/examples

%files examples
%python3_sitelibdir/*/examples


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.6-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.dev0.git20150126.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.dev0.git20150126.1
- NMU: Use buildreq for BR.

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.dev0.git20150126
- Initial build for Sisyphus

