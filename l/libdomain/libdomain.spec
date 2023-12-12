%define _unpackaged_files_terminate_build 1

Name: libdomain
Version: 0.9.10
Release: alt1

Summary: Libdomain library provides ability to manipulate LDAP entries.
License: GPLv2+
Group: Development/C
Url: https://github.com/august-alt/libdomain

BuildRequires: cmake
BuildRequires: rpm-macros-cmake
BuildRequires: cmake-modules
BuildRequires: gcc gcc-c++

BuildRequires: libldap-devel libverto-devel libverto-libev-devel libverto-glib-devel libverto-libevent-devel glib2-devel
BuildRequires: libtalloc-devel libsasl2-devel
BuildRequires: libconfig-devel
BuildRequires: cgreen
BuildRequires: ragel

BuildRequires: doxygen

Requires: libverto-glib libverto-libev libverto-libevent
Requires: libsasl2-plugin-gssapi

Source0: %name-%version.tar

%description
Libdomain library provides ability to manipulate LDAP entries.

%package devel
Summary: Developer tools for the libdomain client library
Group: Development/C
Requires: libdomain = %version-%release

%description devel
The libdomain-devel package contains the header files and libraries needed to
develop programs that link against the libdomain client library.

%package tests
Summary: Tests package for the libdomain client library
Group: Other
Requires: libdomain = %version-%release

%description tests
Tests suite for the libdomain client library to improve test process.
You probably do not need that unless you really sure that you are.

%prep
%setup -q

%build
%cmake -DLIBDOMAIN_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmakeinstall_std

mkdir -p %buildroot%_includedir/%name
install -v -p -m 644 -D %_builddir/%name-%version/src/*.h %buildroot%_includedir/%name/

%files
%doc README.md

%_libdir/libdomain.so

%files devel
%_includedir/%name/*.h

%files tests
%_bindir/*

%changelog
* Tue Dec 12 2023 Vladimir Rubanov <august@altlinux.org> 0.9.10-alt1
- Fixes:
  + Fix remove attribute test.
  + Fix search test.
- Implemented:
  + Ensure test suite supports Windows AD 2012R2.

* Wed Dec 6 2023 Vladimir Rubanov <august@altlinux.org> 0.9.9-alt1
- Implemented:
  + Implement reconnect test.
- Fixes:
  + Fix issue with GSSAPI warning.
  + Add Russian test data.
  + Fix issue with asyn connection during ldap_bind.

* Fri Dec 1 2023 Vladimir Rubanov <august@altlinux.org> 0.9.7-alt1
- Implemented:
  + Implement initial timeout test.
  + Implement configuration loading and tests.
- Fixes:
  + Fix issue with directory test.
  + Improve description in configure test.

* Tue Nov 28 2023 Vladimir Rubanov <august@altlinux.org> 0.9.5-alt1
- Fixes:
  + Implement initial samba support.
  + Implement test suite for samba.

* Mon Nov 20 2023 Vladimir Rubanov <august@altlinux.org> 0.9.1-alt1
- Fixes:
  + Fix user blocking and unblocing in OpenLDAP 2.6.
  + Fix entry addition, deletion, renaming and modification.

* Mon Nov 13 2023 Vladimir Rubanov <august@altlinux.org> 0.9.0-alt1
- Implemented:
  + Implement tests for TLS.
  + Implement tests for computer addition to and removal, modification and rename in OpenLDAP.
  + Implement tests for blocking and unblocking users in OpenLDAP.
  + Implement tests for reconnection testing.
  + Implement tests for anonymous connection.
- Fixes:
  + Fix description in spec file. (Closes: 46202).

* Mon Oct 09 2023 Vladimir Rubanov <august@altlinux.org> 0.8.0-alt1
- Implemented:
  + Implement directory service type detection.
  + Implement new message type handling.

* Thu Aug 24 2023 Vladimir Rubanov <august@altlinux.org> 0.7.1-alt1
- Fixes:
  + Fixes unbind in error state.

* Thu Jun 14 2023 Vladimir Rubanov <august@altlinux.org> 0.7.0-alt1
- Implemented:
  + Implement test stubs for TLS, timeout testing.
  + Implement tests for user addition to and removal from group.
  + Implement test stubs for blocking and unblocking users.
  + Implement tests for reconnection testing.
  + Implement test stub for anonmous connection.

* Thu Jun 08 2023 Vladimir Rubanov <august@altlinux.org> 0.6.0-alt1
- Implemented:
  + Add more tests for users, groups and OUs.

* Fri Jun 02 2023 Vladimir Rubanov <august@altlinux.org> 0.5.0-alt1
- Implemented:
  + Add tests for users, groups and OUs.
  + Add new library API.

* Tue May 30 2023 Vladimir Rubanov <august@altlinux.org> 0.4.0-alt1
- Implemented:
  + Add test for entry renaming, deletion and modification

* Mon May 22 2023 Vladimir Rubanov <august@altlinux.org> 0.3.0-alt1
- Implemented:
  + Add development files

* Mon May 22 2023 Vladimir Rubanov <august@altlinux.org> 0.2.0-alt1
- Implemented:
  + Methods for deleting adding and modifying ldap entries
  + Methods for connection configuration
  + Automated documentation generation
  + Automated tests with OpenLDAP
  + CI pipeline

* Mon Jan 23 2023 Vladimir Rubanov <august@altlinux.org> 0.1.0-alt1
- Initial build
