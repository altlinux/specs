Name: libtevent
Version: 0.9.15
Release: alt2.1
Summary: The tevent library
License: LGPLv3+
Group: System/Libraries
Url: http://tevent.samba.org/

Source: %name-%version.tar
Source10: buildtools.tar
Source11: replace.tar
Source12: talloc.tar

BuildRequires: libtalloc-devel >= 2.0.5
BuildRequires: libpytalloc-devel >= 2.0.5
BuildRequires: python-devel zlib-devel

%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (Tevent Request) functions.

%package devel
Group: Development/C
Summary: Developer tools for the Tevent library
Requires: %name = %version-%release

%description devel
Header files needed to develop programs that link against the tevent library.

%package -n python-module-tevent
Group: Development/Python
Summary: Python bindings for the Tevent library
Requires: %name = %version-%release

%description -n python-module-tevent
Python bindings for libtevent

%prep
%setup -q -a 10 -a 11 -a 12
mkdir lib
mv -f replace lib/
mv -f talloc lib/

%build
%undefine _configure_gettext
%configure \
	--disable-rpath \
	--bundled-libraries=NONE \
	--builtin-libraries=replace

%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a

%files
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n python-module-tevent
%python_sitelibdir/_tevent.so
%python_sitelibdir_noarch/tevent.py*

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.15-alt2.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Apr 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.15-alt2
- add --builtin-libraries=replace to configure

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.15-alt1
- 0.9.15

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.13-alt1.1
- Rebuild with Python-2.7

* Tue Jul 12 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Thu Apr 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.11-alt1
- 0.9.11
- add python-module-tevent package

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt1.1
- Rebuilt for soname set-versions

* Fri Aug 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- initial build for ALT Linux Sisyphus
