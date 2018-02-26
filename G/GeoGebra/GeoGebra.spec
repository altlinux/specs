Name: GeoGebra 
Version: 4.0 
Release: alt5.beta1
Packager: Denis Medvedev <nbr@altlinux.org>

Summary: GeoGebra is a visual geometry/algebra system
License: GPLv2+
Group: Education 
Url: http://geogebra.sf.net

Source: %name-%version.tar.gz

# Common dependencies
BuildPreReq: /proc rpm-build-java jpackage-utils libjogl eclipse
BuildRequires: java-devel-default libjogl

# if ant is used for build
BuildRequires: ant junit
Requires: java-common
Requires: libjogl
Requires: libjogl-gluegen


BuildArch: noarch

%description
A program that allow you to solve geometry tasks by drawing it or  in algebraic form.


Group: Education 



%prep

%setup


%build
export CLASSPATH=$(build-classpath junit example-javalib)
cd geogebra
%ant build-project
%ant -f build-jars.xml geogebra
mkdir geogebra-%version
rm -rf ../build/packed
rm -rf ../build/unpacked
rm -rf ../build/unsigned
cp  ../build/* geogebra-%version

%ant -f build-jars.xml geogebra3D
mkdir geogebra3D-%version
rm -rf ../build/packed
rm -rf ../build/unpacked
rm -rf ../build/unsigned
cp  ../build/* geogebra3D-%version

%install
# jars
install -d -m 755 %buildroot%_javadir

install -d -m 755 %buildroot%_javadir/GeoGebra
install -m 644 geogebra/geogebra-%version/* %buildroot%_javadir/GeoGebra
install -d -m 755 %buildroot%_javadir/GeoGebra3D
install -m 644 geogebra/geogebra3D-%version/* %buildroot%_javadir/GeoGebra3D
mkdir -p %buildroot%_bindir
install -m 644 geogebra/geogebra.sh %buildroot%_bindir/geogebra
install -m 644 geogebra/geogebra3D.sh %buildroot%_bindir/geogebra3D
mkdir -p %buildroot%_desktopdir
install -m 622 geogebra/geogebra.desktop %buildroot%_desktopdir 
install -m 622 geogebra/geogebra3D.desktop %buildroot%_desktopdir 

chmod +x %buildroot%_bindir/geogebra
chmod +x %buildroot%_bindir/geogebra3D
mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir

install -m 622 geogebra16.png %buildroot%_miconsdir/geogebra.png
install -m 622 geogebra48.png %buildroot%_liconsdir/geogebra.png
install -m 622 geogebra32.png %buildroot%_niconsdir/geogebra.png

%files
%doc README.txt RELEASE-NOTES.txt LICENSE.txt LICENSE-NOTES.alt
%_javadir/*
%_bindir/geogebra*
%_miconsdir/geogebra.png
%_liconsdir/geogebra.png
%_niconsdir/geogebra.png
%_desktopdir/geogebra*.desktop

%changelog
* Tue Nov 23 2010 Denis Medvedev <nbr@altlinux.ru> 4.0-alt5.beta1
- Dependencies fixed, icons fix 

* Mon Nov 22 2010 Denis Medvedev <nbr@altlinux.ru> 4.0-alt4.beta1
- dependencies fix

* Mon Nov 22 2010 Denis Medvedev <nbr@altlinux.ru> 4.0-alt3.beta1
- Fixed dependency to libjogl-gluegen, added icons

* Fri Nov 19 2010 Denis Medvedev <nbr@altlinux.ru> 4.0-alt2.beta1
- added missing dependency to gluegen

* Sat Sep 05 2009 Denis Medvedev <nbr@altlinux.org> 4.0-alt1.beta1
- Initial Sisyphus build, GPLv2 code only


