Name: libbctoolbox
Version: 5.4.124
Release: alt1
Summary: Utilities library used by Belledonne Communications softwares
Group: System/Libraries
License: GPLv3
Url: https://gitlab.linphone.org/BC/public/bctoolbox
Vcs: https://github.com/BelledonneCommunications/bctoolbox
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): cmake

# Automatically added by buildreq on Thu Mar 02 2017
# optimized out: bcunit gnu-config libstdc++-devel perl pkg-config python-base
BuildRequires: bcunit-devel gcc-c++ libmbedtls-3.6-devel

%description
Utilities library used by Belledonne Communications
softwares like belle-sip, mediastreamer2 and linphone.

%package devel
Summary: Development libraries for bctoolbox
Group: Development/Other
Requires: %name = %version-%release

%description devel
Libraries and headers required to develop software with belle-sip, mediastreamer2 and linphone.

%prep
%setup
%patch0 -p1

%build
%cmake -DBUILD_SHARED_LIBS=TRUE
%cmake_build

%install
%cmakeinstall_std

%files
%doc CHANGELOG.md LICENSE.txt README.md
%_libdir/*.so.*

%files devel
%_bindir/bctoolbox-tester
%_includedir/bctoolbox
%_libdir/libbctoolbox-tester.so
%_libdir/libbctoolbox.so
%_libdir/pkgconfig/bctoolbox-tester.pc
%_libdir/pkgconfig/bctoolbox.pc
%_datadir/BCToolbox

%changelog
* Thu Aug 06 2026 Leontiy Volodin <lvol@altlinux.org> 5.4.124-alt1
- New version 5.4.124.
- Added vcs tag.
- Fixed build on gcc 15.3.1.

* Thu Jun 11 2026 Leontiy Volodin <lvol@altlinux.org> 5.4.120-alt1
- 5.4.120.

* Thu Jan 15 2026 Leontiy Volodin <lvol@altlinux.org> 5.4.74-alt1
- 5.4.74.

* Fri Oct 17 2025 Leontiy Volodin <lvol@altlinux.org> 5.4.50-alt1
- 5.4.50.
- Build with libmbedtls-3.6.

* Wed Aug 13 2025 Leontiy Volodin <lvol@altlinux.org> 5.4.36-alt1
- 5.4.36

* Wed Jun 04 2025 Leontiy Volodin <lvol@altlinux.org> 5.4.20-alt1
- 5.4.20

* Fri Mar 28 2025 Leontiy Volodin <lvol@altlinux.org> 5.4.2-alt1
- 5.4.2

* Thu Mar 13 2025 Leontiy Volodin <lvol@altlinux.org> 5.4.0-alt1
- 5.4.0

* Fri Aug 02 2024 Andrey Cherepanov <cas@altlinux.org> 5.3.74-alt1
- 5.3.74

* Thu Oct 26 2023 Alexei Takaseev <taf@altlinux.org> 5.2.109-alt1
- 5.2.109 (ALT #48191)
- Use Cmake for build

* Wed Jan 19 2022 Alexander Danilov <admsasha@altlinux.org> 0.6.0-alt5
- fixed FTBFS

* Sun Jul 11 2021 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt4
- Build with mbedtls 2.27.0
- Fix License

* Thu Oct 24 2019 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt3
- Build with gcc8

* Mon Mar 12 2018 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt2
- Rebuild with mbedtls 2.7.0

* Sat Jul 22 2017 Alexei Takaseev <taf@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Mar 02 2017 Alexei Takaseev <taf@altlinux.org> 0.5.1-alt1
- 0.5.1

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus
