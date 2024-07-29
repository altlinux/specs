Name: pam_wrapper
Version: 1.1.7
Release: alt1
Summary: A tool to test PAM applications and PAM modules
License: GPLv3+
Url: http://cwrap.org/
# git://git.samba.org/pam_wrapper.git
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Group: Development/C
BuildRequires: cmake
BuildRequires: libcmocka-devel
BuildRequires: python3-devel
BuildRequires: pam-devel
BuildRequires: doxygen
BuildRequires: git
BuildRequires: ctest
BuildRequires: python3-module-setuptools

%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module.

For testing PAM applications, simple PAM module called pam_matrix is
included. If you plan to test a PAM module you can use the pamtest library,
which simplifies testing of modules. You can combine it with the cmocka
unit testing framework or you can use the provided Python bindings to
write tests for your module in Python.

%package -n libpamtest
Summary: A tool to test PAM applications and PAM modules
License: GPLv3+
Group:Development/C
Requires: pam_wrapper = %version-%release

%description -n libpamtest
If you plan to test a PAM module you can use this library, which simplifies
testing of modules.

%package -n libpamtest-devel
Summary: A tool to test PAM applications and PAM modules
License: GPLv3+
Group: Development/C
Requires: pam_wrapper = %version-%release
Requires: libpamtest = %version-%release


%description -n libpamtest-devel
If you plan to develop tests for a PAM module you can use this library,
which simplifies testing of modules. This sub package includes the header
files for libpamtest.

%package -n libpamtest-doc
Summary: The libpamtest API documentation
Group: Development/C
License: GPLv3+

%description -n libpamtest-doc
Documentation for libpamtest development.

%package -n python3-module-libpamtest
Summary: A python wrapper for libpamtest
License: GPLv3+
Group: Development/C
Requires: pam_wrapper = %version-%release
Requires: libpamtest = %version-%release

%description -n python3-module-libpamtest
If you plan to develop python tests for a PAM module you can use this
library, which simplifies testing of modules. This subpackage includes
the header files for libpamtest

%prep
%setup
%patch0 -p1

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DAPPLICATION_VERSION=%version \
  -DUNIT_TESTING=ON

%cmake_build
%cmake_build --target doc

%install
%cmake_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%cmake_build --target test

%files
%_libdir/libpam_wrapper.so*
%_libdir/pkgconfig/pam_wrapper.pc
%dir %_libdir/cmake/pam_wrapper
%_libdir/cmake/pam_wrapper/pam_wrapper-config-version.cmake
%_libdir/cmake/pam_wrapper/pam_wrapper-config.cmake
%_libdir/pam_wrapper/pam_chatty.so
%_libdir/pam_wrapper/pam_matrix.so
%_libdir/pam_wrapper/pam_get_items.so
%_libdir/pam_wrapper/pam_set_items.so
%_mandir/man1/pam_wrapper.1*
%_mandir/man8/pam_chatty.8*
%_mandir/man8/pam_matrix.8*
%_mandir/man8/pam_get_items.8*
%_mandir/man8/pam_set_items.8*

%files -n libpamtest
%_libdir/libpamtest.so.*

%files -n libpamtest-devel
%_libdir/libpamtest.so
%_libdir/pkgconfig/libpamtest.pc
%dir %_libdir/cmake/pamtest
%_libdir/cmake/pamtest/pamtest-config-relwithdebinfo.cmake
%_libdir/cmake/pamtest/pamtest-config-version.cmake
%_libdir/cmake/pamtest/pamtest-config.cmake
%_includedir/libpamtest.h

%files -n libpamtest-doc
%doc %_cmake__builddir/doc/html

%files -n python3-module-libpamtest
%python3_sitelibdir/pypamtest.so

%changelog
* Mon Jul 29 2024 Evgeny Sinelnikov <sin@altlinux.org> 1.1.7-alt1
- new version 1.1.7
- Fixes from upstream:
  + Fix installation of python module
  + Improve config dir creation if we have pam_start_confdir()
  + Fixed PAM_WRAPPER_DISABLE_DEEPBIND
  + Directly fail if we can't create the config dir

* Tue Dec 19 2023 Grigory Ustinov <grenka@altlinux.org> 1.1.5-alt1.1
- NMU: Add build dependency on setuptools.

* Tue Dec 12 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.1.5-alt1
- Fixed building with Python 3.12

* Mon May 29 2023 Evgeny Sinelnikov <sin@altlinux.org> 1.1.4-alt2
- Fix cmocka >= 1.1.6 find_package() in CONFIG mode.
- Drop support for Python 2.

* Mon Nov 01 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.1.4-alt1
- new version 1.1.4

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 1.1.3-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Aug 13 2020 Anton Farygin <rider@altlinux.ru> 1.1.3-alt1
- first build for ALT (based on specfile from Fedora)

