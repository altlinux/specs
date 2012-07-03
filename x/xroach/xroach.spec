Summary: Displays disgusting cockroaches on your root X window
Name: xroach
Version: 4.0
Release: alt1.2
License: distributable
Group: Toys
Source: xroach-4.0.tar.gz
Patch: xroach.patch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>
Prefix: /usr

# Automatically added by buildreq on Fri Apr 04 2008 (-bi)
BuildRequires: libX11-devel

%description
This program displays disgusting cockroaches on your root X window.
They scurry about when windows are minimized or moved.

%prep
%setup
%patch -p 1

%build
CFLAGS=$RPM_OPT_FLAGS
make clean
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_man1dir}
install -s -m 755  xroach $RPM_BUILD_ROOT%{_bindir}
install -m 644 xroach.1 $RPM_BUILD_ROOT%{_man1dir}/xroach.1x

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{name}
%{_man1dir}/%{name}.1*

%changelog
* Fri Apr 04 2008 Igor Yu. Vlasenko <viy@altlinux.org> 4.0-alt1.2
- refreshed buildreq

* Wed Mar 15 2006 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1.1
- build for alt linux

* Tue Jun 22 1999 Dan Anderson <danx@cts.com>
- Added clean, BuildRoot, Prefix, and README.
- Removed compiler warnings in XGetWindowProperty() call.

* Tue Jan 22 1999  Dan Anderson <danx@cts.com>
- Rebuilt for glibc2.

