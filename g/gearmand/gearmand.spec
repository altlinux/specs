%define _unpackaged_files_terminate_build 1

Summary: Gearman provides a generic application framework to farm out work to other machines.
Name: gearmand
Version: 1.1.21
Release: alt1
License: BSD
Group: Development/C
URL: https://gearman.org/

VCS: https://github.com/gearman/gearmand.git
Source: %name-%version.tar

BuildRequires: perl gcc-c++ boost-devel boost-program_options-devel libevent-devel libuuid-devel gperf
BuildRequires: libsqlite3-devel libtokyocabinet-devel libmemcached-devel memcached libhiredis-devel
BuildRequires: mysql-devel postgresql-devel zlib-devel
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink python3-module-sphinx_rtd_theme
BuildRequires: libssl-devel

%description
%summary

%package devel
Summary:        Gearmand development files
Group:          Development/C++
Requires:       %name = %EVR

%description devel
This package contains necessary header files for Gearman development.

%prep
%setup
# provide information about version needed for bootstrap
sed -i -e 's:git describe --always:echo %version:' \
	version.m4 \
	configure.ac

%build
# without following export it fails to build with new boost for some reason on ppc64le
export ax_boost_user_program_options_lib=boost_program_options
%autoreconf
%configure \
	--enable-ssl \
	--disable-static \
	--localstatedir=%_var \
	%nil

# first build docs
pushd docs
%make_build
popd

%make_build

%install
%makeinstall_std

%files
%doc ChangeLog README.md COPYING
%_bindir/gearman
%_bindir/gearadmin
%_libdir/libgearman.so.*
%_sbindir/gearmand
%_man1dir/*
%_man8dir/*

%files devel
%_includedir/libgearman/*
%_includedir/libgearman-1.0/*
%_libdir/libgearman.so
%_pkgconfigdir/gearmand.pc
%_man3dir/*

%changelog
* Wed Jul 10 2024 Anton Farygin <rider@altlinux.ru> 1.1.21-alt1
- 1.1.19.1 -> 1.1.21

* Mon Aug 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.19.1-alt1
- Updated to upstream version 1.1.19.1.

* Thu Nov 14 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.18-alt3
- Rebuilt with boost-1.71.0.

* Wed Mar 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.1.18-alt2
- Fix FTBFS against libmysqlclient.so.21

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.18-alt1.2
- NMU: Rebuild with new openssl 1.1.0.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.18-alt1.1
- NMU: rebuilt with boost-1.67.0

* Thu Apr 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.18-alt1
- Updated to upstream version 1.1.18.

* Mon Sep 18 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.17-alt1.1
- Rebuild with libhiredis 1.13.3

* Fri Sep 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.17-alt1
- Updated to upstream release version 1.1.17.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.18-alt1.6.qa1.1
- rebuild with boost 1.57.0

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.18-alt1.6.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.6
- Rebuilt with Boost 1.52.0

* Tue Nov 06 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.18-alt1.5
- Fix build with GCC 4.6

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.4
- Rebuilt with Boost 1.51.0

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.1
- Rebuilt with Boost 1.47.0

* Tue May 31 2011 Sergey Alembekov <rt@altlinux.ru> 0.18-alt1
- initial release for ALTLinux 

