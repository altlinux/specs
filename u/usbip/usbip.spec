%def_enable shared
%def_enable static
%def_with tcp_wrappers
#----------------------------------------------------------------------
%define subst_with_to() %{expand:%%{?_with_%{1}:--with-%{2}}} %{expand:%%{?_without_%{1}:--without-%{2}}}

%define Name USB/IP
Name: usbip
%define lname lib%name
Summary: Utility for manage %Name devices
Version: 1.1.1
Release: alt2
License: GPLv2+
Group: System/Configuration/Networking
Source: %name-%version.tar
URL: http://www.kernel.org
Obsoletes: %name-common
Obsoletes: %name-client <= %version
Provides: %name-client = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}

BuildRequires: zlib-devel %{?_with_tcp_wrappers:libwrap-devel} libsysfs-devel >= 2.0.0

%description
Utility for manage %Name devices.


%package -n %{name}d
Summary: %Name server daemon
Group: System/Configuration/Networking
Obsoletes: %name-server <= %version
Provides: %name-server = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}

%description -n %{name}d
%Name server daemon.


%if_enabled shared
%package -n %lname
Summary: %Name shared library
Group: System/Libraries

%description -n %lname
%Name shared library.
%endif


%package -n %lname-devel
Summary: %Name devel files
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name devel files.


%if_enabled shared
%package -n %lname-devel-static
Summary: %Name static library
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name static library.
%endif


%prep
%setup -q


%build
./autogen.sh
%configure \
	%{subst_enable shared} \
	%{subst_enable static} \
	%{subst_with_to tcp_wrappers tcp-wrappers} \
	--with-usbids-dir=%_datadir/hwdatabase
%make_build V=1


%install
%makeinstall_std


%files
%doc AUTHORS README
%_sbindir/%name
%_man8dir/%name.*


%files -n %{name}d
%_sbindir/%{name}d
%_man8dir/%{name}d.*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Fri Oct 11 2013 Led <led@altlinux.ru> 1.1.1-alt2
- updated from 3.12 kernel tree

* Thu Aug 08 2013 Led <led@altlinux.ru> 1.1.1-alt1
- 1.1.1
- build from kernel source tree
- subpackages usbip-common and usbip-client replaced with usbip
- subpackage usbip-server replaced with usbipd

* Sat Apr 09 2011 Lenar Shakirov <snejok@altlinux.ru> 0.1.7-alt0.2
- intersections with system packages fixed:
  * %%_usrsrc/ -> %%kernel_src/

* Tue Nov 03 2009 Igor Vlasenko <viy@altlinux.ru> 0.1.7-alt0.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libusbip
  * postun_ldconfig for libusbip

* Sun Aug 10 2008 Led <led@altlinux.ru> 0.1.7-alt0.1
- SVN revision 82

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt2
- fixed kernel-source-usbip

* Tue May 06 2008 Led <led@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Jul 30 2007 Led <led@altlinux.ru> 0.1.5-alt1
- Initial build
- added %name-0.1.5-configure.patch
- added %name-0.1.5-alt-hwdatabase.patch
- added %name-0.1.5-zlib.patch
