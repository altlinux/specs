%global pypi_name jsonpatch
%global github_name python-json-patch

Name:           python-module-%pypi_name
Version:        1.23
Release:        alt1

Summary:        Applying JSON Patches in Python
Group:          Development/Python
License:        BSD
URL:            https://github.com/stefankoegl/%{github_name}
BuildArch:      noarch

Source0:        %name-%version.tar

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-modules-json
BuildRequires:  python-module-jsonpointer >= 1.9

BuildRequires(pre):  rpm-build-python3
BuildPreReq:  python3-module-setuptools
BuildPreReq:  python3-module-jsonpointer >= 1.9


%description
Library to apply JSON Patches according to RFC 6902.

%package -n python3-module-%pypi_name
Summary:        Applying JSON Patches in Python
Group:		Development/Python

%description -n python3-module-%pypi_name
Library to apply JSON Patches according to RFC 6902.

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
python tests.py

pushd ../python3
python3 tests.py
popd

%files
%doc README.md COPYING
%_bindir/*.py2
%python_sitelibdir/*

%files -n python3-module-%{pypi_name}
%doc README.md COPYING
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*

%changelog
* Tue Jan 15 2019 Alexey Shabalin <shaba@altlinux.org> 1.23-alt1
- 1.23

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9-alt1.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9-alt1
- Version 1.9

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2-alt1
- First build for ALT (based on Fedora 1.2-3.fc21.src)
