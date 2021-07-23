%define _unpackaged_files_terminate_build 1
%define oname PyContracts

%def_with check

Name: python3-module-%oname
Version: 1.8.12
Release: alt2

Summary: Declare constraints on function parameters and return values
License: LGPLv3
Group: Development/Python3
# https://github.com/AndreaCensi/contracts.git
Url: https://pypi.org/project/PyContracts/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(decorator)
BuildRequires: python3(future)
BuildRequires: python3(nose)
BuildRequires: python3(numpy)
BuildRequires: python3(pyparsing)
BuildRequires: python3(six)
%endif

BuildArch: noarch
%py3_provides PyContracts
%py3_requires decorator

%description
%oname is a Python package that allows to declare constraints on function
parameters and return values. It supports a basic type system, variables
binding, arithmetic constraints, and has several specialized contracts (notably
for Numpy arrays).

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install

for i in testing tests docs;
do
    [ -d "%buildroot%python_sitelibdir/%oname/$i" -o \
     -d "%buildroot%python3_sitelibdir/%oname/$i" ] && \
    { echo "There should be no packaged $i"; exit 1; }
done

%check
nosetests3 -v

%files
%doc *.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/contracts/

%changelog
* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.8.12-alt2
- Drop python2 support.

* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 1.8.12-alt1
- Initial build for Sisyphus.

