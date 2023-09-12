%define soname 0

%def_enable tests

Name: luksmeta
Version: 9
Release: alt1

Summary: Tools for storing metadata in a LUKSv1 header

License: LGPL-2.1-or-later
Group: Development/Tools
Url: https://github.com/latchset/luksmeta

Source: %url/archive/v%version/%name-%version.tar.gz
Patch0: luksmeta-9-upstream-relax-content-tests-in-test-suite.patch
Patch1: luksmeta-9-upstream-force-creation-of-luks1-containers.patch

# BEGIN SourceDeps(oneline):
BuildRequires: asciidoc-a2x libcryptsetup-devel
# END SourceDeps(oneline)
%if_enabled tests
BuildRequires: cryptsetup
%endif

%description
%summary.

%package -n lib%name%soname
Summary: Library for storing metadata in a LUKSv1 header
Group: System/Libraries

%description -n lib%name%soname
This package provides library for %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C

%description -n lib%name-devel
This package provides development files for %name.

%prep
%setup
%autopatch -p1
sed -i 's|cryptsetup|/sbin/cryptsetup|' \
  ./test-luksmeta

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%if_enabled tests
%check
make check
%endif

%files
%doc COPYING README.md
%_bindir/%name
%_man8dir/%{name}*

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Sep 12 2023 Leontiy Volodin <lvol@altlinux.org> 9-alt1
- Initial build for ALT Sisyphus.
- Needed for clevis 19.
