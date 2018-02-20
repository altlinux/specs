Name: javazi
Version: %{get_version tzdata}
Release: %{get_release tzdata}

Summary: Timezone data for Java
License: Public Domain
Group: System/Base
Url: https://www.iana.org/time-zones
BuildArch: noarch

Requires: tzdata = %{get_SVR tzdata}
Provides: tzdata-java = %EVR
Obsoletes: tzdata-java < %EVR

%define javazic16 javazic-1.6.0
# https://icedtea.classpath.org/
# javazic source codes comes from openjdk-1.6.0 source archive
Source1: %javazic16.tar

%define javazic18 javazic-1.8-37392f2f5d59
# https://omajid.fedorapeople.org/%javazic18.tar.xz
Source2: %javazic18.tar

Patch1: javazic-fixup.patch
Patch2: javazic-exclusion-fix.patch

BuildRequires: hardlink java-devel-default tzdata-source

%description
This package contains timezone information for use by Java runtimes.

%prep
%setup -cT -a1 -a2
cp -a %_usrsrc/tzdata .

pushd %javazic16
%patch1 -p0
%patch2 -p0
	# A hack: sun.tools may be defined and installed in the JVM.
	# In order to guarantee that we are using IcedTea/OpenJDK
	# for creating the zoneinfo files, rebase all the package
	# from "sun." to "alt.".
	mv sun alt
	find alt -type f -name '*.java' -print0 |
		xargs -0 -- sed -ri 's/sun(\.(tools|util)\.)/alt\1/g'
popd

%build
FILES='africa antarctica asia australasia europe northamerica southamerica
pacificnew backward etcetera'

# Java 6/7 tzdata
pushd %javazic16
	javac -source 1.5 -target 1.5 -classpath . $(find -name '*.java')
popd
pushd tzdata
	java -classpath ../%javazic16 alt.tools.javazic.Main \
		-V %version -d javazi $FILES \
		../%javazic16/tzdata_jdk/gmt \
		../%javazic16/tzdata_jdk/jdk11_backward
popd

# Java 8 tzdata
pushd %javazic18
	javac -source 1.7 -target 1.7 -classpath . $(find -name '*.java')
popd
pushd tzdata
	java -classpath ../%javazic18 build.tools.tzdb.TzdbZoneRulesCompiler \
		-srcdir . -dstfile tzdb.dat -verbose $FILES \
		../%javazic18/tzdata_jdk/gmt \
		../%javazic18/tzdata_jdk/jdk11_backward
popd

%install
mkdir -p %buildroot%_datadir/javazi-1.8
cp -a tzdata/javazi %buildroot%_datadir/
install -pm644 tzdata/tzdb.dat %buildroot%_datadir/javazi-1.8/

# Hardlink identical files together.
%define __spec_install_custom_post hardlink -vc %buildroot

%files
%_datadir/javazi*/

%changelog
* Tue Feb 20 2018 Dmitry V. Levin <ldv@altlinux.org> %{get_SVR tzdata}
- Packaged javazi for OpenJDK {6,7,8}.

* Tue Feb 20 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt1
- Bootstrap.
