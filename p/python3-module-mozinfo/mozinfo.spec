%define _unpackaged_files_terminate_build 1
%define oname mozinfo

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Library to get system information for use in Mozilla testing
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozinfo/
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mozfile python-tools-2to3

Conflicts: python-module-%oname


%description
Library to get system information for use in Mozilla testing.

%prep
%setup -q -n %{oname}-%{version}

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
# %%__python3 setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt1
- Version updated to 1.2.1
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt1
- Updated to upstream version 0.10.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Added necessary requirements
- Enabled testing

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

