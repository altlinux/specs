Name: flexdock
Version: 0.5.1
Release: alt4
Summary: Docking framework for Java Swing GUI apps

Group: Development/Java

#Licence is MIT on their website
License: MIT
Url: https://flexdock.dev.java.net/

Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version-clean.tar.gz

# Original Source# Contains code that we cannot ship.
# Download the upstream tarball and invoke this script while in the
# tarball's directory
Source1: %name-generate-tarball.sh

# This patch is fedora specific -- System.loadLibrary fix to help locate JNI components
Patch: flexdock-jni.patch
#Removes the java media framework from the demos to satisfy reqs
Patch1: flexdock-nojmf.patch
#Modifies the build process  -- fedora specific
Patch2: flexdock-build.patch
#Fixes the skinlf search paths in the skinlf.jar (1 of 2)
Patch3: flexdock-skinlfTitlebarui-path.patch
#Fixes the skinlf search paths in the skinlf.jar (2 of 2)
Patch4: flexdock-skinlfPainter-path.patch

BuildRequires(pre): rpm-build-java
BuildRequires: ant
BuildRequires: ant-apache-regexp
BuildRequires: ant-commons-logging
BuildRequires: java-devel
BuildRequires: jgoodies-looks
BuildRequires: jpackage-utils
BuildRequires: libX11-devel
BuildRequires: skinlf

%description
FlexDock is a Java docking framework for use in cross-platform
Swing applications.

%prep
%setup -qc

#Modify the jni dir that is hardcoded in the patch
cp -pf %PATCH0 %PATCH0.tmp
sed -i 's!@@libdir_name@@!%_libdir/%name/!' %PATCH0
#Apply patches
%patch0
%patch1
%patch2
%patch3
%patch4

#restore patch0
mv %PATCH0.tmp %PATCH0

#Override the build file's default hard-coded paths
echo "sdk.home=%_jvmdir/java" > workingcopy.properties

#remove *dll
find ./ -name \*.dll -exec rm  {} \;
#remove .so files
find ./ -name \*.so -exec rm {} \;

#JAR "dependency" handling
#==========
#delete and symlink any jar files we know about

#rm commands commented out, as we delete these
#at repackage time

# Apache commons Logging component
# http://commons.apache.org/logging/
#rm -f lib/commons-logging-1.1.jar

#remove jmf, as it is only used in a demo,
#which is unused after patching
#rm -rf lib/jmf

#" Looks" project
# https://looks.dev.java.net/
#rm -f lib/looks-2.1.1.jar

#skinlf "Skin look and Feel" project
# https://skinlf.dev.java.net/
#rm -f lib/skinlf.jar

build-jar-repository -s -p lib commons-logging skinlf jgoodies-looks.jar

pushd lib
ln -s jgoodies-looks.jar looks-2.2.1.jar
ln -s commons-logging.jar commons-logging-1.1.jar
popd

JAR_files=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
	JAR_files="$JAR_files $j"
	fi
done

if [ ! -z "$JAR_files" ] ; then
	echo "These JAR files should be deleted and symlinked to system JAR files: $JAR_files"
	exit 1
fi
#=========

#Endline convert Doc files
for i in "README-RELEASE LICENSE.txt README release-notes.txt" ;
do
	sed -i 's/\r//' $i
done

%build
export CLASSPATH=$(build-classpath jgoodies-looks skinlf)
ant -v -Dbuild.sysclasspath=first build.with.native jar
ant -v -Dbuild.sysclasspath=first compile.native

%install


#Create dirs needed.
mkdir -p %buildroot/%_libdir/%name
mkdir -p %buildroot/%_javadir

#flexdock has funny arch flags, such as "libRubberBand-linux-x86.so" on i386
SOFILE=`find ./ -name libRubberBand*so`

install -pm755 $SOFILE %buildroot/%_libdir/%name/libRubberBand-0.so
#install jar file into lib dir as it is a JNI requiring jar
install -pm644 build/%name-%version.jar %buildroot/%_javadir/%name-%version.jar

pushd .
cd %buildroot/%_javadir
ln -s %name-%version.jar %name.jar
popd


%files
%doc LICENSE.txt README README-RELEASE release-notes.txt
%_libdir/%name
%_javadir/*

%changelog
* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt4
- resurrect

* Thu Aug 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt3
- Fix creation %%_libdir/%%name in working dir (ALT #21138)

* Mon Jul 20 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt2
- Move jar to %%_javadir

* Thu Jul 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1
- Initial from Fedora
