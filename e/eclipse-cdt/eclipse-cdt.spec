# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
%global debug_package %{nil}

Epoch: 1

%define major                   8
%define minor                   1       
%define majmin                  %{major}.%{minor}
%define micro                   2
%define eclipse_base            %{_libdir}/eclipse
%define cdt_snapshot		org.eclipse.cdt-CDT_8_1_2
%define build_id		201302132326	
%define libhover_build_id	201302051708
%define pdebuild		eclipse-pdebuild 

# All arches line up except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%ifarch %{arm}
%define eclipse_arch    arm
%else
%define eclipse_arch   %{_arch}
%endif
%endif

Summary:        Eclipse C/C++ Development Tools (CDT) plugin
Name:           eclipse-cdt
Version:        %{majmin}.%{micro}
Release:        alt2_1jpp7
License:        EPL and CPL
Group:          Development/Java
URL:            http://www.eclipse.org/cdt
Requires:       eclipse-platform


# The following tarball was fetched via:
# http://git.eclipse.org/c/cdt/org.eclipse.cdt.git/snapshot/org.eclipse.cdt-CDT_8_1_2.tar.bz2
Source0: %{cdt_snapshot}.tar.bz2

Source2: http://download.eclipse.org/linuxtools/1.2.1-sources/linuxtools-libhover-parent-1.2.1-src.tar.bz2

# Script to run the tests in Xvnc
Source5: %{name}-runtests.sh

# Libhover docs to place locally
Source7: libstdc++-v3.libhover

Patch0: %{name}-tycho-build.patch

# Following are patches to build libhover libstdcxx plug-in and to supply
# binary libhover data directly in the plug-in itself.
Patch1: %{name}-libhover-local-libstdcxx.patch
Patch2: %{name}-libhover-libstdcxx.patch

BuildRequires: tycho
BuildRequires: tycho-extras
BuildRequires: eclipse-pde >= 1:3.8.0
BuildRequires: eclipse-rse >= 3.3
BuildRequires: maven-local maven >= 3.0.3
BuildRequires: lpg-java-compat
BuildRequires: eclipse-platform >= 1:3.8.0

Requires:       gdb make gcc-c++ autoconf automake libtool
Requires:       eclipse-platform >= 1:3.8.0
Requires:	eclipse-rse >= 3.3

%if 0%{?rhel} >= 6
ExclusiveArch: %{ix86} x86_64
%else
ExclusiveArch: %{ix86} x86_64 ppc ia64 ppc64 %{arm} s390 s390x
%endif
Source44: import.info
%define java_bin %_jvmdir/java/bin

%description
Eclipse features and plugins that are useful for C and C++ development.

%package parsers
Summary:        Eclipse C/C++ Development Tools (CDT) Optional Parsers
Group:          Editors
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       lpg-java-compat

%description parsers
Optional language-variant parsers for the CDT.

%package sdk
Summary:        Eclipse C/C++ Development Tools (CDT) SDK plugin
Group:          Editors
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description sdk
Source for Eclipse CDT for use within Eclipse.

%prep
%setup -q -c 

pushd %{cdt_snapshot}
%patch0 -p1
sed -i -e 's/<arch>x86<\/arch>/<arch>%{eclipse_arch}<\/arch>/g' pom.xml
# Add secondary arch support if we are building there
%ifarch %{arm} s390 s390x
pushd core
cp -r org.eclipse.cdt.core.linux.x86 org.eclipse.cdt.core.linux.%{eclipse_arch}
pushd org.eclipse.cdt.core.linux
sed -i -e 's/<arch>x86<\/arch>/<arch>%{eclipse_arch}<\/arch>/g' pom.xml
popd
pushd org.eclipse.cdt.core.linux.%{eclipse_arch}
sed -i -e 's/x86/%{eclipse_arch}/g' pom.xml
pushd META-INF
sed -i -e 's/x86/%{eclipse_arch}/g' MANIFEST.MF
popd
pushd os/linux
mv x86 %{eclipse_arch}
popd
popd
popd
pushd releng/org.eclipse.cdt.platform-feature
sed -i -e 's/"org.eclipse.cdt.core.linux.x86"/"org.eclipse.cdt.core.linux.%{eclipse_arch}"/g' feature.xml
sed -i -e 's/arch="x86"/arch="%{eclipse_arch}"/' feature.xml
popd
sed -i -e"/<module>core\/org.eclipse.cdt.core.linux<\/module>/ a\ \t\t<module>core\/org.eclipse.cdt.core.linux.%{eclipse_arch}<\/module>" pom.xml
%endif
# Force the linux arch-specific plug-in to be a dir so that the .so files aren't loaded into
# the user.home .eclipse configuration
pushd core
pushd org.eclipse.cdt.core.linux.%{eclipse_arch}
sed -i -e"/Bundle-Localization: plugin/ aEclipse-BundleShape: dir" META-INF/MANIFEST.MF
popd
popd
popd

