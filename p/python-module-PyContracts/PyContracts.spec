%define _unpackaged_files_terminate_build 1
%define oname PyContracts

%def_with check

Name: python-module-%oname
Version: 1.8.12
Release: alt1

Summary: Declare constraints on function parameters and return values
License: LGPLv3
Group: Development/Python
# https://github.com/AndreaCensi/contracts.git
Url: https://pypi.org/project/PyContracts/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(decorator)
BuildRequires: python2.7(future)
BuildRequires: python2.7(nose)
BuildRequires: python2.7(numpy)
BuildRequires: python2.7(pyparsing)
BuildRequires: python2.7(six)
BuildRequires: python3(decorator)
BuildRequires: python3(future)
BuildRequires: python3(nose)
BuildRequires: python3(numpy)
BuildRequires: python3(pyparsing)
BuildRequires: python3(six)
%endif

BuildArch: noarch
%py_provides PyContracts
%py_requires decorator

%description
%oname is a Python package that allows to declare constraints on function
parameters and return values. It supports a basic type system, variables
binding, arithmetic constraints, and has several specialized contracts (notably
for Numpy arrays).

%package -n python3-module-%oname
Summary: Declare constraints on function parameters and return values
Group: Development/Python3
%py3_provides PyContracts
%py3_requires decorator

%description -n python3-module-%oname
%oname is a Python package that allows to declare constraints on function
parameters and return values. It supports a basic type system, variables
binding, arithmetic constraints, and has several specialized contracts (notably
for Numpy arrays).

%prep
%setup
%patch -p1

rm -rf ../python3
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

for i in testing tests docs;
do
    [ -d "%buildroot%python_sitelibdir/%oname/$i" -o \
     -d "%buildroot%python3_sitelibdir/%oname/$i" ] && \
    { echo "There should be no packaged $i"; exit 1; }
done

%check
nosetests -v --ignore-files=test_py3k_annotations.py

pushd ../python3
nosetests3 -v
popd

%files
%doc *.rst
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%python_sitelibdir/contracts/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/contracts/

%changelog
* Mon Apr 22 2019 Stanislav Levin <slev@altlinux.org> 1.8.12-alt1
- Initial build for Sisyphus.

