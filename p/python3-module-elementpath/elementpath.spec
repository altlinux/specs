%define _unpackaged_files_terminate_build 1
%define oname elementpath

%def_without check

Name: python3-module-%oname
Version: 4.0.1
Release: alt1

Summary: XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/elementpath/

BuildArch: noarch

# Source-git: https://github.com/sissaschool/elementpath
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(lxml)
BuildRequires: python3(tox)
%endif


%description
%oname provides XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
structures, both for the standard ElementTree library and for the lxml.etree
library.

%prep
%setup

# break circle dependencies during testing
# note: xmlschema requires elementpath for testing too
grep -qsF 'xmlschema' tox.ini || exit 1
sed -i '/xmlschema/d' tox.ini

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
LANG=en_US.utf8 tox.py3 --sitepackages -vr -p auto -o

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Build new version.

* Mon Mar 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.3-alt2
- Version updated to 1.4.3.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt2
- Build for python2 disabled.

* Sat Aug 17 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build.

