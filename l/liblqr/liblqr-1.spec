# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(glib-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname liblqr-1
Name:           liblqr
Version:        0.4.1
Release:        alt2.1_2
Summary:        LiquidRescale library
Group:          System/Libraries
License:        GPLv3
URL:            http://liquidrescale.wikidot.com/
Source0:        http://liblqr.wikidot.com/local--files/en:download-page/%{oldname}-%{version}.tar.bz2
BuildRequires:  libglib2-devel
Source44: import.info

%description
The LiquidRescale (lqr) library provides a C/C++ API for
performing non-uniform resizing of images by the seam-carving
technique.

%package devel
Summary:        LiquidRescale library  development kit
Group:          System/Libraries
License:        GPLv3
Requires:       liblqr = %{version}-%{release}
Requires:       libglib2-devel pkgconfig

%description devel
The libqr-devel package contains the header files
needed to develop applications with liblqr


%prep
%setup -q -n %{oldname}-%{version}

%build
export LDFLAGS="`pkg-config --libs glib-2.0` -lm"
%configure
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# remove .la files
find $RPM_BUILD_ROOT -name \*.la -exec %{__rm} -f {} \;

# Fedora MUST
%files 
%doc README ChangeLog COPYING
%{_libdir}/liblqr-1.so.0.3.1
%{_libdir}/liblqr-1.so.0

%files devel
%doc docs/liblqr_manual.docbook
%{_libdir}/liblqr-1.so
%{_includedir}/lqr-1/
%{_libdir}/pkgconfig/lqr-1.pc


%changelog
* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2.1_2
- initial import by fcimport

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2.1
- Rebuilt for debuginfo

* Wed Nov 10 2010 Victor Forsiuk <force@altlinux.org> 0.4.1-alt2
- Rebuilt for soname set-versions.

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Dec 16 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt2
- Remove obsolete ldconfig calls.

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt1
- 0.2.1

* Wed Apr 02 2008 Victor Forsyuk <force@altlinux.org> 0.1.0-alt1
- Initial build.
