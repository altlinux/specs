%define  oname mypy

Name:    python3-module-%oname
Version: 0.701
Release: alt1

Summary: Optional static typing for Python 3 and 2 (PEP 484)
License: MIT
Group:   Development/Python3
URL:     https://github.com/python/mypy

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

# Needed to generate the man pages
BuildRequires:  help2man

BuildArch: noarch

Source:  %oname-%version.tar

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

# Generate man pages
mkdir -p %buildroot%_man1dir

PYTHONPATH=%buildroot%python3_sitelibdir \
    help2man --no-info --version-string 'mypy %version-dev' \
        --no-discard-stderr -o %buildroot%_man1dir/mypy.1 \
        %buildroot%_bindir/mypy

PYTHONPATH=%buildroot%python3_sitelibdir \
    help2man --no-info --version-string 'mypy stubgen %version-dev' \
        --no-discard-stderr -o %buildroot%_man1dir/stubgen.1 \
        %buildroot%_bindir/stubgen

%files
%doc README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info
%_bindir/%oname
%_bindir/dmypy
%_bindir/stubgen
%_man1dir/mypy.1*
%_man1dir/stubgen.1*

%changelog
* Wed Apr 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.701-alt1
- Initial build for Sisyphus
