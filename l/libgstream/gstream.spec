# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname gstream
Name:           libgstream
Version:        1.6
Release:        alt2_7
Summary:        Simplified stream output/input for Allegro
Group:          System/Libraries
License:        Giftware
URL:            http://allegro.molhanec.net/gstream.html
Source0:        http://allegro.molhanec.net/gstrm16.zip
BuildRequires:  liballegro-devel texinfo
Source44: import.info
Provides: gstream = %{version}-%{release}

%description
gstream is a C++ add-on library for Allegro. Its main purpose is to provide a
simplified syntax for Allegro's keyboard and text functions for input and
output, so that you can treat a graphical mode as a console.


%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
Requires:       libgstream = %{version}-%{release}
Provides: gstream-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.


%prep
%setup -q -n gstream16
sed -i 's/\r//g' *.h *.cc gstream gmanip README NEWS
touch -r font.dat *.h *.cc gstream gmanip
touch -r gstream._tx README NEWS


%build
make %{?_smp_mflags} -f Makefile.unx MAKEDOC=%{_bindir}/allegro-makedoc \
  OFLAGS="$RPM_OPT_FLAGS -fPIC"
rm test.o
# makefile makes a .a file, make a .so ourselves
g++ -shared -o libgstrm.so.0 -Wl,-soname,libgstrm.so.0 $RPM_OPT_FLAGS *.o `allegro-config --libs`
# generate man-pages too
allegro-makedoc -man foo.3 gstream._tx
sed -i 's/^.BR \(.*\) (3)/.BR gstream-\1 (3)/g' *.3
touch -r gstream._tx *.3 gstream.html gstream.inf


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{oldname}
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -m 755 libgstrm.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libgstrm.so.0 $RPM_BUILD_ROOT%{_libdir}/libgstrm.so
install -p -m 644 gstream.h gstream gmanip.h gmanip \
  $RPM_BUILD_ROOT%{_includedir}/%{oldname}
install -p -m 644 %{oldname}.inf $RPM_BUILD_ROOT%{_infodir}/%{oldname}.info
for i in *.3; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_mandir}/man3/%{oldname}-$i
done
  

%files
%doc README NEWS
%{_libdir}/libgstrm.so.0

%files devel
%doc %{oldname}.html
%{_includedir}/%{oldname}
%{_libdir}/libgstrm.so
%{_infodir}/%{oldname}.info*
%{_mandir}/man3/%{oldname}-*


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_7
- rebuild to get rid of #27020

* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_7
- update to new release by fcimport

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_6
- initial release by fcimport

