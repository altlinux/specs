%define _unpackaged_files_terminate_build 1

%define oname BarkingOwl

Name: python3-module-%oname
Version: 0.8.1
Release: alt3

Summary: Scalable web scraper framework for finding documents on websites
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/BarkingOwl/

BuildArch: noarch

# https://github.com/thequbit/BarkingOwl.git
Source0: https://pypi.python.org/packages/a2/6d/f3d53fbbc1f616835345dfce105f2a33e556dae0b6b6cf6e5ed8ebeca17b/%{oname}-%{version}.tar.gz
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
BarkingOwl is a scalable web crawler intended to be used to find
specific document types on websites, such as PDFs, XLS, TXT, HTML, etc.

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p2

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Wed Feb 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.1-alt3
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt2
- Fixed build.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1
- automated PyPI update

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.git20150209
- Version 0.6.5

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4.1-alt1.git20150125
- Version 0.6.4.1

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20150122
- Version 0.6.0

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150119
- Initial build for Sisyphus

