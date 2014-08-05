# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit b362566
%global cluster wmeissner

Name:     jaffl
Version:  0.5.9
Release:  alt1_5jpp7
Summary:  Java Abstracted Foreign Function Layer
Group:    System/Libraries
License:  LGPLv3
URL:      http://github.com/%{cluster}/%{name}
Source0:  https://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz
Patch0:   jaffl_fix_jar_dependencies.patch
Patch1:   jaffl_remove_impure.patch

BuildRequires: jpackage-utils
BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: jffi
BuildRequires: jnr-x86asm
BuildRequires: objectweb-asm

Requires:      jpackage-utils
Requires:      jffi
Requires:      jnr-x86asm
Requires:      objectweb-asm
BuildArch:     noarch
Source44: import.info

%description
An abstracted interface to invoking native functions from java

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}
%patch0 -p0
%patch1 -p0

# remove all builtin jars
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;

# remove tests/junit dependency
rm -rf test/

mkdir build_lib
build-jar-repository -s -p build_lib jffi jnr-x86asm objectweb-asm/asm \
                                     objectweb-asm/analysis objectweb-asm/commons \
                                     objectweb-asm/tree objectweb-asm/util objectweb-asm/xml

%build
ant

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -m 644 dist/%{name}-0.5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
cp -rp dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_5jpp7
- new version

