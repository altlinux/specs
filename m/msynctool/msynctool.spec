Name:  msynctool
Version: 0.36
Release: alt1

Summary: A calendar (and other PIM data) synchronization program (Command line version)
License: %gpl2only
Group: Communications
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %name-%version.tar.bz2

Requires: libopensync = %version

Provides: multisync0.90-cli 
Provides: multisync-cli  = %version-%release
Obsoletes: multisync0.90-cli 
Obsoletes: multisync-cli < 0.35

BuildRequires: cmake gcc-c++ glib2-devel libopensync-devel libxml2-devel pkg-config rpm-build-licenses

%description
MultiSync is a program to synchronize calendars, addressbooks and other PIM data
between programs on your computer and other computers, mobile devices, PDAs or
cell phones. It relies on the OpenSync framework to do the actual
synchronisation.
Command line version of MultiSync. To allow synchronisation on machines which
lack a X server.

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
%_bindir/msynctool
%doc AUTHORS CODING COPYING README

%changelog
* Tue Jan 29 2008 Alexey Shabalin <shaba@altlinux.ru> 0.36-alt1
- 0.36 release for developers

* Mon Jan 21 2008 Alexey Shabalin <shaba@altlinux.ru> 0.35-alt1
- 0.35 release for developers
- rename package to msynctool

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1 
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanup spec(drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Wed Oct 11 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1cvs20060529
- two src rpm package: cli and gui
- add doc

* Tue Mar 07 2006 Alexey Shabalin <shaba@altlinux.ru> 0.90.18-alt2
- fix BuildRequires

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.90.18-alt1
- 0.18 release
- build for Sisyphus
- add Packager SynCE Development Team

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.90.18-alt0.1.cvs20050930
- Initial package
