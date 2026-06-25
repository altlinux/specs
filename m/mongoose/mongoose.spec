%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif
%define _unpackaged_files_terminate_build 1

%define libname lib%name
%define sover 7

%def_disable static

Name: mongoose
Version: 7.22
Release: alt1

Summary: An easy-to-use self-sufficient web server
License: MIT
Group: System/Libraries
Url: https://mongoose.ws
VCS: https://github.com/cesanta/mongoose

Source: %name-%version.tar
Patch0: alt-disable-static-build.patch

BuildRequires: gcc-c++

%description
Mongoose web server executable is self-sufficient, it does not depend on
anything to start serving requests. If it is copied to any directory and
executed, it starts to serve that directory on port 8080 (so to access
files, go to http://localhost:8080). If some additional configuration
is required - for example, different listening port or IP-based access
control, then a 'mongoose.conf' file with respective options can be
created in the same directory where executable lives. This makes
Mongoose perfect for all sorts of demos, quick tests, file sharing, and
Web programming.

%package -n %libname%sover
Summary: %summary
Group: System/Libraries

%description -n %libname%sover
This package contains the shared library required by applications that
are using %name's embeddable API to provide web services.

%package -n %libname-devel
Summary: Development files for the %name
Group: Development/C
Requires: %libname%sover = %EVR

%description -n %libname-devel
This package contains the header files and development libraries
for %name. If you like to develop programs embedding %name on them,
you will need to install %name-devel and check %name's API at its
comprisable header file.

%if_enabled static
%package -n %libname-static
Summary: Development files for the %name
Group: Development/C
Requires: %libname-devel = %EVR

%description -n %libname-static
This package contains the shared library required by applications that
are using %name's embeddable API to provide web services.
%endif

%prep
%setup
%patch0 -p1
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' test/Makefile
%endif

%build
export ASAN=
%make_build -C test linux-libs \
%if_enabled static
    WITH_STATIC=ON
%endif
    #

%install
%__mkdir -p %buildroot%_libdir
cd test
ln -s %libname.so.%version %libname.so.%sover
ln -s %libname.so.%version %libname.so
install -Dpm 0644 %libname.so* %buildroot%_libdir/
%if_enabled static
install -Dpm 0644 %libname.a %buildroot%_libdir/
%endif

%__mkdir -p %buildroot%_includedir
install -Dpm 0644 %name.h %buildroot%_includedir

%add_debuginfo_skiplist %_libdir/%libname.so

%files
%doc README.md

%files -n %libname%sover
%_libdir/%libname.so.%{sover}*

%files -n %libname-devel
%_libdir/%libname.so
%_includedir/%name.h

%if_enabled static
%files -n %libname-static
%_libdir/%libname.a
%endif

%changelog
* Thu Jun 25 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 7.22-alt1
- new version

* Mon Apr 06 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 7.21-alt1
- new version

* Sat Nov 22 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 7.20-alt2
- e2k build fix

* Thu Nov 20 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 7.20-alt1
- new version

* Tue Feb 18 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 7.16-alt1
- new version

* Tue May 28 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 7.14-alt2
- don't create a libmongoose.so.debug

* Mon May 27 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 7.14-alt1
- Initial build for ALT Linux
