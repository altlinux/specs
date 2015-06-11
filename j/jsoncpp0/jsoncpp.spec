
Name: jsoncpp0
Version: 0.6.0
Release: alt1
%define rname jsoncpp
%define sover 0
%define libname lib%rname%sover

Group: System/Libraries
Summary: JSON library implemented in C++
Url: http://sourceforge.net/projects/%rname/
License: Public Domain or MIT

Source: %rname-src-%version.tar
Source1: jsoncpp.pc

BuildRequires: gcc-c++ python scons doxygen graphviz

%description
%rname is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package -n %libname
Summary: JSON library implemented in C++
Group: System/Libraries
%description -n %libname
%rname is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package devel
Summary: Development headers and library for %rname
Group: Development/C++
%description devel
This package contains the development headers and library for %rname.

%package doc
Summary: Documentation for %rname
Group: Documentation
BuildArch: noarch
%description doc
This package contains the documentation for %rname

%prep
%setup -n %rname-src-%version
grep -e "-Wall" SConstruct
sed -i 's/CCFLAGS = "-Wall"/CCFLAGS = "%optflags"/' SConstruct

%build
scons platform=linux-gcc
# make a proper shared lib.
g++ -o libjsoncpp.so.0.0.0 -shared -Wl,-soname,libjsoncpp.so.0 buildscons/linux-gcc-*/src/lib_json/*.os -lpthread
# build docs
#python doxybuild.py --with-dot --doxygen %_bindir/doxygen

%install
install -p -D lib%rname.so.0.0.0 %buildroot/%_libdir/lib%rname.so.0.0.0
ln -s lib%rname.so.0.0.0 %buildroot/%_libdir/lib%rname.so
ln -s lib%rname.so.0.0.0 %buildroot/%_libdir/lib%rname.so.0

#install -d %buildroot/%_includedir/%rname/json
#install -p -m 0644 include/json/*.h %buildroot/%_includedir/%rname/json
#mkdir -p %buildroot/%_docdir/%rname/html
#for f in AUTHORS LICENSE NEWS.txt README.txt ; do
#    install -p -m 0644 $f %buildroot/%_docdir/%rname
#done
#install -p -m 0644 dist/doxygen/*/*.{html,png} %buildroot/%_docdir/%rname/html
#install -d %buildroot/%_libdir/pkgconfig
#install -p -m 0644 %SOURCE1 %buildroot/%_libdir/pkgconfig/
#sed -i 's|@@LIBDIR@@|%_libdir|g' %buildroot/%_libdir/pkgconfig/jsoncpp.pc

%files -n %libname
%doc AUTHORS LICENSE
%_libdir/lib%rname.so.%sover
%_libdir/lib%rname.so.%sover.*

#%files devel
#%doc %_docdir/%rname/html
#%_libdir/lib%rname.so
#%_includedir/%rname/
#%_libdir/pkgconfig/jsoncpp.pc

#%files doc
#%_docdir/%rname/

%changelog
* Thu Jun 11 2015 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt1
- build compat library

* Thu Jun 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6.0-alt0.1.1
- rebuild with c++11 ABI

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt0.0.M70P.2
- built for M70P

* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt0.1
- initial build
