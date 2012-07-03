BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-xerces-c
Version:        3.1.1
Release:        alt1_1
Summary:        MingGW Windows validating XML parser

Group:          System/Libraries
License:        ASL 2.0
URL:            http://xml.apache.org/xerces-c/
Source0:        http://www.apache.org/dist/xerces/c/3/sources/xerces-c-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 53
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

Requires:       pkgconfig
Source44: import.info

%description
Xerces-C is a validating XML parser written in a portable subset of
C++. Xerces-C makes it easy to give your application the ability to
read and write XML data. A shared library is provided for parsing,
generating, manipulating, and validating XML documents. Xerces-C is
faithful to the XML 1.0 recommendation and associated standards (DOM
1.0, DOM 2.0. SAX 1.0, SAX 2.0, Namespaces).




%prep
%setup -q -n xerces-c-%{version}


%build
%{_mingw32_configure} LDFLAGS=-no-undefined \
    --disable-static \
    --disable-pretty-make
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mingw32_bindir}/*.exe


%files
%doc LICENSE
%{_mingw32_includedir}/xercesc/
%{_mingw32_bindir}/libxerces-c-3-1.dll
%{_mingw32_libdir}/libxerces-c.dll.a
%{_mingw32_libdir}/libxerces-c.la
%{_mingw32_libdir}/pkgconfig/xerces-c.pc


%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_1
- initial release by fcimport

