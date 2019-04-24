%define  oname eradicate

Name:    python3-module-%oname
Version: 1.0
Release: alt1

Summary: Removes commented-out code from Python files

License: MIT
Group:   Development/Python3
URL:     https://github.com/myint/eradicate

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %oname-%version.tar

%description
With modern revision control available, there is no reason to save
commented-out code to your repository. "eradicate" helps cleans up
existing junk comments. It does this by detecting block comments that
contain valid Python syntax that are likely to be commented out code.
(It avoids false positives like the sentence "this is not good",
which is valid Python syntax, but is probably not code.)

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%if "3"=="3"
mv %buildroot%_bindir/eradicate %buildroot%_bindir/eradicate3
%endif

%files
%doc README.rst
%_bindir/eradicate3
%python3_sitelibdir/*

%changelog
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
