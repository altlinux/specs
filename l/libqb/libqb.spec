# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen /usr/bin/pkg-config /usr/bin/splint gcc-c++ pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libqb
Version:        0.13.0
Release:        alt1_1
Summary:        An IPC library for high performance servers

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.libqb.org
Source0:        https://fedorahosted.org/releases/q/u/quarterback/%{name}-%{version}.tar.xz

Patch1:         0000-test-with-output.patch

BuildRequires:  libtool doxygen procps libcheck-devel automake
Source44: import.info

#Requires: <nothing>

%description
libqb provides high performance client server reusable features.
Initially these are IPC and poll.

%prep
%setup -q

%patch1 -p1

# work-around for broken epoll in rawhide/f17
%build
./autogen.sh
%configure --disable-static ac_cv_func_epoll_create1=no ac_cv_func_epoll_create=no
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*

%files
%doc COPYING
%{_libdir}/libqb.so.*

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libqb = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%doc COPYING README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*

%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_1
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_1
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.0-alt1_1
- update to new release by fcimport

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_2
- update to new release by fcimport

* Tue Jan 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_1
- initial import by fcimport

