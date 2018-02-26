%define orig_name msynctool
Name:  msynctool0
Version: 0.22
Release: alt2.1

Summary: A calendar (and other PIM data) synchronization program (Command line version)
License: %gpl2only
Group: Communications
URL: http://www.opensync.org/
Packager: Mobile Development Team <mobile@packages.altlinux.org>

Source: %orig_name-%version.tar.bz2

Requires: libopensync0 = %version
Conflicts: %orig_name

# Provides: multisync0.90-cli 
# Provides: multisync-cli  = %version-%release
# Obsoletes: multisync0.90-cli 

# Automatically added by buildreq on Fri Oct 17 2008
BuildRequires: gcc-c++ gcc-fortran glib2-devel glibc-devel-static libopensync0-devel libxml2-devel
BuildRequires: rpm-build-licenses

%description
MultiSync is a program to synchronize calendars, addressbooks and other PIM data
between programs on your computer and other computers, mobile devices, PDAs or
cell phones. It relies on the OpenSync framework to do the actual
synchronisation.
Command line version of MultiSync. To allow synchronisation on machines which
lack a X server.

%prep
%setup -q -n %orig_name-%version

%build
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make

%install
%make_install install DESTDIR=%buildroot

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/msynctool
%{_bindir}/convcard
%{_bindir}/convtest
%{_man1dir}/convcard.1*
%{_man1dir}/msynctool.1*

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt2.1
- Removed bad RPATH

* Fri Oct 17 2008 Andriy Stepanov <stanv@altlinux.ru> 0.22-alt2
- Stable version

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
