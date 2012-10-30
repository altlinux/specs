# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname python-module-corba
%define oldname python-corba
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

### Abstract ###

Name: 		python-module-corba
Version: 	1.4.0
Release: 	alt1_1.1.1.1
License: 	LGPLv2+
Group: 		Development/Other
Summary: 	Python bindings for Corba.
URL: 		http://mate-desktop.org
Source0: 	http://pub.mate-desktop.org/releases/1.4/%{oldname}-%{version}.tar.xz

### Dependencies ###

Requires: mate-corba >= 1.0.0
Requires: glib2 >= 2.4.0
Requires: libIDL >= 0.8.0
Requires: python >= 2.3

### Build Dependencies ###

BuildRequires: mate-corba-devel >= 1.0.0
BuildRequires: autoconf
BuildRequires: automake >= 1.6.3-5
BuildRequires: glib2-devel >= 2.4.0
BuildRequires: libIDL-devel >= 0.8.0
BuildRequires: libtool
BuildRequires: pygtk2 >= 2.4.0
BuildRequires: python-devel >= 2.3
BuildRequires: mate-common

Obsoletes: 		pymatecorba
Provides:  		python-corba

%description
pymatecorba is an extension module for python that gives you access
to the ORBit2 CORBA ORB.

%package -n python-module-corba-devel
Summary: Files needed to build wrappers for mate-corba addon libraries.
Group: Development/Other
Requires: python-module-corba = %{version}
Obsoletes: 		pymatecorba-devel
Provides:  		python-corba-devel

%description -n python-module-corba-devel
This package contains files required to build wrappers for mate-corba addon
libraries so that they interoperate with pymatecorba

%prep
%setup -q -n %{oldname}-%{version}

NOCONFIGURE=1 ./autogen.sh

%build

%configure \
	--disable-static

make

%install
make install DESTDIR=$RPM_BUILD_ROOT
#find $RPM_BUILD_ROOT -name "*.la" -exec rm {} \;

%files
%doc AUTHORS NEWS README ChangeLog

%defattr(755, root, root, 755)
%{python_sitelibdir}/*.so
%defattr(644, root, root, 755)
%{python_sitelibdir}/*.py*
%{python_sitelibdir}/MateCORBA.la

%files -n python-module-corba-devel
%defattr(644, root, root, 755)
%{_includedir}/pymatecorba-2
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1.1
- Build for Sisyphus

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Thu Oct 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- 20120622 mate snapshot

* Wed May 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

