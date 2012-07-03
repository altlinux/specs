# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/bison /usr/bin/docbook-to-man /usr/bin/docbook2html /usr/bin/doxygen /usr/bin/gtkdocize /usr/bin/guile /usr/bin/guile-config /usr/bin/indent /usr/bin/valgrind cppunit-devel gcc-c++ guile18-devel imlib2-devel libGL-devel libX11-devel libXext-devel libaccounts-glib-devel libexpat-devel libfreetype-devel libreadline-devel libuuid-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary: A library for accessing deltacloud
Name: libdeltacloud
Version: 0.9
Release: alt2_2
License: LGPLv2+
Group: System/Libraries
URL: http://people.redhat.com/clalance/libdeltacloud
Source0: http://people.redhat.com/clalance/libdeltacloud/%{version}/%{name}-%{version}.tar.gz
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
Source44: import.info

%description
Libdeltacloud is a library for accessing deltacloud via a
convenient C API.

%package devel
Summary: Header files for libdeltacloud library
License: LGPLv2+
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
The libdeltacloud-devel package contains the files needed for developing
applications that need to use the libdeltacloud library.

%prep
%setup -q

%build
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install
make DESTDIR="${RPM_BUILD_ROOT}" install

# Move the symlink
rm -f $RPM_BUILD_ROOT/%{_lib}/%{name}.so
mkdir -p $RPM_BUILD_ROOT%{_libdir}
VLIBNAME=$(ls $RPM_BUILD_ROOT/%{_lib}/%{name}.so.*.*.*)
LIBNAME=$(basename $VLIBNAME)
ln -s ../../%{_lib}/$LIBNAME $RPM_BUILD_ROOT%{_libdir}/%{name}.so

# Move the pkgconfig file
mv $RPM_BUILD_ROOT/%{_lib}/pkgconfig $RPM_BUILD_ROOT%{_libdir}

# Remove a couple things so they don't get picked up
rm -f $RPM_BUILD_ROOT/%{_lib}/libdeltacloud.la
rm -f $RPM_BUILD_ROOT/%{_lib}/libdeltacloud.a

%files
%doc COPYING
%attr(0755,root,root) /%{_lib}/libdeltacloud.so.*

%files devel
%attr(0644,root,root) %{_includedir}/libdeltacloud/action.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/address.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/bucket.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/driver.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/hardware_profile.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/image.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/instance.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/instance_state.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/key.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/libdeltacloud.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/link.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/loadbalancer.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/realm.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/storage_snapshot.h
%attr(0644,root,root) %{_includedir}/libdeltacloud/storage_volume.h
%attr(0755,root,root) %{_libdir}/libdeltacloud.so
%{_libdir}/pkgconfig/libdeltacloud.pc

%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_1
- initial import by fcimport

