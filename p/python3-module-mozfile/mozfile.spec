%define _unpackaged_files_terminate_build 1
%define oname mozfile

%def_without check

Name: python3-module-%oname
Version: 1.2
Release: alt2

Summary: Library of file utilities for use in Mozilla testing
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozfile/
BuildArch: noarch

Source0: https://pypi.python.org/packages/83/e2/ea5cbdecefd2fd824a836fc5bd16c254a903e1597e9708fab427b4024e0b/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Library of file utilities for use in Mozilla testing.

%prep
%setup -q -n %{oname}-%{version}

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
%__python3 setup.py test
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

