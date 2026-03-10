#Enable ZeroMQ support (builds Python client for server communication)
%def_with zeromq

#Enable ezHPC UIT support: adds optional UIT-based HPC integration and SSL certs.
%def_without ezHPC

#Documentation
%def_with docs


Name:    molequeue
Version: 0.9.0
Release: alt1

Summary: Desktop integration of high performance computing resources
Group: Sciences/Chemistry
License: BSD-3-Clause
URL: https://www.openchemistry.org/projects/molequeue/
VCS: https://github.com/OpenChemistry/molequeue

Source: %name-%version.tar
Source2: %name.desktop

Patch0: molequeue-python3.13.patch

BuildRequires(pre): rpm-build-cmake
%{?_with_zeromq:BuildRequires(pre): rpm-build-python3}

#BuildRequires: /proc - Mounting /proc does not affect the build
BuildRequires: qt5-base-devel
BuildRequires: gcc-c++

%{?_with_docs:BuildRequires: doxygen}
%{?_with_zeromq:BuildRequires: libzeromq-cpp-devel}
%{?_with_ezHPC:BuildRequires: kde5-kdsoap-devel qt5-xmlpatterns-devel}


%description
MoleQueue is an open-source, cross-platform, system-tray resident desktop
application for abstracting, managing, and coordinating the execution of tasks
both locally and on remote computational resources. Users can set up local and
remote queues that describe where the task will be executed. Each queue can
have programs, with templates to facilitate the execution of the program. Input
files can be staged, and output files collected using a standard interface.
Some highlights:

* Open source distributed under the liberal 3-clause BSD license
* Cross platform with nightly builds on Linux, Mac OS X and Windows
* Intuitive interface designed to be useful to whole community
* Support for local executation and remote schedulers (SGE, PBS, SLURM)
* System tray resident application managing queue of queues and job lifetime
* Simple, lightweight JSON-RPC 2.0 based communication over local sockets
* Qt 5 client library for simple integration in Qt applications


%package -n lib%name
Summary: Shared and private libraries of %name
Group: System/Libraries

%description -n lib%name
Shared and private libraries of %name.


%package -n lib%name-devel
Summary:  Development files of %name
Requires: lib%name = %version-%release
Group: Development/C++

%description -n lib%name-devel
This package contains libraries and header files for developing
applications that use %name.


%if_with zeromq
%package -n python3-module-%name
BuildArch: noarch
Summary: Python3 module for Molequeue
Group: Development/Python3

%description -n python3-module-%name
Python3 module providing API client to communicate with MoleQueue server over ZeroMQ.
%endif


%if_with docs
%package doc
Summary: HTML documentation of %name
BuildArch: noarch
Group: Development/Documentation

%description doc
HTML documentation of %name.
%endif

%prep
%setup
%patch0 -p1


%build
%cmake -Wno-dev \
 -DENABLE_RPATH:BOOL=OFF \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DENABLE_TESTING:BOOL=OFF \
 -DBUILD_DOCUMENTATION:BOOL=%{with docs} \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
 -DMoleQueue_BUILD_APPLICATION:BOOL=ON \
 -DMoleQueue_BUILD_CLIENT:BOOL=ON \
 -DUSE_ZERO_MQ:BOOL=%{with zeromq} \
 -DMoleQueue_USE_EZHPC_UIT:BOOL=%{with ezHPC} \
 -DPYTHON_EXECUTABLE:FILEPATH=%__python3 \
 -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build

%if_with docs
pushd %_target_platform/docs
doxygen
popd
%endif

%install
%cmake_install

rm -rv %buildroot%_datadir/doc

install -Dm644 molequeue/app/icons/%name.png %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -Dm644 %SOURCE2 %buildroot%_desktopdir/%name.desktop


%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/32x32/apps/%name.png
%if_with ezHPC
%_datadir/%name/certs/
%endif
%doc README.md
%doc LICENSE


%files -n lib%name
%_libdir/libMoleQueue*.so
%_libdir/%name/


%files -n lib%name-devel
%_libdir/cmake/%name/
%_includedir/%name/


%if_with zeromq
%files -n python3-module-%name
%python3_sitelibdir_noarch/%name
%endif

%if_with docs
%files doc
%doc README.md %_target_platform/docs/html
%doc LICENSE
%endif

%changelog
* Fri Feb 13 2026 Valentin Sokolov <sova@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.

