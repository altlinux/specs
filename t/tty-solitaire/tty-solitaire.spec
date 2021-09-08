%def_enable Werror

Name:     tty-solitaire
Version:  1.3.1
Release:  alt1

Summary:  Play solitaire in your terminal!

License:  MIT
Group:    Games/Cards
Url:      https://github.com/mpereira/tty-solitaire

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch: make-gcc10-happy.patch

Buildrequires: libncursesw-devel

%description
%summary.

%prep
%setup
%patch -p1

%build
%make_build CFLAGS='%optflags -std=gnu11'

%install
%makeinstall_std PREFIX=%_prefix

%check
make test

%files
%_bindir/*
%doc LICENSE README CHANGELOG TODO.md

%changelog
* Wed Sep 08 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Automatically updated to 1.3.1.

* Mon Dec 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt2
- Fixed build with gcc10.

* Tue Jun 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.
- Add check.

* Mon Nov 12 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.1-alt1
- Build new version.

* Mon Aug 13 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Wed May 23 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt3
- Force building with gnu11 standart for e2k arch.

* Thu Nov 02 2017 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt2
- Remove buildroot macro from spec.

* Thu Oct 26 2017 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
