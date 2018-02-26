%set_verify_elf_method relaxed

Name: libopensync-plugin-vformat
Version: 0.36
Release: alt1

Summary: Vformat plugin for OpenSync
License: %lgpl2plus
Group: System/Libraries
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2

Requires: libopensync = %version

BuildRequires: gcc-c++ glib2-devel libxml2-devel pkg-config zlib-devel cmake libcheck-devel rpm-build-licenses
BuildRequires: libopensync-devel = %version

%description
This plugin is based on vformat.{c,h} which got adapted from evolution e-vcard
parser. vformat.{c,h} parsing and assembling of vObject-like formatting. The
term vformat is often use to describe this format of vCard 2.1, vCard 3.0,
vCalendar, iCalendar and vNote.

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
%_bindir/vconvert
%_libdir/opensync-1.0/formats/*

%changelog
* Tue Jan 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.36-alt1
- 0.36 release for developers

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.35-alt1
- 0.35 release for developers
- Initial package
