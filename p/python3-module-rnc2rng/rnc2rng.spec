%define _unpackaged_files_terminate_build 0
%define oname rnc2rng

%def_with check

Name: python3-module-%oname
Version: 2.7.0
Release: alt1

Summary: RELAX NG Compact to RELAX NG conversion library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/rnc2rng

Source0: %oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-rply
%endif

%description
Converts RELAX NG schemata in Compact syntax (rnc) to the equivalent schema in the XML-based default RELAX NG syntax.

%prep
%setup -q -n %{oname}-%{version}

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 test.py -v

%files
%doc LICENSE README.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Thu Jul 09 2026 Nikita Panov <nexxy@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus.
