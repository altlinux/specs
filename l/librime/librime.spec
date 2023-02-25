# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           librime
Version:        1.8.4
Release:        alt1_2
Summary:        Rime Input Method Engine Library

License:        GPLv3
URL:            https://rime.im/
Source0:        https://github.com/rime/librime/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  ctest cmake, opencc-devel
BuildRequires:  boost-complete >= 1.46
BuildRequires:  zlib-devel
BuildRequires:  libglog-devel, libgtest-devel
BuildRequires:  libyaml-cpp-devel
BuildRequires:  libgflags-devel
BuildRequires:  libmarisa-devel
BuildRequires:  libleveldb-devel
BuildRequires:  capnproto, capnproto-devel
Source44: import.info

%description
Rime Input Method Engine Library

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

%package -n librime1
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n librime1
Rime Input Method Engine Library

Support for shape-based and phonetic-based input methods,
including those for Chinese dialects.

A selected dictionary in Traditional Chinese,
powered by opencc for Simplified Chinese output.

This package contains the shared library.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       librime1 = %EVR

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Group: Development/C
Summary:        Tools for %{name}
Requires:       librime1 = %EVR

%description    tools
The %{name}-tools package contains tools for %{name}.


%prep
%setup -q


%build
%{fedora_v2_cmake} -DCMAKE_BUILD_TYPE=Release
%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install





%files -n librime1
%doc README.md LICENSE
%_libdir/librime.so.1
%_libdir/librime.so.1.*


%files devel
#doc %_docdir/%name
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/rime.pc
%dir %{_datadir}/cmake/rime
%{_datadir}/cmake/rime/RimeConfig.cmake


%files tools
%{_bindir}/rime_deployer
%{_bindir}/rime_dict_manager
%{_bindir}/rime_patch


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 1.8.4-alt1_2
- update to new release by fcimport

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 1.7.3-alt1_2
- new version

