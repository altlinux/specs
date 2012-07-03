Name: libjogl
Version: 1.1.1
Release: alt8

Summary: java OpenGL library
License: BSD 
Group: Development/Java
Url: https://jogl.dev.java.net/

Packager: Denis Medvedev <nbr@altlinux.ru>

Source: jogl.tar.bz2 
Source1: gluegen.tar.bz2

BuildRequires: rpm-build-java ant-antlr ant-contrib ant-testutil cpptasks libGL-devel libXt-devel libXxf86vm-devel

Conflicts: gluegen

%description
Provides OpenGL bindings for Java
Allows 3d operations with objects
Built from zip package from official site
Includes gluegen


%package manual
Summary: Manual for %name
Group: Documentation

%description manual
Documentation for %name


%package gluegen
Summary: glue generator between c and java code
Group: Development/Java

%description gluegen
Glue generator for java classes and c classes

%prep
%setup -n jogl
cd ..
%setup -T -D -b 1 -n gluegen

# remove all binary libs
cd ..
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.zip" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

cd %_builddir/jogl
%build
export CLASSPATH=$(build-classpath  $_javadir/jre/ext/jogl.jar
 $_javadir/jre/ext/gluegen.jar
 /usr/share/java
 /usr/share/ant/lib/
 /usr/share/ant/lib/ant-antlr.jar
 )

cd %_builddir/gluegen/make
%ant -v -lib /usr/share/java

cd %_builddir/jogl/make


%ifarch i586
%ant -v -lib /usr/share/java -Dgluegen.cpptasks.detected.os=true -DisUnix=true -DisLinux=true  -DisLinuxX86=true -DisX11=true
%endif
%ifarch x86_64
%ant -v -lib /usr/share/java -Dgluegen.cpptasks.detected.os=true -DisUnix=true -DisLinux=true  -DisLinuxAMD64=true -DisX11=true

%endif
%install
# jars
install -d -m 755 %buildroot%_javadir/
install -d -m 755 %buildroot%_libdir/jogl
install -d -m 755 %buildroot%_libdir/
install -m 644 %_builddir/jogl/build/jogl*.jar %buildroot%_javadir/
cp -ar %_builddir/jogl/build/obj/*.so %buildroot%_libdir/

install -d -m 755 %buildroot%_libdir/gluegen/
install -m 644 %_builddir/gluegen/build/gluegen*.jar %buildroot%_javadir/
install -m 644 %_builddir/gluegen/build/obj/*.so %buildroot%_libdir/
install -m 644 %_builddir/gluegen/make/*.xml %buildroot%_libdir/gluegen/
install -d -m 755 %buildroot%_docdir/gluegen/
cp -ar  %_builddir/gluegen/doc/manual %buildroot/%_docdir/gluegen/
%set_verify_elf_method unresolved=relaxed

%files
%_javadir/jogl*
%_libdir/libjogl*

%doc LICENSE.txt 

%files manual
%doc doc

%files gluegen
%_javadir/gluegen*
%_libdir/gluegen/*
%_libdir/libglue*
%doc LICENSE.txt 

%changelog
* Tue Dec 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt8
- fix build

* Thu Nov 25 2010 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt7
- gluegen and jogl are NOT noarch

* Sun Sep 05 2010 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt6
- Add dependence on strict ant-1.7, due to bugs in 1.8

* Thu Jun 25 2009 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt5
- i386- i586

* Thu Jun 25 2009 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt4
- Fixed amd64 build

* Mon Jun 08 2009 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt3
- Only for i586 now

* Sun Jun 07 2009 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt2
- x86_64 linker fix, files/packages cleanup

* Sun May 24 2009 Denis Medvedev <nbr@altlinux.ru> 1.1.1-alt1
- Initial sisyphus pack build


