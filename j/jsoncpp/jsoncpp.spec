
Name: jsoncpp
Version: 0.6.0
Release: alt0.1
%define sover 0
%define libname lib%name%sover

Group: System/Libraries
Summary: JSON library implemented in C++
Url: http://sourceforge.net/projects/%name/
License: Public Domain or MIT

Source: %name-src-%version.tar
Source1: jsoncpp.pc

BuildRequires: gcc-c++ python scons doxygen graphviz

%description
%name is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package -n %libname
Summary: JSON library implemented in C++
Group: System/Libraries
%description -n %libname
%name is an implementation of a JSON (http://json.org) reader and writer in
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It is easy for humans to read and write. It is easy for machines to parse and
generate.

%package devel
Summary: Development headers and library for %name
Group: Development/C++
%description devel
This package contains the development headers and library for %name.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
%description doc
This package contains the documentation for %name

%prep
%setup -n %name-src-%version
grep -e "-Wall" SConstruct
sed -i 's/CCFLAGS = "-Wall"/CCFLAGS = "%optflags"/' SConstruct

%build
scons platform=linux-gcc
# make a proper shared lib.
g++ -o libjsoncpp.so.0.0.0 -shared -Wl,-soname,libjsoncpp.so.0 buildscons/linux-gcc-*/src/lib_json/*.os -lpthread
# build docs
python doxybuild.py --with-dot --doxygen %_bindir/doxygen

%install
install -p -D lib%name.so.0.0.0 %buildroot/%_libdir/lib%name.so.0.0.0
ln -s lib%name.so.0.0.0 %buildroot/%_libdir/lib%name.so
ln -s lib%name.so.0.0.0 %buildroot/%_libdir/lib%name.so.0

install -d %buildroot/%_includedir/%name/json
install -p -m 0644 include/json/*.h %buildroot/%_includedir/%name/json
mkdir -p %buildroot/%_docdir/%name/html
for f in AUTHORS LICENSE NEWS.txt README.txt ; do
    install -p -m 0644 $f %buildroot/%_docdir/%name
done
install -p -m 0644 dist/doxygen/*/*.{html,png} %buildroot/%_docdir/%name/html
install -d %buildroot/%_libdir/pkgconfig
install -p -m 0644 %SOURCE1 %buildroot/%_libdir/pkgconfig/
sed -i 's|@@LIBDIR@@|%_libdir|g' %buildroot/%_libdir/pkgconfig/jsoncpp.pc

%files -n %libname
%dir %_docdir/%name/
%doc %_docdir/%name/AUTHORS
%doc %_docdir/%name/LICENSE
%doc %_docdir/%name/*.txt
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*

%files devel
%doc %_docdir/%name/html
%_libdir/lib%name.so
%_includedir/%name/
%_libdir/pkgconfig/jsoncpp.pc

#%files doc
#%_docdir/%name/

%changelog
* Mon Feb 03 2014 Sergey V Turchin <zerg@altlinux.org> 0.6.0-alt0.1
- initial build
