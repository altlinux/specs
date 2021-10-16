Name:     py3c
Version:  1.4
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
* Sat Oct 16 2021 Andrey Cherepanov <cas@altlinux.org> 1.4-alt1
- New version.

* Thu Jan 07 2021 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Sun Nov 29 2020 Andrey Cherepanov <cas@altlinux.org> 1.3-alt1
- New version.

* Mon Jun 29 2020 Andrey Cherepanov <cas@altlinux.org> 1.2-alt1
- New version.

* Mon Oct 07 2019 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- New version.

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
