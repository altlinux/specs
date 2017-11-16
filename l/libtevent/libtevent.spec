%def_enable tests

Name: libtevent
Version: 0.9.34
Release: alt1%ubt
Summary: The tevent library
License: LGPLv3+
Group: System/Libraries
Url: http://tevent.samba.org/

Source: http://samba.org/ftp/tevent/tevent-%{version}.tar.gz

BuildRequires: libtalloc-devel >= 2.0.10
BuildRequires: libpytalloc-devel >= 2.0.10
BuildRequires: python-devel zlib-devel

BuildRequires(pre):rpm-build-ubt

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
%setup -n tevent-%version

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

%if_enabled tests
%check
export LD_LIBRARY_PATH=./bin/shared:$LD_LIBRARY_PATH
make test
%endif

%files
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n python-module-tevent
%python_sitelibdir/_tevent.so
%python_sitelibdir/tevent.py*

%changelog
* Thu Nov 16 2017 Evgeny Sinelnikov <sin@altlinux.org> 0.9.34-alt1%ubt
- New version for samba-4.6.10 and samba-4.7.2

* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.33-alt1%ubt
- New version for samba-4.7.0

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.31-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.31-alt1%ubt
- New version for samba-4.6.0

* Thu Sep 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 0.9.29-alt1
- New version for samba-4.5.0

* Thu Mar 03 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.28-alt1
- New version

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 0.9.26-alt1
- 0.9.26
- Enable tests

* Wed Jul 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.25-alt1
- 0.9.25

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.24-alt1
- 0.9.24

* Fri Nov 07 2014 Alexey Shabalin <shaba@altlinux.ru> 0.9.22-alt1
- 0.9.22

* Thu Jan 23 2014 Alexey Shabalin <shaba@altlinux.ru> 0.9.21-alt1
- 0.9.21

* Mon Dec 16 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.20-alt1
- 0.9.20

* Wed Aug 07 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.19-alt1
- 0.9.19

* Tue Apr 09 2013 Alexey Shabalin <shaba@altlinux.ru> 0.9.18-alt1
- 0.9.18

* Mon Sep 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.17-alt1
- 0.9.17

* Fri Jul 27 2012 Alexey Shabalin <shaba@altlinux.ru> 0.9.16-alt1
- 0.9.16

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
