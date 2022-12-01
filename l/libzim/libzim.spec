Name:    libzim
Version: 8.1.0
Release: alt1
Summary: Library for reading/writing ZIM files

License: GPLv2+
Group:   System/Libraries
URL:     http://openzim.org/wiki/Main_Page
# VCS:   https://github.com/openzim/libzim

Source0: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: liblzma-devel
BuildRequires: libgtest-devel
BuildRequires: zlib-devel
BuildRequires: cmake
BuildRequires: libxapian-devel
BuildRequires: libicu-devel
BuildRequires: python3-dev
BuildRequires: python3-module-Cython
BuildRequires: ninja-build
BuildRequires: libzstd-devel

Provides: zimlib = %version-%release

%description
The zimlib is the standard implementation of the ZIM specification. It
is a library which implements the read and write method for ZIM files.
Use zimlib in your own software - like reader applications - to make
them ZIM-capable without the need having to dig too much into the ZIM
file format. zimlib is written in C++. It also includes the binaries
zimsearch and zimdump, for directly searching and viewing ZIM file
contents.

%package  devel
Summary:  Development files for %{name}
Group:    Development/Other
Requires: %name = %version-%release
Provides: zimlib-devel = %version-%release

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup
%ifarch %e2k
sed -i "s/compiler.get_id()/'gcc'/" meson.build
%endif

%build
%meson -Dwerror=false
%meson_build 

%install
%meson_install

%files
%doc AUTHORS README.md
%_libdir/*.so.*

%files devel
%doc examples
%_includedir/zim/
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Dec 01 2022 Andrey Cherepanov <cas@altlinux.org> 8.1.0-alt1
- New version.

* Fri Sep 09 2022 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- New version.

* Sat Aug 13 2022 Andrey Cherepanov <cas@altlinux.org> 8.0.0-alt1
- New version.

* Fri May 20 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 7.2.2-alt1.1
- Fixed build for Elbrus

* Thu May 19 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.2-alt1
- New version.

* Sun May 08 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.1-alt1
- New version.

* Sat Jan 22 2022 Andrey Cherepanov <cas@altlinux.org> 7.2.0-alt1
- New version.

* Wed Dec 22 2021 Andrey Cherepanov <cas@altlinux.org> 7.1.0-alt1
- New version.

* Thu Oct 07 2021 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version.

* Thu Jun 10 2021 Andrey Cherepanov <cas@altlinux.org> 6.3.2-alt1
- New version.

* Tue Nov 17 2020 Andrey Cherepanov <cas@altlinux.org> 6.3.0-alt1
- New version.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 6.2.2-alt1
- New version.

* Wed Sep 02 2020 Andrey Cherepanov <cas@altlinux.org> 6.2.1-alt1
- New version.

* Sun Aug 30 2020 Andrey Cherepanov <cas@altlinux.org> 6.2.0-alt1
- New version.

* Sat Jul 18 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.8-alt1
- New version.

* Wed Jul 01 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.7-alt1
- New version.

* Thu Jun 25 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.6-alt1
- New version.

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.5-alt1
- New version.

* Mon May 25 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.4-alt1
- New version.

* Mon May 18 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.3-alt1
- New version.

* Tue May 12 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.2-alt1
- New version.

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.1-alt1
- New version.

* Thu Apr 09 2020 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Tue Oct 01 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Wed Sep 04 2019 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.

* Thu Aug 22 2019 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version.

* Tue Aug 20 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.2-alt1
- New version.

* Tue Jul 30 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version.

* Wed May 29 2019 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Thu Apr 18 2019 Andrey Cherepanov <cas@altlinux.org> 4.0.7-alt1
- New version.

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt2
- Provide zimlib and zimlib-devel for compatibity with Fedora

* Mon Jan 13 2014 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Import to ALT Linux from Fedora
