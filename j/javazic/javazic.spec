Name: javazic
Version: 1.6.0
Release: alt1

Summary: A time zone compiler for Java
License: GPLv2 with classpath exception
Group: Development/Java
Url: http://icedtea.classpath.org/
BuildArch: noarch

# javazic source codes comes from openjdk-1.6.0 source archive
Source: %name-%version.tar

Patch1: javazic-fixup.patch
Patch2: javazic-exclusion-fix.patch

BuildRequires: gcc-java

%description
This is a time zone compiler for opensource Java Virtual Machine
derived from openjdk6 source code.

%prep
%setup
%patch1 -p0
%patch2 -p0

# A hack: sun.tools may be defined and installed in the JVM.
# In order to guarantee that we are using IcedTea/OpenJDK
# for creating the zoneinfo files, rebase all the package
# from "sun." to "alt.".
mv sun alt
find alt -type f -name '*.java' -print0 |
	xargs -0 -- sed -ri 's/sun(\.(tools|util)\.)/alt\1/g'

%build
gcj -C $(find alt -name \*.java)
echo 'Main-Class: alt.tools.javazic.Main' > manifest.txt
fastjar -cfm %name.jar manifest.txt $(find . -iname '*.class')

%install
mkdir -p %buildroot%_datadir/{java,%name}
cp -a tzdata_jdk %buildroot%_datadir/%name/
install -pm644 %name.jar %buildroot%_datadir/java/

%files
%_datadir/%name/
%_datadir/java/%name.jar

%changelog
* Sat Oct 27 2012 Dmitry V. Levin <ldv@altlinux.org> 1.6.0-alt1
- Packaged javazic separately from tzdata.
