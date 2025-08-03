%define _unpackaged_files_terminate_build 1

Name: asm
Version: 9.8
Release: alt1

Summary: Java bytecode manipulation and analysis framework
License: Apache-2.0
Group: Development/Java
Url: https://asm.ow2.io
Vcs: https://gitlab.ow2.org/asm/asm.git
ExcludeArch: i586

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: install_jars.sh
Source3: install_poms.sh
Patch0: 0001-Disable-signing-with-key.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: gradle

%description
ASM is an all purpose Java bytecode manipulation and analysis framework. It can
be used to modify existing classes or to dynamically generate classes, directly
in binary form. ASM provides some common bytecode transformations and analysis
algorithms from which custom complex transformations and code analysis tools
can be built. ASM offers similar functionality as other Java bytecode
frameworks, but is focused on performance. Because it was designed and
implemented to be as small and as fast as possible, it is well suited for use
in dynamic systems (but can of course be used in a static way too, e.g. in
compilers).

%prep
%setup
%autopatch -p1

test -d ~/.gradle && rm -rf ~/.gradle
tar xf %SOURCE1 -C ~

cp %SOURCE2 .
chmod +x install_jars.sh

cp %SOURCE3 .
chmod +x install_poms.sh

%build
gradle publishToMavenLocal -Prelease=true

%install
./install_jars.sh %buildroot%_javadir/asm
./install_poms.sh ~/.m2 %buildroot%_datadir/maven-poms/asm

%check
gradle check

%files
%_javadir/asm/
%_datadir/maven-poms/asm/

%changelog
* Sun Aug 03 2025 Ivan Khanas <xeno@altlinux.org> 9.8-alt1
- First build for ALT.
