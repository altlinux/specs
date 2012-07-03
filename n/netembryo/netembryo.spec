# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gawk pkgconfig(glib-2.0)
# END SourceDeps(oneline)
#%%define git 1
%define rev 20071031

Summary: Network abstraction library
Name: netembryo
Version: 0.1.1
Release: alt2_2
License: LGPLv2+
Group: Development/C
%if %{?git:1}0
# http://live.polito.it/gitweb/?p=netembryo.git;a=snapshot;h=HEAD
Source: %{name}-%{rev}git.tar.gz
%else
Source: http://www.lscube.org/files/downloads/netembryo/%{name}-%{version}.tar.bz2
%endif
URL: http://www.lscube.org/projects/netembryo
BuildRequires: liblksctp-devel
%{?git:BuildRequires: libtool}
Source44: import.info

%description
Netembryo is a network abstraction library (originated from our old wrapper
socket) plus some misc utility functions used as foundation for feng,
libnemesi, felix.

It provides an uniform access to the following protocols:

    * UDP
    * TCP
    * SCTP

%package devel
Summary: Netembryo development library and headers
Group: Development/C
Requires: %{name} = %{version}-%{release}

%description devel
The netembryo-devel package contains the header files and some
documentation needed to develop application with netembryo.

%prep
%setup -q %{?git:-n %{name}.git}

%build
%{?git:autoreconf -i}
%configure --disable-dependency-tracking --disable-static --without-openssl
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install
%{__rm} %{buildroot}%{_libdir}/libnetembryo.la

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/libnetembryo.so.*

%files devel
%{_includedir}/netembryo
%{_libdir}/libnetembryo.so
%{_libdir}/pkgconfig/libnetembryo*.pc

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt2_2
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_2
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_1
- initial import by fcimport

