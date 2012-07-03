# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen /usr/bin/pkg-config /usr/bin/splint gcc-c++ pkgconfig(glib-2.0) unzip
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
Name:           libtpcmisc
Version:        1.4.8
Release:        alt2_5
Summary:        Miscellaneous PET functions

License:        LGPLv2+
URL:            http://www.turkupetcentre.net/software/libdoc/%{name}/index.html
Source0:        http://www.turkupetcentre.net/software/libsrc/%{name}_1_4_8_src.zip
Patch0:         %{name}-shared.patch

BuildRequires:  doxygen dos2unix graphviz
Source44: import.info


%description
Former libpet, the common PET C library, has been divided up in 
smaller sub-libraries that each handle a specific task. 
This library includes miscellaneous functions utilized in PET 
data processing.


%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        static
Group: Development/C
Summary:        Static libraries for %{name}

%description	static
This package contains static libraries for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .shared
sed -i "/^CFLAGS/d" Makefile

# Fix encodings and line endings.
dos2unix -k History Readme
iconv -f ISO_8859-1 -t utf8 -o History.new History && mv -f History.new History


%build
# c99 standard since they use declarations in the for loops
export CFLAGS="%{optflags} -std=c99 -fPIC -DPIC -D_POSIX_C_SOURCE=200112L"
export CXXFLAGS="%{optflags} -fPIC -DPIC"
make %{?_smp_mflags}

# Build doxygen documentation
mkdir doc
( cat Doxyfile ; echo "OUTPUT_DIRECTORY=./doc" ) | doxygen -


%install
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}

install -p -m 0755 %{name} -t $RPM_BUILD_ROOT%{_bindir}/
install -p -m 0644 %{name}.a -t $RPM_BUILD_ROOT%{_libdir}/
install -p -m 0755 %{name}.so.0.0.0 -t $RPM_BUILD_ROOT%{_libdir}/
install -p -m 0644 include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}/

pushd $RPM_BUILD_ROOT%{_libdir}/
ln -s %{name}.so.0.0.0 %{name}.so.0
ln -s %{name}.so.0.0.0 %{name}.so
popd

%files
%doc History Readme
%{_bindir}/%{name}
%{_libdir}/%{name}.so.*

%files devel
%doc doc/%{name}/*
%{_libdir}/%{name}.so
%{_includedir}/*

%files static
%{_libdir}/%{name}.a

%changelog
* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.8-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.8-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.8-alt1_4
- initial import by fcimport

