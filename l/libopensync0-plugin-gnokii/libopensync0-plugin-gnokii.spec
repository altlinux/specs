%define orig_name libopensync-plugin-gnokii
#set_verify_elf_method relaxed

Name: libopensync0-plugin-gnokii
Version: 0.22
Release: alt3

Summary: Gnokii plugin for OpenSync
License: GPL
Group: System/Libraries

URL: http://www.opensync.org/
Source: %orig_name-%version.tar.bz2
Patch0: libopensync-plugin-gnokii-add_new_entries.diff
Patch1: alt-build.diff
Patch2: libopensync-plugin-gnokii_enum.patch
Patch3: libopensync0-plugin-gnokii-0.22-alt-no-Werror.patch
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Requires: libgnokii 
Requires: libopensync0 = %version
# Conflicts: %orig_name

# Automatically added by buildreq on Thu Oct 16 2008
BuildRequires: gcc-c++ gcc-fortran glib2-devel glibc-devel-static libgnokii-devel libopensync0-devel libxml2-devel

%description
This a _experimental_ OpenSync plugin for Nokia cellphones. Don't use it
without a whole backup of your phonebook, todo list and calendar! This
plugin is based on gnokii which can be found on http://gnokii.org
It is recommended to use the latest version of gnokii.

%prep
%setup -n %orig_name-%version
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
%configure
%make

%install
%makeinstall_std
rm -f %buildroot%_libdir/opensync/*/*.la

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_libdir/opensync/plugins/*.so
%_libdir/opensync/formats/*.so
%_datadir/opensync/defaults/*

%changelog
* Wed Feb 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.22-alt3
- Rebuilt with new libgnokii.

* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt2.4
- Fixed build

* Fri Aug 06 2010 Michael Shigorin <mike@altlinux.org> 0.22-alt2.3
- *rebuilt* with Fedora patch

* Wed Aug 04 2010 Michael Shigorin <mike@altlinux.org> 0.22-alt2.2
- rebuilt against current libgnokii

* Mon Jan 11 2010 Michael Shigorin <mike@altlinux.org> 0.22-alt2.1
- rebuilt against current libgnokii

* Thu Oct 16 2008 Andriy Stepanov <stanv@altlinux.ru> 0.22-alt2
- Stable version.

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 12 2007 Alexey Shabalin <shaba@altlinux.ru> 0.21-alt1
- 0.21
- cleanup spec(drop cvs)

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.20-alt1
- release 0.20

* Tue Oct 03 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921
- Initial package
