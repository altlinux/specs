# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%define power64 ppc64
Name:           xalan-c
Version:        1.11.0
Release:        alt1_8
Summary:        Xalan XSLT processor for C

Group:          System/Libraries
License:        ASL 2.0
URL:            http://xml.apache.org/xalan-c/
Source0:        http://www.us.apache.org/dist/xalan/xalan-c/sources/xalan_c-1.11-src.tar.gz
Patch0:         xalan-c-1.10.0-escaping.patch

BuildRequires:  xerces-c-devel
Source44: import.info

%description
Xalan is an XSLT processor for transforming XML documents into HTML, text, or
other XML document types.


%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%package doc
Group:          Documentation
Summary:        Documentation for Xerces-C++ validating XML parser

%description doc
Documentation for %{name}.


%prep
%setup -q -n xalan-c-1.11/c
%patch0 -p2 -b .escaping
find -type d -name CVS -print0 | xargs -0 rm -rf
chmod 644 NOTICE

# Update config.guess for new architectures
# cp /usr/lib/rpm/config.guess config.guess

%build
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
COMMONARGS="-plinux -cgcc -xg++ -minmem"
%ifarch alpha %{power64} s390x sparc64 x86_64 aarch64
./runConfigure ${COMMONARGS} -b64 -P %{_prefix} -C --libdir="%{_libdir}" -z '%{optflags}'
%else
./runConfigure ${COMMONARGS} -b32 -P %{_prefix} -C --libdir="%{_libdir}" -z '%{optflags}'
%endif
# _smp_mflags do not work
make


%install
export XALANCROOT="${PWD}"
export XERCESROOT=%{_includedir}/xercesc/
make install DESTDIR=%{buildroot}


%files
%doc LICENSE KEYS NOTICE
%{_bindir}/Xalan
%{_libdir}/libxalan*.so.*


%files devel
%{_libdir}/libxalan*.so
%{_includedir}/xalanc/


%files doc
%doc readme.html xdocs samples


%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_8
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_7
- new version

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_4
- dependency

