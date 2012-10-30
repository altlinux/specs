# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/pkg-config /usr/bin/xsltproc
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname python-caja
Name:           python-module-caja
Version:        1.4.0
Release:        alt1_1.1
Summary:        Python bindings for Caja

Group:          Development/C
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

BuildRequires:  python-devel
BuildRequires:  mate-file-manager-devel
BuildRequires:  python-module-pygobject-devel
BuildRequires:  gtk-doc
BuildRequires:  autoconf automake libtool
BuildRequires: 	mate-common
BuildRequires: 	python-module-pygtk-devel
BuildRequires: 	python-module-mate-devel

Requires:       mate-file-manager >= 1.1.0

Obsoletes: 		caja-python
Provides:  		python-caja

%description
Python bindings for Caja


%package -n python-module-caja-devel
Summary:        Python bindings for Caja
Group:          Development/C
Requires:       python-module-caja = %{version}-%{release}
Obsoletes: 		caja-python-devel
Provides:  		python-caja-devel

%description -n python-module-caja-devel
Python bindings for Caja


%prep
%setup -q -n %{oldname}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{oldname}/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete

%files
%doc README AUTHORS COPYING NEWS
%{_libdir}/caja/extensions-2.0/libcaja-python.so
%{_libdir}/caja-python/caja.so
%dir %{_datadir}/%{oldname}/extensions

%files -n python-module-caja-devel
%doc README AUTHORS COPYING NEWS
%{_libdir}/pkgconfig/caja-python.pc
%{_datadir}/doc/*

%changelog
* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

