%define _unpackaged_files_terminate_build 1

Name: mx
Version: 7.88.2
Release: alt1

Summary: Command-line build tool for Graal suites
License: GPL-2.0-only
Group: Development/Other
URL: https://github.com/graalvm/mx
VCS: https://github.com/graalvm/mx.git

Source0: %name-%version.tar
Source1: mx-launcher
Patch0: mx-linux-x86.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: java-21-openjdk-devel
BuildRequires: git-core
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-deploy-plugin)
BuildArch: noarch

# Private modules are loaded by mx's bootstrap, outside site-packages.
%add_findprov_skiplist %_datadir/%name
%add_findprov_skiplist %_datadir/%name/*
%add_python3_self_prov_path %_datadir/%name/src
%add_python3_compile_include %_datadir/%name

%description
Python command-line tool for building and managing Graal project suites.
Includes the genuine Java tool sources and native toolchain templates used
by mx to build tools on demand in a writable output directory.

%prep
%setup
%patch0 -p1
sed -i '1c#!%__python3' mx.py

%build
%__python3 -m compileall -q src
./mx build --no-daemon --dependencies \
    com.oracle.mxtool.compilerserver,com.oracle.mxtool.checkcopy

%install
install -d %buildroot%_datadir/%name
cp -a .mx_vcs_root mx mx.py select_jdk.py remove_jdks.py src mx.mx java \
    ninja-toolchains javadoc jdk-binaries.json common.json \
    %buildroot%_datadir/%name/
install -Dm755 %SOURCE1 %buildroot%_bindir/mx

%check
MAVEN_COMMAND=xmvn ./mx --java-home=%_jvmdir/java-21-openjdk --max-cpus=4 \
    gate --strict-task-filter MxTests

%files
%_bindir/mx
%_datadir/%name
%doc LICENSE copyrights

%changelog
* Tue Nov 10 2026 Ivan Khanas <xeno@altlinux.org> 7.88.2-alt1
- Initial build for ALT.
