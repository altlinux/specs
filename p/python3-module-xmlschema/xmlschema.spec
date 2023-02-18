%define _unpackaged_files_terminate_build 1
%define oname xmlschema

%def_without check

Name: python3-module-%oname
Version: 2.2.1
Release: alt1

Summary: XML Schema validator and data conversion library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/xmlschema/
Vcs: https://github.com/sissaschool/xmlschema

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(elementpath)
BuildRequires: python3(lxml)

%if_with check
BuildRequires: /proc
BuildRequires: python3(tox)
BuildRequires: python3-module-memory_profiler
%endif

%description
The xmlschema library is an implementation of XML Schema for Python.

%prep
%setup

%build
export LANG=C.UTF-8
%python3_build

%install
%python3_install

%check
%tox_check

%files
%doc LICENSE README.rst
%_bindir/xmlschema-json2xml
%_bindir/xmlschema-validate
%_bindir/xmlschema-xml2json
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
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

