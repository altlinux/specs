%def_enable Werror

Name:     tty-solitaire
Version:  1.0.0
Release:  alt3

Summary:  Play solitaire in your terminal!

License:  MIT
Group:    Other
Url:      https://github.com/mpereira/tty-solitaire

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar
Patch0:   tty-solitaire-1.0.0-fix_non_critical_unused_result_warning.patch

Buildrequires: libncursesw-devel

%description
%summary.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS='%optflags -std=gnu11'

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/*
%doc README.md

%changelog
* Wed May 23 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt3
- Force building with gnu11 standart for e2k arch.

* Thu Nov 02 2017 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt2
- Remove buildroot macro from spec.

* Thu Oct 26 2017 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
