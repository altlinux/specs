Name: javazi
Version: %{get_version tzdata}
%define tzdata_rel %(rpmquery --qf '%%{RELEASE}' tzdata 2>/dev/null | sed 's/^alt//')
Release: alt2.%tzdata_rel

Summary: Timezone data for Java
License: Public Domain
Group: System/Base
Url: https://www.iana.org/time-zones
BuildArch: noarch

Requires: tzdata >= %{get_SVR tzdata}
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
# OpenJDK JDK-8340552: harden TzdbZoneRulesCompiler against missing zone names
Patch3: javazi-1.8-fedora-harden-links.patch
# OpenJDK JDK-8051641: ZoneRulesBuilder last rules fix
Patch4: javazi-1.8-fedora-lastrule-fix.patch

Source3: ZoneTest.java

BuildRequires: hardlink java-devel-default tzdata-source

%description
This package contains timezone information for use by Java runtimes.

%package checkinstall
Summary: Check %name and tzdata compatibility
Group: Other
Requires: %name = %EVR
Requires: tzdata = %{get_SVR tzdata}

%description checkinstall
Check during install that %name and tzdata are compatible with each other.
This package is intended to be used in the install check step of the build
system only.

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

pushd %javazic18
%patch3 -p1
%patch4 -p1
popd

%build
FILES='africa antarctica asia australasia europe northamerica southamerica
pacificnew backward etcetera'

# Java 6/7 tzdata
pushd %javazic16
	javac -source 1.6 -target 1.6 -classpath . $(find -name '*.java')
popd
pushd tzdata
	java -classpath ../%javazic16 alt.tools.javazic.Main \
		-V %version -d javazi $FILES \
		../%javazic16/tzdata_jdk/gmt \
		../%javazic16/tzdata_jdk/jdk11_backward
popd

# Java 8 tzdata
pushd %javazic18
	javac -source 1.8 -target 1.8 -classpath . $(find -name '*.java')
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

%check
# Smoke test: load the freshly built tzdb.dat with the build system JDK.
system_java_home=$(dirname $(readlink -f $(which java)))/..
mkdir -p java_home
cp -Lr $system_java_home/* java_home/.
tzdb_found=$(find java_home -name tzdb.dat | head -1)
[ -n "$tzdb_found" ] || { echo "ERROR: no tzdb.dat found in system JDK"; exit 1; }
for tzdb in $(find java_home -name tzdb.dat) ; do
	rm -f $tzdb
	cp %buildroot%_datadir/javazi-1.8/tzdb.dat $tzdb
done
cp %{SOURCE3} .
javac ZoneTest.java
java_home/bin/java ZoneTest

%files
%_datadir/javazi*/

%files checkinstall

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with the latest tzdata.

* Thu Oct 15 2026 Anton Farygin <rider@altlinux.org> 2026e-alt2
- javazic-1.8: dropped EST/HST/MST alias entries (they are links since
  tzdata 2024b) (Closes: #61080)
- backported fixes from Fedora: JDK-8340552, JDK-8051641
- added %check smoke test for the built tzdb.dat

* Wed Aug 10 2022 Dmitry V. Levin <ldv@altlinux.org> 2024a-alt1
- Rebuilt with the latest tzdata.

* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 2021a-alt1.1
- java 11 migration: java-devel-default moves to java 11,
  -source 1.5 -target 1.5 no more supported

* Wed Apr 04 2018 Dmitry V. Levin <ldv@altlinux.org> %{get_SVR tzdata}
- Rebuilt with new tzdata.

* Wed Apr 04 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt3
- Relaxed dependency on tzdata.
- Added checkinstall subpackage.

* Wed Apr 04 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt2
- Packaged javazi for OpenJDK {6,7,8}.

* Tue Feb 20 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt1
- Bootstrap.
