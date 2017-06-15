Name: 	  clac
Version:  0.3.0
Release:  alt1

Summary:  A command line, stack-based calculator with postfix notation
License:  BSD-2-Clause
Group:    Other
Url: 	  https://github.com/soveran/clac

Packager: Gordeev Mikhail <obirvalger@altlinux.org>

Source:   %name-%version.tar

%description
A command line, stack-based calculator with postfix notation that displays the
stack contents at all times. As you type, the stack changes are reflected
immediately.

%prep
%setup

%build
%make_build

%install
make install PREFIX=%buildroot%_prefix

%check
make test

%files
%_bindir/*
%_man1dir/*
%doc README*

%changelog
* Thu Jun 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
