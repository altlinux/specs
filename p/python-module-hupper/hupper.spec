%define oname hupper

%def_with python3

Name:           python-module-%oname
Version:        1.0
Release:        alt1
Summary:        Integrated process monitor for developing servers
Group:          Development/Python
License:        MIT
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/%{oname}

# https://github.com/Pylons/hupper.git
Source: %name-%version.tar

BuildRequires: python-dev python2.7(pytest) python2.7(pytest_cov) python2.7(watchdog) python2.7(mock)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3(pytest) python3(pytest_cov) python3(watchdog) python3(mock)
%endif

%description
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%package -n python3-module-%oname
Summary:        Integrated process monitor for developing servers
Group:          Development/Python

%description -n python3-module-%oname
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

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
for i in %buildroot%_bindir/* ; do
	mv $i ${i}.py3
done
%endif

%python_install

%check
PYTHONPATH=%buildroot%python_sitelibdir py.test

%if_with python3
pushd ../python3
PYTHONPATH=%buildroot%python3_sitelibdir py.test3
popd
%endif

%files
%doc CHANGES.rst CONTRIBUTING.rst LICENSE.txt README.rst rtd.txt
%python_sitelibdir/*
%_bindir/*
%exclude %_bindir/*.py3

%files -n python3-module-%oname
%doc CHANGES.rst CONTRIBUTING.rst LICENSE.txt README.rst rtd.txt
%python3_sitelibdir/*
%_bindir/*.py3

%changelog
* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.2-1
- Initial version for Fedora. 

