%define oname tqdm

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.15.0
Release: alt1
Summary: A fast, extensible progress bar for Python and CLI
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/tqdm

# https://github.com/tqdm/tqdm.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-nose python-module-flake8 python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-flake8 python3-module-coverage
%endif

%py_provides %oname

%description
tqdm means "progress" in Arabic (taqadum) and an abbreviation
for "I love you so much" in Spanish (te quiero demasiado).

Instantly make your loops show a smart progress meter -
just wrap any iterable with tqdm(iterable), and you're done!

%package -n python3-module-%oname
Summary: A fast, extensible progress bar for Python and CLI
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
tqdm means "progress" in Arabic (taqadum) and an abbreviation
for "I love you so much" in Spanish (te quiero demasiado).

Instantly make your loops show a smart progress meter -
just wrap any iterable with tqdm(iterable), and you're done!

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test3
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Aug 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.15.0-alt1
- Initial build for ALT.
