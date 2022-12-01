Name:     kiwix-lib
Version:  12.0.0
Release:  alt1

Summary:  Common code base for all Kiwix ports
License:  GPL-3.0
Group:    Other
Url:      https://github.com/kiwix/kiwix-lib

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: libicu-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libpugixml-devel
BuildRequires: libzim-devel
BuildRequires: mustache-cpp-devel
BuildRequires: zlib-devel

%description
%summary

%package -n libkiwix
Summary: Common code base for all Kiwix ports
Group: System/Libraries

%description -n libkiwix
%summary

%package -n libkiwix-devel
Summary: Development files for common code base for all Kiwix ports
Group: Development/C++

%description -n libkiwix-devel
%summary

%prep
%setup
%ifarch %e2k
sed -i "s/compiler.get_id()/'gcc'/" meson.build
%endif

%build
# Ignore warning about old Xapian version
%add_optflags -Wno-error=cpp
%meson
%meson_build

%install
%meson_install

%files -n libkiwix
%doc AUTHORS README.md
%_libdir/*.so.*

%files -n libkiwix-devel
%_bindir/kiwix-compile-resources
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/kiwix.pc
%_man1dir/*.1*

%changelog
* Thu Dec 01 2022 Andrey Cherepanov <cas@altlinux.org> 12.0.0-alt1
- New version.

* Fri Jun 24 2022 Andrey Cherepanov <cas@altlinux.org> 11.0.0-alt1
- New version.

* Thu Jun 02 2022 Andrey Cherepanov <cas@altlinux.org> 10.1.1-alt2
- FTBFS: ignore warning about old Xapian version.

* Sat May 21 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 10.1.1-alt1.1
- Fixed build for Elbrus.

* Tue Apr 12 2022 Andrey Cherepanov <cas@altlinux.org> 10.1.1-alt1
- New version.

* Fri Mar 25 2022 Andrey Cherepanov <cas@altlinux.org> 10.1.0-alt1
- New version.

* Thu Feb 03 2022 Andrey Cherepanov <cas@altlinux.org> 10.0.1-alt1
- New version.

* Sat Jan 22 2022 Andrey Cherepanov <cas@altlinux.org> 10.0.0-alt1
- New version.

* Tue May 04 2021 Andrey Cherepanov <cas@altlinux.org> 9.4.1-alt2
- Add rpm-build-python3 to detect python3 requirements.

* Wed Nov 18 2020 Andrey Cherepanov <cas@altlinux.org> 9.4.1-alt1
- New version.

* Sun Aug 30 2020 Andrey Cherepanov <cas@altlinux.org> 9.4.0-alt1
- New version.

* Sat Jul 18 2020 Andrey Cherepanov <cas@altlinux.org> 9.3.1-alt1
- New version.

* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 9.3.0-alt1
- New version.

* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 9.2.3-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 9.2.2-alt1
- New version.

* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 9.2.1-alt1
- New version.

* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 9.2-alt1
- New version.

* Thu May 14 2020 Andrey Cherepanov <cas@altlinux.org> 9.1.2-alt1
- New version.

* Tue Apr 28 2020 Andrey Cherepanov <cas@altlinux.org> 9.1.1-alt1
- Initial build for Sisyphus
