%define _unpackaged_files_terminate_build 1
%define git 24d9c9d

Name:    frugally-deep
Version: 0.18.2
Release: alt1.g%{git}
Summary: Use Keras models in C++ with ease
Group:   Development/C++
License: MIT
URL:     https://github.com/Dobiasd/frugally-deep
Vcs:     https://github.com/Dobiasd/frugally-deep

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libfplus-devel nlohmann-json-devel eigen3-devel

BuildArch: noarch

%description
A small header-only library written in modern and pure C++.

- is very easy to integrate and use.
- supports inference ('model.predict') not only for sequential models but also
  for computational graphs with a more complex topology, created with the
  functional API.
- re-implements a small subset of TensorFlow, i.e., the operations needed to
  support prediction.
- results in a much smaller binary size than linking against TensorFlow.

%package devel
Summary: Use Keras models in C++ with ease
Group:   Development/C++
Requires: libfplus-devel eigen3-devel

%description devel
A small header-only library written in modern and pure C++.

- is very easy to integrate and use.
- supports inference ('model.predict') not only for sequential models but also
  for computational graphs with a more complex topology, created with the
  functional API.
- re-implements a small subset of TensorFlow, i.e., the operations needed to
  support prediction.
- results in a much smaller binary size than linking against TensorFlow.

%prep
%setup
%patch -p1

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  %nil
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE *.cff
%doc *.md
%_includedir/*
%_datadir/cmake/*

%changelog
* Sat Apr 11 2026 L.A. Kostis <lakostis@altlinux.ru> 0.18.2-alt1.g24d9c9d
- Initial build for ALTLinux.

