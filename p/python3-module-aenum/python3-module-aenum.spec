%define modulename aenum

Name: python3-module-%modulename
Summary: Python advanced enumerations, namedtuples, and constants
Version: 2.2.6
Release: alt1
Group: Development/Python3
License: BSD
URL: https://github.com/ethanfurman/aenum
Source: https://pypi.io/packages/source/a/%modulename/%modulename-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%description
Advanced Enumerations (compatible with Python's stdlib Enum), NamedTuples,
and NamedConstants.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

# Delete docs from python module
rm -r %buildroot%python3_sitelibdir/aenum/doc
rm %buildroot%python3_sitelibdir/aenum/{LICENSE,CHANGES,README}

# Delete tests
rm %buildroot%python3_sitelibdir/aenum/test*

%files
%doc README
%python3_sitelibdir/*

%changelog
* Fri Dec 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.6-alt1
- Initial build for ALT

