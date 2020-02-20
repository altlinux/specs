%define _unpackaged_files_terminate_build 1
%define oname xmlschema

%def_with check

Name: python3-module-%oname
Version: 1.0.13
Release: alt2

Summary: XML Schema validator and data conversion library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/xmlschema/

BuildArch: noarch

# Source-git: https://github.com/sissaschool/xmlschema
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(elementpath)
BuildRequires: python3(lxml)

%if_with check
BuildRequires: /proc
BuildRequires: python3(tox)
%endif


%description
The xmlschema library is an implementation of XML Schema for Python.

%prep
%setup
sed -i \
-e 's/elementpath~=/elementpath>=/g' \
-e '/memory_profiler/d' \
tox.ini setup.py

%build
export LANG=C.UTF-8
%python3_build

%install
%python3_install

install -m 0644 ./xmlschema/unicode_categories.json \
%buildroot%python3_sitelibdir/xmlschema/unicode_categories.json

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%oname/tests

%check
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -vr -- -v

%files
%doc LICENSE README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/


%changelog
* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.13-alt2
- Build for python2 disabled.

* Sat Aug 17 2019 Stanislav Levin <slev@altlinux.org> 1.0.13-alt1
- Initial build.

