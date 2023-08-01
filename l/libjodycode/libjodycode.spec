Name: libjodycode
Version: 3.0.1
Release: alt1

Summary: General purpose utility functions

License: MIT
Group: System/Libraries
Url: https://github.com/jbruchon/libjodycode

# Source-url: https://github.com/jbruchon/libjodycode/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

%description
libjodycode is a software code library containing code shared among
several of the programs written by Jody Bruchon such as imagepile,
jdupes, winregfs, and zeromerge. These shared pieces of code were
copied between each program as they were updated. As the number of
programs increased and keeping these pieces of code synced became more
annoying, the decision was made to combine all of them into a single
reusable shared library.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%make_build HARDEN=1 PREFIX="%prefix" LIB_DIR="%_libdir"

%install
%makeinstall_std HARDEN=1 PREFIX="%prefix" LIB_DIR="%_libdir"

# Do not include the static library
rm -f %buildroot%_libdir/libjodycode.a

# man page is currently empty
rm -rf %buildroot%_man7dir

%files
%doc LICENSE.txt
%doc CHANGES.txt README.md
%_libdir/libjodycode.so.*

%files devel
%_includedir/libjodycode.h
%_libdir/libjodycode.so

%changelog
* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 3.0.1-alt1
- initial build for ALT Sisyphus

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 20 2023 David Cantrell <dcantrell@redhat.com> - 3.0.1-1
- Upgrade to libjodycode-3.0.1

* Thu Jun 15 2023 David Cantrell <dcantrell@redhat.com> - 2.0.1-2
- Add a comment explaining Patch0 is for building and packaging on
  Fedora
- Use %%forgeautosetup macro in %%prep
- Do not package the static library
- Move the header file to the devel subpackage
- Do not use CFLAGS_EXTRA as that just duplicates the CFLAGS again

* Tue Jun 13 2023 David Cantrell <dcantrell@redhat.com> - 2.0.1-1
- Initial package
