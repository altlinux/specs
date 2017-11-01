%def_enable Werror

Name:     tty-solitaire
Version:  1.0.0
Release:  alt1

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
%patch -p1

%build
%make_build CFLAGS='%optflags'

%install
%makeinstall PREFIX=%buildroot%_prefix

%files
%_bindir/*
%doc README.md

%changelog
* Thu Oct 26 2017 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
