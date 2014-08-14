%global pkgname jsonpath-rw
%def_with python3

Name:		python-module-%{pkgname}
Version:	1.2.3
Release:	alt1
Summary:        Extended implementation of JSONPath for Python
Group:		Development/Python

License:	ASL 2.0
URL:		https://github.com/kennknowles/python-jsonpath-rw
Source0:	%{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:	python-devel, python-module-setuptools
Requires:       python-module-ply
Requires:       python-module-decorator
Requires:       python-module-six

%description

This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming. It is tested with
Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%if_with python3
%package -n python3-module-%{pkgname}
Summary: Extended implementation of JSONPath for Python
Group: Development/Python
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
Requires:       python3-module-ply
Requires:       python3-module-decorator
Requires:       python3-module-six

%description -n python3-module-%{pkgname}

This library provides a robust and significantly extended implementation of
JSONPath for Python, with a clear AST for meta-programming. It is tested with
Python 2.6, 2.7, 3.2, 3.3, and PyPy.

This library differs from other JSONPath implementations in that it is a full
language implementation, meaning the JSONPath expressions are first class
objects, easy to analyze, transform, parse, print, and extend.

%endif

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation
BuildArch:      noarch

%description    doc
Documentation for %{name}.

%prep
%setup

%if_with python3
rm -rf ../python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst LICENSE
%{python_sitelibdir}/*

%if_with python3
%files -n python3-module-%{pkgname}
%doc README.rst LICENSE
%{python3_sitelibdir}/*
%endif

%changelog
* Mon Aug 11 2014 Lenar Shakirov <snejok@altlinux.ru> 1.2.3-alt1
- First build for ALT (based on Fedora 1.2.3-4.fc21.src)

