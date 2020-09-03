%define oname pylama

# For a while until update
%def_without check

Name: python3-module-%oname
Version: 7.7.1
Release: alt1
Summary: pylama -- Code audit tool for python
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/pylama/

# https://github.com/klen/pylama.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: git
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-ipdb python3-tools-pep8 python3-pyflakes
BuildPreReq: pylint-py3 python3-module-nose
BuildPreReq: python3(pytest)

%py3_provides %oname

%description
pylama -- Code audit tool for python.

%prep
%setup

%build
export LC_ALL=en_US.UTF-8
%python3_build_debug

%install
export LC_ALL=en_US.UTF-8
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
python3 setup.py test
nosetests3

%files
%doc AUTHORS Changelog *.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Fri Sep 04 2020 Grigory Ustinov <grenka@altlinux.org> 7.7.1-alt1
- Automatically updated to 7.7.1.

* Sat Aug 01 2020 Grigory Ustinov <grenka@altlinux.org> 6.1.1-alt4.git20141029
- Drop python2 support.

* Tue Oct 01 2019 Stanislav Levin <slev@altlinux.org> 6.1.1-alt3.git20141029.3
- Fixed build.

* Thu Apr 25 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 6.1.1-alt3.git20141029.2
- build fixed

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.1.1-alt3.git20141029.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 6.1.1-alt3.git20141029
- Recompile for python3.5 changed place of site-packages.

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 6.1.1-alt2.git20141029
- Build back into sisyphus

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.1.1-alt1.git20141029
- Initial build for Sisyphus

