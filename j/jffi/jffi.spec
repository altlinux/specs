# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit 5874d2a
%global cluster wmeissner

Name:    jffi
Version: 1.0.10
Release: alt1_1jpp7
Summary: An optimized Java interface to libffi 

Group:   System/Libraries
License: LGPLv3
URL:     http://github.com/%{cluster}/%{name}
Source0: https://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz
Patch0:  fix_dependencies_in_build_xml.patch
Patch1:  fix_jar_dependencies.patch
Patch2:  fix_compilation_flags.patch

BuildRequires: jpackage-utils
BuildRequires: libffi-devel
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: junit4
Requires: jpackage-utils
Source44: import.info

%description
An optimized Java interface to libffi 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
%patch0
%patch1
%patch2

# ppc{,64} fix
# https://bugzilla.redhat.com/show_bug.cgi?id=561448#c9
sed -i.cpu -e '/m\$(MODEL)/d' jni/GNUmakefile libtest/GNUmakefile
%ifnarch %{ix86} x86_64
rm -rf test/
%endif

# remove random executable bit
chmod 0644 jni/jffi/jffi.h

# remove uneccessary directories
rm -rf archive/ jni/libffi/ jni/win32/ lib/CopyLibs/ lib/junit*

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
mkdir lib/build_lib
build-jar-repository -s -p lib/build_lib junit junit4

ant

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_jnidir}

cp build/jni/libjffi-1.0.so $RPM_BUILD_ROOT%{_libdir}/%{name}/
cp dist/jffi-complete.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}.jar
ln -s %{_libdir}/%{name}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_jnidir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/jffi

%check
ant test

%files
%{_libdir}/%{name}/
%{_jnidir}/*

%files javadoc
%{_javadocdir}/jffi

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_1jpp7
- new version

