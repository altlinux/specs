%define _unpackaged_files_terminate_build 1
%define oname mozfile

Name: python3-module-%oname
Version: 3.0.0
Release: alt1

Summary: Library of file utilities for use in Mozilla testing
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozfile/

Source0: https://files.pythonhosted.org/packages/25/f8/a1f0076490d50dbe8bdcf15df97856a4734f459aaf0a4d42c64a11ab7231/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
Library of file utilities for use in Mozilla testing.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Thu Mar 02 2023 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt1
- new version 3.0.0

* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

