%global pypi_name jsonpointer
%global github_name python-json-pointer

Name:           python-module-%pypi_name
Version:        2.0
Release:        alt1
Summary:        Resolve JSON Pointers in Python
Group:          Development/Python

License:        BSD
URL:            https://github.com/stefankoegl/%github_name
Source0:        %name-%version.tar

BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools

BuildRequires(pre):  rpm-build-python3
BuildPreReq:  python3-module-setuptools

%description
Library to resolve JSON Pointers according to RFC 6901.

%package -n python3-module-%pypi_name
Summary:        Resolve JSON Pointers in Python
Group:          Development/Python3

%description -n python3-module-%pypi_name
Library to resolve JSON Pointers according to RFC 6901.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
export LC_ALL=en_US.UTF-8
%python3_build
popd

%install
%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py2
done
popd

pushd ../python3
export LC_ALL=en_US.UTF-8
%python3_install
popd

%check
pushd ../python3
python3 tests.py
popd

python tests.py

%files
%doc README.md
%_bindir/*.py2
%python_sitelibdir/*


%files -n python3-module-%pypi_name
%doc README.md
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*

%changelog
* Tue Jan 15 2019 Alexey Shabalin <shaba@altlinux.org> 2.0-alt1
- 2.0

* Fri Apr 08 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1.1
- (NMU) Rebuild with python3-3.5.1-alt3 to get rid of the meaningless __pycache__/ dep
  (it is meaningless because arbitrary packages package that dir).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1
- Version 1.6

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0-alt1
- First build for ALT (based on Fedora 1.0-5.fc21.src)

