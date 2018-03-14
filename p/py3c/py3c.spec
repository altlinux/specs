Name:     py3c
Version:  1.0
Release:  alt1

Summary:  A Python 2/3 compatibility layer for C extensions
License:  MIT
Group:    Development/Python3
Url:      https://github.com/encukou/py3c

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires: python3-devel

%description
py3c helps you port C extensions to Python 3.

It provides a detailed guide, and a set of macros to make porting easy
and reduce boilerplate.

%package  devel
Summary:  Header files for py3c
Group:    Development/Python3
Requires: python3-devel

%description devel
%{name}-devel is only required for building software that uses py3c.
Because py3c is a header-only library, there is no matching run-time package.

%prep
%setup

%build
make py3c.pc includedir=%_includedir

%install
make install prefix=%buildroot%_prefix includedir=%buildroot%_includedir

%check
export CFLAGS="%optflags"
make test-python3

%files devel
%doc README.rst
%_includedir/py3c.h
%_includedir/py3c/
%_datadir/pkgconfig/py3c.pc

%changelog
* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
