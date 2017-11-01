%define oname isort

%def_with python3

Name:           python-module-%oname
Version:        4.2.15
Release:        alt1%ubt
Summary:        Python utility / library to sort Python imports
Group:          Development/Python
License:        MIT
URL:            https://github.com/timothycrosley/isort
BuildArch:      noarch

# https://github.com/timothycrosley/isort.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-pytest python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-pytest python3-module-mock
%endif

%description
Python utility / library to sort Python imports

%if_with python3
%package -n python3-module-%oname
Group:          Development/Python3
Summary:        Python utility / library to sort Python imports

%description -n python3-module-%oname
Python utility / library to sort Python imports
%endif

%prep
%setup

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

python setup.py test

%files
%doc README.rst LICENSE
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py2*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst LICENSE
%_bindir/*.py3
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py3*.egg-info
%endif

%changelog
* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.15-alt1%ubt
- Initial build for ALT.
