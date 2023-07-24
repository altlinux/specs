%define _unpackaged_files_terminate_build 1
%define oname elementpath

%def_with check

Name: python3-module-%oname
Version: 4.1.4
Release: alt1

Summary: XPath 1.0 and 2.0 selectors for Python's ElementTree XML data

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/elementpath
VCS: https://github.com/sissaschool/elementpath

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-lxml
%endif

BuildArch: noarch

%description
%oname provides XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
structures, both for the standard ElementTree library and for the lxml.etree
library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# test_validate_json_to_xml and test_validate_analyzed_string needs xmlschema
%pyproject_run_pytest -k"not test_validate_json_to_xml and \
                         not test_validate_analyzed_string"

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Jul 24 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.4-alt1
- Automatically updated to 4.1.4.

* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.2-alt1
- Automatically updated to 4.1.2.

* Mon Apr 24 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt1
- Automatically updated to 4.1.1.

* Thu Mar 23 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Build new version.

* Mon Mar 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- Version updated to 1.4.3.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt2
- Build for python2 disabled.

* Sat Aug 17 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build.

