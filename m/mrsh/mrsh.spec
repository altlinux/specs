%define _unpackaged_files_terminate_build 1

%define _soversion 0
# (mrsh_build_system == make) is untested; patches welcome.
%define mrsh_build_system meson

%define register_shell() for i in %*; do grep -Fqx "$i" /etc/shells || echo "$i" >> /etc/shells; done
%define unregister_shell() for i in %*; do sed -i 'y/\\//)/; /^'$(echo "$i" | tr / ')')'$/d; y/)/\\//' /etc/shells; done

Name: mrsh
Version: 0.0.1.g280fdf5ec59d
Release: alt1

Summary: A minimal POSIX shell

License: MIT
Group: Shells
Url: https://mrsh.sh

%define libname lib%name%_soversion

VCS: https://git.sr.ht/~emersion/mrsh
Source: %name-%version-%release.tar

%if %mrsh_build_system == meson
BuildRequires: meson
%endif
%if %mrsh_build_system == make
BuildRequires: make
%endif
BuildRequires: libreadline-devel

%description
A minimal, POSIX compliant shell with simple, readable code.

%package -n %libname
Summary: %name as a shared library
Group: System/Libraries

%description -n %libname
A minimal, POSIX compliant shell with simple, readable code, available as a
shared library.

%package -n %libname-devel
Summary: Header files for developing POSIX shells or more elaborate ones
Group: Development/C
Requires: %libname = %version-%release
#Requires: glibc-devel

%description -n %libname-devel
This package contains the development files needed to develop programs
that use %name's shared library.

%prep
%setup

%build
%if %mrsh_build_system == meson
%meson -Dreadline=enabled
%meson_build
%endif
%if %mrsh_build_system == make
%configure
%make_build
%endif

%install
%if %mrsh_build_system == meson
%meson_install
%endif
%if %mrsh_build_system == make
%makeinstall_std
%endif

%post
# Unfortunately, we don't have a filetrigger-based mechanism.
if [ $1 -eq 1 ]; then
%register_shell %_bindir/%name
fi

%preun
if [ $1 -eq 0 ]; then
%unregister_shell %_bindir/%name
fi

%files
%_bindir/*
#_man1dir/*
%doc README.md LICENSE

%files -n %libname
%_libdir/lib%name.so.%{_soversion}*

%files -n %libname-devel
%_libdir/lib%name.so
%_includedir/mrsh/
%_pkgconfigdir/%name.pc

%changelog
* Mon Jul 28 2020 Arseny Maslennikov <arseny@altlinux.org> 0.0.1.g280fdf5ec59d-alt1
- Initial build for ALT Sisyphus.