## Libhover stuff
tar -xaf %{SOURCE2}
pushd linuxtools-libhover-parent-1.2.1-src
# newlib libhover is an optional feature...remove it from CDT base
rm -rf org.eclipse.linuxtools.cdt.libhover.newlib
rm -rf org.eclipse.linuxtools.cdt.libhover.newlib-feature
%patch1 -p0
%patch2 -p0
pushd org.eclipse.linuxtools.cdt.libhover.libstdcxx
mkdir data
pushd data
cp %{SOURCE7} .
popd
popd
popd

%build
export JAVA_HOME=%{java_home}

# Exclude EquinoxResolver to avoid NPE occuring on arm
%ifarch %{arm}
export MAVEN_OPTS="-XX:CompileCommand=exclude,org/eclipse/tycho/core/osgitools/EquinoxResolver,newState"
%endif

# See comments in the script to understand this.
/bin/sh -x %{eclipse_base}/buildscripts/copy-platform SDK \
  %{eclipse_base} xmlrpc codec httpclient lang rse
SDK=$(cd SDK >/dev/null && pwd)

pushd %{cdt_snapshot}
sed -i -e "s:/builddir/build/BUILD/myrepo:$repodir:g" pom.xml
popd

mkdir home
homedir=$(cd home > /dev/null && pwd)

pushd %{cdt_snapshot}
pushd core/org.eclipse.cdt.core.linux/library
make JAVA_HOME="%{java_home}" ARCH=%{eclipse_arch} CC='gcc -D_GNU_SOURCE'
popd

mvn-rpmbuild -o -DskipTychoVersionCheck -Dmaven.test.skip=true -Dtycho.local.keepTarget -DforceContextQualifier=%{build_id} -fae clean install

## Libhover has dependencies on CDT so we must add these to the SDK directory
unzip -o releng/org.eclipse.cdt.repo/target/org.eclipse.cdt.repo-8.1.1-SNAPSHOT.zip -d $SDK
popd

## Libhover build
pushd linuxtools-libhover-parent-1.2.1-src
%{pdebuild} -f org.eclipse.linuxtools.cdt.libhover.feature  -a "-DbaseLocation=$SDK -DforceContextQualifier=%{libhover_build_id}"
%{pdebuild} -f org.eclipse.linuxtools.cdt.libhover.devhelp.feature  \
-a "-DbaseLocation=$SDK -DjavacSource=1.6 -DjavacTarget=1.6 \
-DforceContextQualifier=%{libhover_build_id}"
popd

%install
# Eclipse may try to write to the home directory.
mkdir -p home
homedir=$(cd home > /dev/null && pwd)

installDir=${RPM_BUILD_ROOT}/%{eclipse_base}/dropins/cdt
parsersInstallDir=${installDir}-parsers
sdkInstallDir=${installDir}-sdk
install -d -m755 $installDir
install -d -m755 $parsersInstallDir
install -d -m755 $sdkInstallDir

# Unzip contents of the cdt repo, removing all but plugins and features
unzip -q -o %{cdt_snapshot}/releng/org.eclipse.cdt.repo/target/org.eclipse.cdt.repo-8.1.1-SNAPSHOT.zip \
-d $installDir/eclipse

