
Name: libopensync-plugin-moto
Version: 0.36
Release: alt1.2.1

Summary: Plugin for syncing with Motorola phones via libopensync
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2

Requires: libopensync = %version
Requires: libopensync-plugin-python >= %version

BuildRequires: cmake
BuildRequires: rpm-build-licenses
BuildRequires: libopensync-devel = %version

%description
Plugin for syncing with Motorola phones via libopensync.

%prep
%setup -q

%build
mkdir build
cd build
cmake -D CMAKE_INSTALL_PREFIX:PATH=%_prefix \
	-D OPENSYNC_LIBEXEC_DIR=%_libexecdir/opensync-1.0 \
%if %{_lib} == lib64
	-D LIB_SUFFIX=64 \
%endif
    -D CMAKE_SKIP_RPATH:BOOL=TRUE ../

%make_build

%install
pushd build
%make_install install DESTDIR=%buildroot
popd

%files
%doc AUTHORS COPYING
%_libdir/opensync-1.0/python-plugins/motosync*
%_datadir/opensync-1.0/defaults/moto-sync

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.36-alt1.2.1
- Rebuild with Python-2.7

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.36-alt1.2
- Rebuilt with python 2.6

* Sun Feb 10 2008 Grigory Batalov <bga@altlinux.ru> 0.36-alt1.1
- Rebuilt with python-2.5.

* Tue Jan 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.36-alt1
- 0.36 release for developers

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.35-alt1
- 0.35 release for developers
- Initial package

