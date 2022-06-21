%define _unpackaged_files_terminate_build 1

Name:       aushape
Version:    2
Release:    alt1.wip
Summary:    Audit message format conversion library and utility
Group:      Monitoring

License:    GPLv2+ and LGPLv2+
URL:        https://scribery.github.io/aushape/

Source:     %name-%version.tar

BuildRequires: libaudit-devel

%description
Aushape is a library and a tool for converting audit messages to other
formats.

%prep
%setup

%build
%autoreconf
%configure --disable-rpath --disable-static
%make_build

%install
%make DESTDIR=%buildroot docdir=%_docdir/%name-%version install

%check
make check

%files
%doc README.md notes.txt
%_bindir/%name
%_libdir/lib%name.so.*
%exclude %_libdir/lib%name.so
#%exclude %_libdir/*.la
%exclude %_includedir

%changelog
* Mon Jun 20 2022 Paul Wolneykien <manowar@altlinux.org> 2-alt1.wip
- Initial build for Sisyphus.
