# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/gtkdocize /usr/sbin/nscd libldap-devel libpam0-devel libpopt-devel
# END SourceDeps(oneline)
BuildRequires: OpenSP
%add_optflags %optflags_shared
# python macros required
BuildRequires(pre): rpm-build-python
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name: libuser
Version: 0.57.6
Release: alt1_1
Group: System/Base
License: LGPLv2+
URL: https://fedorahosted.org/libuser/
Source: https://fedorahosted.org/releases/l/i/libuser/libuser-%{version}.tar.xz
BuildRequires: glib2-devel linuxdoc-tools pam-devel popt-devel python-devel
BuildRequires: libsasl2-devel libselinux-devel openldap-devel
# To make sure the configure script can find it
BuildRequires: nscd
# For %%check
BuildRequires: openldap-clients openldap-servers openssl
Summary: A user and group account administration library
Source44: import.info
Patch33: libuser-0.57.2-alt-modularized_ldap.patch

%description
The libuser library implements a standardized interface for manipulating
and administering user and group accounts.  The library uses pluggable
back-ends to interface to its data sources.

Sample applications modeled after those included with the shadow password
suite are included.

%package devel
Group: Development/C
Summary: Files needed for developing applications which use libuser
Requires: libuser = %{version}-%{release}
Requires: glib2-devel

%description devel
The libuser-devel package contains header files, static libraries, and other
files useful for developing applications with libuser.

%package -n python-module-libuser
Summary: Python bindings for the libuser library
Group: Development/C
Requires: libuser = %{version}-%{release}

%description -n python-module-libuser
The libuser-python package contains the Python bindings for
the libuser library, which provides a Python API for manipulating and
administering user and group accounts.

%prep
%setup -q
%patch33 -p0

%build
%configure --with-selinux --with-ldap --with-html-dir=%{_datadir}/gtk-doc/html
make

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

%find_lang %{name}

%check

make check

# Verify that all python modules load, just in case.
LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH
cd $RPM_BUILD_ROOT/%{python_sitelibdir}
python -c "import libuser"

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README TODO docs/*.txt
%config(noreplace) %{_sysconfdir}/libuser.conf

%attr(0755,root,root) %{_bindir}/*
%{_libdir}/*.so.*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%attr(0755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%exclude %{_libdir}/%{name}/*.la

%files -n python-module-libuser
%doc python/modules.txt
%{python_sitelibdir}/*.so
%exclude %{python_sitelibdir}/*.la

%files devel
%{_includedir}/libuser
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/html/*

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.57.6-alt1_1
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.57.4-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.3-alt2_2
- spec cleanup thanks to ldv@

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.57.3-alt1_2.1
- Rebuild with Python-2.7

* Fri Oct 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.3-alt1_2
- update to new release by fcimport

* Thu Oct 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.3-alt1_1
- update to new release by fcimport

* Mon Aug 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.57.2-alt1_1
- initial release by fcimport

