# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/doxygen gcc-c++ unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libpgf
Version:        6.11.42
Release:        alt3_2
Summary:        PGF (Progressive Graphics File) library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.libpgf.org
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.zip

BuildRequires:  doxygen
BuildRequires:  libtool
Source44: import.info

%description
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%package        devel
Group: System/Libraries
Summary:        Development files for %{name}
Requires:       libpgf = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}

sed -i 's|$(DESTDIR)$(datadir)/doc/$(DOC_MODULE)|$(RPM_BUILD_DIR)/libpgf|g' doc/Makefile.am


%build
sh autogen.sh

%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING README
%{_libdir}/libpgf.so.4*

%files devel
%doc html
%{_includedir}/%{name}
%{_libdir}/libpgf.so
%{_libdir}/pkgconfig/libpgf.pc
%{_mandir}/man3/*


%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 6.11.42-alt1_1
- initial import by fcimport

