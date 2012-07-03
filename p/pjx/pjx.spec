Name: pjx
Version: 1.4.0
Release: alt1jpp5.1

Summary: PJX is a general purpose PDF programming library for Java
License: GPL
Group: Development/Java
Packager: Eugeny A. Rostovtsev (REAL) <real@altlinux.org>

Url: http://sourceforge.net/projects/pjx/
Source: http://downloads.sourceforge.net/pjx/pjx-1.4.0.tar.gz

BuildRequires(pre): rpm-build-java jpackage-utils
BuildPreReq: java-devel-default ant
BuildArch: noarch

# Automatically added by buildreq on Wed Jan 07 2009
BuildRequires: texlive-latex-base tzdata

%description
PJX is a general purpose PDF programming library for Java; with support for
reading, combining, manipulating, and writing PDF documents.

%package doc
Summary: Documentation for pjx
Group: Development/Java
Requires: %name = %version-%release
BuildArch: noarch

%description doc
Documentation for pjx.

%package javadoc
Summary: Javadoc for pjx
Group: Development/Java
Requires: %name = %version-%release
BuildArch: noarch

%description javadoc
Javadoc for pjx.

%prep
%setup -n %name-%version

%build
cd src
%__sed -i \
	-e 's/enum/_enum/g' \
	com/etymon/pj/object/PjInfo.java
%__sed -i \
	-e 's/enum/_enum/g' \
	-e 's/_enumb/enumb/g' \
	com/etymon/pj/object/PjDictionary.java
%javac `find ./ -type f -name '*.java'`
%jar cvf pjx.jar `find ./ -type f -name '*.class'`
mkdir -pv javadoc
pkglist=`find com -type d|sed 's/\//./g'`
cd javadoc
%javadoc -private -sourcepath .. -overview ../overview.html \
	-use -splitIndex $pkglist
cd ../../doc
%make
cd ..

%install
mkdir -pv %buildroot%_docdir/%name
mv doc/%name.pdf %buildroot%_docdir/%name
mkdir -pv %buildroot%_javadir/%name
mv src/*.jar %buildroot%_javadir/%name/
mkdir -pv %buildroot%_javadocdir/%name
mv src/javadoc/* %buildroot%_javadocdir/%name/
curdir=`pwd`
cd %buildroot%_javadir
ln -s %name/%name.jar %name.jar
cd $curdir

%files
%doc COPYING README VERSION
%_javadir/%name.jar
%_javadir/%name

# doc in pdf
%files doc
%_docdir/%name

%files javadoc
%_javadocdir/%name

%changelog
* Mon Dec 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1jpp5.1
- Rebuilt with texlive instead of tetex

* Wed Jan 07 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.4.0-alt1jpp5
- Initial build for Sisyphus
