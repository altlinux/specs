# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: liblapack-devel perl(Pod/Usage.pm) python3-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name sphinxbase
#comment out if not prerelease
%global prel	5prealpha

%define major	3
%define admajor	3

%define libname		lib%{name}%{major}
%define adlibname	libsphinxad%{admajor}
%define devname		lib%{name}-devel

# rel to bump
%define rel 6

Name:		sphinxbase
Version:	0.9
Release:	alt1_0.0.5prealpha.6.1
Summary:	The CMU Sphinx Recognition System
Group:		System/Libraries
License:	BSD and LGPLv2+
Url:		https://cmusphinx.github.io/
Source0:	http://downloads.sourceforge.net/cmusphinx/%{name}-%{?prel}%{?!prel:%version}.tar.gz
# https://github.com/cmusphinx/sphinxbase/pull/72
Patch0:		sphinxbase-5prealpha-fix-doxy2swig.patch
Patch1:		python3.10.patch
BuildRequires:	bison
BuildRequires:	doxygen
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	libblas-devel
BuildRequires:	swig
BuildRequires:	texlive-dist
# for check
BuildRequires:	locales-fr
Source44: import.info

%description
The CMU Sphinx Recognition System is a library and a set
of examples and utilities for speech recognition.

This package contains the utilities.

%package -n %{libname}
Summary:	Shared components for Sphinx speech recognition
Group:		System/Libraries

%description -n %{libname}
This package contains the shared libraries for Sphinx speech recognition.

%package -n %{adlibname}
Summary:	Shared components for Sphinx speech recognition
Group:		System/Libraries

%description -n %{adlibname}
This package contains the shared libraries for Sphinx speech recognition.

%package -n %{devname}
Summary:	Header files for developing with The CMU Sphinx Recognition System
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{adlibname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the header files and examples for developing with
The CMU Sphinx Recognition System.

%package -n python3-module-sphinxbase
Summary:	Python 3 extension for The CMU Sphinx Recognition System
Group:		Development/Python
%{?python_provide:%python_provide python3-%{name}}

Obsoletes:	python-sphinxbase < 0.9-0.0.5prealpha.3
Provides:	python-sphinxbase = %{version}-%{release}
Obsoletes:	python2-sphinxbase < 0.9-0.0.5prealpha.5

%description -n python3-module-sphinxbase
This package contains the python 3 extension for The CMU Sphinx Recognition
System.

%prep
%setup -qn %{name}-%{?prel}%{?!prel:%version}
%patch0 -p1
%patch1 -p1


%build
autoreconf -vfi
%configure \
	--disable-static \
	--disable-rpath \
	--with-python=%{__python3}
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -delete

# man pages
mkdir -p %{buildroot}%{_mandir}/man1
install -pm644 doc/*.1 %{buildroot}%{_mandir}/man1/

%check
make check

%files
%{_bindir}/sphinx*
%{_mandir}/man1/sphinx*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{adlibname}
%{_libdir}/libsphinxad.so.%{admajor}
%{_libdir}/libsphinxad.so.%{admajor}.*

%files -n python3-module-sphinxbase
%{python3_sitelibdir}/*

%files -n %{devname}
%doc doc/html/
%{_includedir}/%{name}/
%dir %{_datadir}/sphinxbase/
%dir %{_datadir}/sphinxbase/swig/
%{_datadir}/sphinxbase/swig/*.i
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_libdir}/libsphinxad.so


%changelog
* Wed Dec 15 2021 Grigory Ustinov <grenka@altlinux.org> 0.9-alt1_0.0.5prealpha.6.1
- Fixed build with python3.10.

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 0.9-alt1_0.0.5prealpha.6
- new version

* Fri Jan 04 2013 Denis Smirnov <mithraen@altlinux.ru> 0.8-alt1
- 0.8

* Mon Mar 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.4.1-alt2
- Add libsphinxbase and libsphinxbase-devel subpackages (Closes: #13980)

* Tue Feb 24 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Sep 08 2008 Denis Klimov <zver@altlinux.ru> 0.3-alt2
- fix directory ownership violation

* Tue Jan 08 2008 Denis Klimov <zver@altlinux.org> 0.3-alt1
- initial build for ALT Linux
