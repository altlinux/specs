%define _unpackaged_files_terminate_build 1
%define oname xmlschema

%ifnarch ppc64le
%def_with check
%else
%def_without check
%endif

Name: python3-module-%oname
Version: 3.3.1
Release: alt1

Summary: XML Schema validator and data conversion library

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/xmlschema
VCS: https://github.com/sissaschool/xmlschema

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(elementpath)
BuildRequires: python3(lxml)

%if_with check
BuildRequires: /proc
BuildRequires: python3(tox)
BuildRequires: python3-module-memory_profiler
# these are optional
BuildRequires: python3-module-mypy
BuildRequires: python3-module-jinja2
# lxml-stubs is not packaged yet
%endif

%description
The xmlschema library is an implementation of XML Schema for Python.

%prep
%setup

%build
export LANG=C.UTF-8
%pyproject_build

%install
%pyproject_install

%check
# Increase verbosity of check
sed -i 's/unittest/unittest -v/' tox.ini
%tox_check_pyproject

%files
%doc LICENSE README.rst
%_bindir/xmlschema-json2xml
%_bindir/xmlschema-validate
%_bindir/xmlschema-xml2json
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Apr 30 2024 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.

* Fri Apr 19 2024 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Tue Apr 09 2024 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt1
- Automatically updated to 3.2.1.

* Thu Mar 28 2024 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Automatically updated to 3.2.0.

* Wed Apr 26 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.3-alt1
- Automatically updated to 2.2.3.

* Tue Mar 07 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.2-alt1
- Automatically updated to 2.2.2.

* Sun Feb 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Build new version.

* Mon Mar 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.2-alt2
- Requires fixed.

* Mon Mar 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.2-alt1
- Version updated to 1.1.2.

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.13-alt2
- Build for python2 disabled.

* Sat Aug 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.13-alt1
- Initial build.