# Unpack all existing feature jars
for x in $installDir/eclipse/features/*.jar; do
  dirname=`echo $x | sed -e 's:\\(.*\\)\\.jar:\\1:g'`
  mkdir -p $dirname
  unzip -q $x -d $dirname
  rm $x
done 

# Add CDT core tests plugin even though this isn't done upstream
cp %{cdt_snapshot}/core/org.eclipse.cdt.core.tests/target/org.eclipse.cdt.core.tests-*-SNAPSHOT.jar $installDir/eclipse/plugins

# Libhover install
pushd linuxtools-libhover-parent-1.2.1-src
unzip -qq -d $installDir build/rpmBuild/org.eclipse.linuxtools.cdt.libhover.feature.zip
unzip -qq -d $installDir build/rpmBuild/org.eclipse.linuxtools.cdt.libhover.devhelp.feature.zip
popd

# Remove lpgjavaruntime jar file
rm -rf $installDir/eclipse/plugins/net.sourceforge.*

# Move upc, xlc, and lrparser plugins/features to parsers install area.
mkdir -p $parsersInstallDir/eclipse/features $parsersInstallDir/eclipse/plugins
mv $installDir/eclipse/features/*xlc* $parsersInstallDir/eclipse/features
mv $installDir/eclipse/plugins/*xlc* $parsersInstallDir/eclipse/plugins
mv $installDir/eclipse/features/*lrparser* $parsersInstallDir/eclipse/features
mv $installDir/eclipse/plugins/*lrparser* $parsersInstallDir/eclipse/plugins
mv $installDir/eclipse/features/*upc* $parsersInstallDir/eclipse/features
mv $installDir/eclipse/plugins/*upc* $parsersInstallDir/eclipse/plugins
pushd $parsersInstallDir/eclipse/plugins
ln -s ../../../../../../share/java/lpgjavaruntime.jar net.sourceforge.lpg.lpgjavaruntime_1.1.0.jar
popd

mkdir -p $sdkInstallDir/eclipse/features $sdkInstallDir/eclipse/plugins
mv $installDir/eclipse/features/*source* $sdkInstallDir/eclipse/features
mv $installDir/eclipse/plugins/*source* $sdkInstallDir/eclipse/plugins
mv $installDir/eclipse/plugins/org.eclipse.cdt.doc.isv_* $sdkInstallDir/eclipse/plugins
mv $installDir/eclipse/features/*sdk* $sdkInstallDir/eclipse/features
mv $installDir/eclipse/plugins/*sdk* $sdkInstallDir/eclipse/plugins

rm -rf $installDir/eclipse/features/org.eclipse.cdt.master_*
rm -rf $installDir/eclipse/plugins/org.eclipse.ant.optional.junit_*
rm -rf $installDir/eclipse/plugins/org.eclipse.test_*

# remove repo stuff that shouldn't be in dropins folder
rm -rf $installDir/eclipse/artifacts.jar
rm -rf $installDir/eclipse/content.jar
rm -rf $installDir/eclipse/binary

%files
%{eclipse_base}/dropins/cdt
%doc %{cdt_snapshot}/releng/org.eclipse.cdt.releng/epl-v10.html
%doc %{cdt_snapshot}/releng/org.eclipse.cdt.releng/notice.html

%files sdk
%{eclipse_base}/dropins/cdt-sdk
%doc %{cdt_snapshot}/releng/org.eclipse.cdt.releng/epl-v10.html
%doc %{cdt_snapshot}/releng/org.eclipse.cdt.releng/notice.html

%files parsers
%{eclipse_base}/dropins/cdt-parsers
%doc %{cdt_snapshot}/releng/org.eclipse.cdt.releng/epl-v10.html
%doc %{cdt_snapshot}/releng/org.eclipse.cdt.releng/notice.html

%changelog
* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:8.1.2-alt2_1jpp7
- rebuild with maven-local

* Tue Jul 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:8.1.2-alt1_1jpp7
- update

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1:8.0.0-alt1_5jpp6
- update to new release by jppimport

* Wed Mar 02 2011 Igor Vlasenko <viy@altlinux.ru> 1:7.0.1-alt1_5jpp6
- new version

* Thu Dec 02 2010 Igor Vlasenko <viy@altlinux.ru> 1:6.0.2-alt1_5jpp6
- new version

* Thu Feb 04 2010 Igor Vlasenko <viy@altlinux.ru> 1:6.0.0-alt1_10jpp6
- build for new eclipse version

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.0.1-alt1_1jpp6
- eclipse 3.4.1 build

* Sun Jul 27 2008 Igor Vlasenko <viy@altlinux.ru> 1:4.0.3-alt1_1jpp6
- new version

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_1jpp5.0
- converted from JPackage by jppimport script

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Sun Jan 08 2006 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.1-alt1
- 3.0.1

* Fri Aug 19 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.0-alt1
- 3.0.0 release

* Wed Aug 10 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.0-alt0.1.RC3
- RC3

* Tue Aug 02 2005 Mikhail Zabaluev <mhz@altlinux.ru> 3.0.0-alt0.1.RC2
- Updated to 3.0.0RC2
- Steps to support non-x86 architectures, chiefly x86_64

* Thu Jan 13 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.1.0-alt1
- First release for Sisyphus
