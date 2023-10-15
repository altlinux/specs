%define rname fmt
%define sover 9

Name: %rname%sover
Version: 9.1.0
Release: alt1.3
Epoch: 1

Summary: An open-source formatting library for C++
License: BSD
Group: System/Legacy libraries
Url: http://fmtlib.net/

# https://github.com/fmtlib/fmt/archive/%version/%rname-%version.tar.gz
Source: %rname-%version.tar

BuildRequires: cmake ctest gcc-c++

%package -n lib%rname%sover
Summary: An open-source formatting library for C++
Group: System/Libraries

%define desc fmt (formerly cppformat) is an open-source formatting library. \
It can be used as a fast and safe alternative to printf and IOStreams.

%description
%desc

%description -n lib%rname%sover
%desc

%prep
%setup -n %rname-%version

%build
%cmake_insource \
	-DFMT_PKGCONFIG_DIR=%_pkgconfigdir \
	-DBUILD_SHARED_LIBS=ON \
	%nil

%make_build VERBOSE=1

%ifnarch %ix86
%check
export LD_LIBRARY_PATH=%buildroot%_libdir
make test
%endif

%install
%makeinstall_std

%__rm -rf %buildroot%_includedir
%__rm -rf %buildroot%_libdir/cmake
%__rm -rf %buildroot%_pkgconfigdir
%__rm -rf %buildroot%_libdir/lib%rname.so

%files -n lib%rname%sover
%doc LICENSE* README*
%_libdir/libfmt.so.*

%changelog
* Sun Oct 15 2023 Nazarov Denis <nenderus@altlinux.org> 1:9.1.0-alt1.3
- Build as legacy library

* Sat Jul 01 2023 Nazarov Denis <nenderus@altlinux.org> 1:9.1.0-alt1.2
- Fix FTBFS

* Thu May 18 2023 Nazarov Denis <nenderus@altlinux.org> 1:9.1.0-alt1.1
- Rollback to version 9.0.1.

* Wed May 10 2023 Nazarov Denis <nenderus@altlinux.org> 10.0.0-alt1
- Updated to upstream version 10.0.0.

* Sat Aug 27 2022 Nazarov Denis <nenderus@altlinux.org> 9.1.0-alt1
- Updated to upstream version 9.0.1.

* Wed Jul 06 2022 Nazarov Denis <nenderus@altlinux.org> 9.0.0-alt1
- Updated to upstream version 9.0.0.

* Fri Jan 07 2022 Nazarov Denis <nenderus@altlinux.org> 8.1.1-alt1
- Updated to upstream version 8.1.1.

* Sat Nov 06 2021 Nazarov Denis <nenderus@altlinux.org> 8.0.1-alt1
- Updated to upstream version 8.0.1.

* Sun Jan 24 2021 Nazarov Denis <nenderus@altlinux.org> 7.1.3-alt1
- Updated to upstream version 7.1.3.

* Fri Jun 05 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.1-alt1
- Updated to upstream version 6.2.1.

* Fri Apr 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.2.0-alt1
- Updated to upstream version 6.2.0.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.1.2-alt1
- Updated to upstream version 6.1.2.

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.3.0-alt1
- initial
