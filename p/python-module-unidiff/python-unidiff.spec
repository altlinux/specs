Name:		python-module-unidiff
Version:	0.1
Release:	alt1.1
License:	MIT
Source:		v%{version}.tar.gz
Group:		Development/Python
Summary:	Parse and interact with unified diff data
BuildArch:	noarch
URL:		https://github.com/matiasb/python-unidiff
BuildPreReq:	rpm-build-python3
%setup_python_module unidiff

# Automatically added by buildreq on Mon Sep 22 2014
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools

%description
Simple Python library to parse and interact with unified diff data.

%package -n python3-module-unidiff
Group:		Development/Python3
Summary:        Parse and interact with unified diff data
%description -n python3-module-unidiff
Simple Python library to parse and interact with unified diff data.

%prep
%setup -n python-unidiff-%version

%build
%python_build
%python3_build -b build3

%install
%python_install
mv build build2
mv build3 build
%python3_install
mv build build3
mv build2 build

%files
%python_sitelibdir_noarch/*

%files -n python3-module-unidiff
%python3_sitelibdir_noarch/*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 22 2014 Fr. Br. George <george@altlinux.ru> 0.1-alt1
- Initial build

