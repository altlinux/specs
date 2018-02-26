Name: refdbg
Version: 1.2
Release: alt5
License: %gpl2plus
Group: Development/Debuggers
Summary: RefDbg is a GObject reference count debugger.
Url: http://refdbg.sourceforge.net/index.html
Source: %name-%version.tar

BuildRequires(pre):rpm-build-licenses
BuildRequires: glib2-devel binutils-devel

%description
RefDbg is a GObject reference count debugger. GObject is part of the
glib library. The GObject library adds object oriented stuff to C which
by itself lacks object oriented features. Since C lacks garbage
collection, a reference counting system is used. Each object has a count
of how many other references (pointers) there are to it. Reference count
bugs can be very hard to track down and can lead to crashes and memory
leaks. Refdbg is a tool that can be used interactively with GDB to log,
display and break on reference count activity, thereby making this task
easier.

%prep
%setup -n %name-%version

%build
sed -i "s;lib/librefdbg.so;%_lib/librefdbg.so;" refdbg.in
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS README
%_includedir/*
%_bindir/*
%_libdir/*.so*

%changelog
* Mon Feb 07 2011 Mikhail Efremov <sem@altlinux.org> 1.2-alt5
- Don't build static library.
- Don't use sweeping glob pattern in %%_libdir.
- Slightly spec cleanup.

* Tue Dec 14 2010 Kirill A. Shutemov <kas@altlinux.org> 1.2-alt4
- rebuild with binutils-devel

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 1.2-alt3
- rebuild with libbfd 2.20.51.0.11

* Mon Jun 21 2010 Mikhail Efremov <sem@altlinux.org> 1.2-alt2
- rebuild with libbfd 2.20.51.0.9

* Fri Apr 23 2010 Mikhail Efremov <sem@altlinux.org> 1.2-alt1
- initial build for Sisyphus


