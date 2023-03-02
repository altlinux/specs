%define _unpackaged_files_terminate_build 1
%define oname mozinfo

Name: python3-module-%oname
Version: 1.2.2
Release: alt1

Summary: Library to get system information for use in Mozilla testing
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozinfo/
BuildArch: noarch

Source: %oname-%version.tar
Patch0: fix-detect-dist.patch

BuildRequires(pre): rpm-build-python3

Requires: python3-module-six

Conflicts: python-module-%oname

%description
Library to get system information for use in Mozilla testing.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Wed Mar 01 2023 Anton Vyatkin <toni@altlinux.org> 1.2.2-alt1
- new version 1.2.2

* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt2
- Detect dist fixed.

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

