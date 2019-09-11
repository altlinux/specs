Name:    sunfish
Version: 0.2
Release: alt1

Summary: A Python Chess Engine in 111 lines of code

License: GPLv3
Group:   Games/Boards
Url:     https://github.com/thomasahle/sunfish

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev

BuildArch: noarch

Source:  %name-%version.tar
Patch: %name-%version-alt-no-pypy.patch

%description
Sunfish is a simple, but strong chess engine, written in Python, mostly for
teaching purposes. Without tables and its simple interface, it takes up
just 111 lines of code!
Because Sunfish is small and strives to be simple, the code provides a great
platform for experimenting. People have used it for testing parallel search
algorithms, experimenting with evaluation functions, and developing
deep learning chess programs. Fork it today and see what you can do!

%prep
%setup
%patch -p1

%install
install -Dm755 %name.py %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Wed Sep 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.2-alt1
- Build new version.
- Transfer for python3.

* Thu Nov 02 2017 Grigory Ustinov <grenka@altlinux.org> 0.1-alt2
- Change summary and upstream.

* Wed Sep 20 2017 Grigory Ustinov <grenka@altlinux.org> 0.1-alt1
- Initial build for Sisyphus.
