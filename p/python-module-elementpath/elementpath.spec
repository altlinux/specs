%define _unpackaged_files_terminate_build 1
%define oname elementpath

%def_with check

Name: python-module-%oname
Version: 1.2.0
Release: alt1

Summary: XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
License: MIT
Group: Development/Python
# Source-git: https://github.com/sissaschool/elementpath
Url: https://pypi.org/project/elementpath/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(lxml)
BuildRequires: python3(lxml)
BuildRequires: python3(tox)
%endif

BuildArch: noarch

%py_requires json
%description
%oname provides XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
structures, both for the standard ElementTree library and for the lxml.etree
library.

%package -n python3-module-%oname
Summary: XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
Group: Development/Python3

%description -n python3-module-%oname
%oname provides XPath 1.0 and 2.0 selectors for Python's ElementTree XML data
structures, both for the standard ElementTree library and for the lxml.etree
library.

%prep
%setup
%patch -p1
# break circle dependencies during testing
# note: xmlschema requires elementpath for testing too
grep -qsF 'xmlschema' tox.ini || exit 1
sed -i '/xmlschema/d' tox.ini
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
LANG=en_US.utf8 tox.py3 --sitepackages -vr -p auto -o

%files
%doc LICENSE README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Sat Aug 17 2019 Stanislav Levin <slev@altlinux.org> 1.2.0-alt1
- Initial build.

