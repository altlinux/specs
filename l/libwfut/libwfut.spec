BuildRequires: gcc-c++
%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           libwfut
Version:        0.2.2
Release:        alt1_1.1
Summary:        Software updater tool for WorldForge applications

Group:          Development/C++
License:        LGPLv2+
URL:            http://www.worldforge.org/
Source0:        http://downloads.sourceforge.net/worldforge/%{name}-%{version}.tar.gz

BuildRequires:  libsigc++2-devel libcurl-devel zlib-devel tinyxml-devel python-devel swig
Source44: import.info

%description
libwfut is the WorldForge Update Tool (WFUT) client side implementation in C++
for use directly by WorldForge clients.


%package devel
Summary: Development files for libwfut library
Group:   Development/C++
Requires: pkgconfig %{name} = %{version}-%{release} libsigc++2-devel libcurl-devel zlib-devel


%description devel
Development libraries and headers for linking against the libwfut library.


%package -n python-module-%name
Summary: Python interface for libwfut library
Group:   Development/C++
Provides: libwfut-python = %{version}-%{release}


%description -n python-module-%name
Python interface for libwfut library.


%prep
%setup -q

echo "python_sitelib == %{python_sitelib}"
echo "python_sitearch == %{python_sitearch}"


%build
%configure --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

#rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

#rm -f $RPM_BUILD_ROOT%{python_sitelib}/%{name}/*.a
rm -f $RPM_BUILD_ROOT%{python_sitearch}/%{name}/*.la

## cleaning up redundant docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

# remove wfut binary from package - will return it back when java wfut package will be obsoleted
rm -f $RPM_BUILD_ROOT%{_bindir}/wfut
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/wfut.1


%check
make check

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
#%{_bindir}/wfut
#%{_mandir}/man1/wfut.1.gz
%{_libdir}/libwfut-0.2.so.*


%files devel
%{_includedir}/%{name}-0.2
%{_libdir}/libwfut-0.2.so
%{_libdir}/pkgconfig/*.pc

%files -n python-module-%name
%{python_sitearch}/%{name}


%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.2-alt1_1.1
- Rebuild with Python-2.7

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- initial release by fcimport

