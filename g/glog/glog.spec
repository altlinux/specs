Name: glog
Version: 0.3.4
Release: alt4
Summary: C++ implementation of Google logging module
License: BSD
Group: Development/C++
Url: https://github.com/google/glog

Source: %name-%version.tar
BuildRequires: gcc-c++

%description
C++ implementation of Google logging module

%package -n lib%{name}
Group: Development/C++
Summary: C++ implementation of Google logging module

%description -n lib%{name}
C++ implementation of Google logging module.

%package -n lib%{name}-devel
Summary: Development tools for programs which will use Google logging library
Group: Development/C++
Requires: lib%{name} = %version-%release

%description -n lib%{name}-devel
C++ implementation of Google logging module.
Development tools.

%prep
%setup

%build
%configure \
%ifarch x86_64
	--enable-frame-pointers \
%endif
	#

%make_build

%install
%makeinstall_std
rm -rf %_datadir/doc/%name-%version
rm -f %_libdir/lib%{name}.a

%files -n lib%{name}
%_libdir/lib%{name}.so.*
%doc README ChangeLog AUTHORS COPYING doc/*

%files -n lib%{name}-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc


%changelog
* Tue Feb 13 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.4-alt4
- Fixed build on non-x86 architectures.

* Thu Jul 02 2015 Dmitry Derjavin <dd@altlinux.org> 0.3.4-alt3
- Fixed typo in devel package requirements.

* Mon Jun 22 2015 Dmitry Derjavin <dd@altlinux.org> 0.3.4-alt2
- Unused files removed.

* Mon Jun 22 2015 Dmitry Derjavin <dd@altlinux.org> 0.3.4-alt1
- Initial ALT Linux build.

