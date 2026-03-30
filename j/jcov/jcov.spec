%define _unpackaged_files_terminate_build 1
%define javaver 21
%def_without check

Name: jcov
Version: 3.0
Release: alt3

Summary: The JCov open source project is used to gather quality metrics associated with the production of test suites
License: GPL-2.0
Group: Development/Java
Url: https://wiki.openjdk.org/display/CodeTools/jcov
Vcs: https://github.com/openjdk/jcov.git

Source0: %name-%version.tar
Patch1: jcov-3.0-alt-change-paths-for-asm-deps.patch
Patch2: jcov-3.0-alt-linux-repair-string-formater.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-java
BuildRequires: ant
BuildRequires: objectweb-asm
BuildRequires: jtharness
BuildRequires: testng
BuildRequires: java-%javaver-openjdk-devel
%if_with check
BuildRequires: beust-jcommander
%endif

%description
%summary.
JCov is being opened in order to facilitate the practice of
verifying test execution of regression tests in OpenJDK development.

%prep
%setup
%autopatch -p1
sed -i "s/^asm\.checksum=.*/asm.checksum=$(sha1sum asm.jar | awk '{print $1}')/" build/build.properties
sed -i "s/^asm\.tree\.checksum=.*/asm.tree.checksum=$(sha1sum asm-tree.jar | awk '{print $1}')/" build/build.properties
sed -i "s/^asm\.util\.checksum=.*/asm.util.checksum=$(sha1sum asm-util.jar | awk '{print $1}')/" build/build.properties

%build
cd build
ant

%install
find JCOV_BUILD/jcov_3.0/ -name "*.jar" \
    -exec install -D -m 0644 -t %buildroot%_javadir/%name/lib {} \;

#Tests require testng with YamlParser
%check
cd build
ant test

%files
%_javadir/jcov
%doc LICENSE examples

%changelog
* Tue Mar 30 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.0-alt3
- Fixed errors with String.formater (Closes: #57226).

* Tue Feb 24 2026 Timofei Fedotov <sovtouch@altlinux.org> 3.0-alt2.694bcdb
- Updated the sources to version 2025.

* Fri Nov 14 2025 Timofei Fedotov <sovtouch@altlinux.org> 3.0-alt1.b07
- Initial build for ALT Sisyphus.
