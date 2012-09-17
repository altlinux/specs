BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit b362566
%global cluster wmeissner

Name:     jaffl
Version:  0.5.9
Release:  alt1_1jpp7
Summary:  Java Abstracted Foreign Function Layer
Group:    System/Libraries
License:  LGPLv3
URL:      http://github.com/%{cluster}/%{name}
Source0:  https://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz
Patch0:   jaffl_fix_jar_dependencies.patch

# invokedynamic is a Java 7 feature and the method
# which needs it is only defined and not used
Patch1:   jaffl_remove_invokedynamic.patch

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
Requires:       %{name} = %{version}-%{release}
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
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

cp dist/%{name}-0.5.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{_javadir}/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp -rp dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
%add_to_maven_depmap org.jruby.extras %{name} %{version} JPP %{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jaffl.pom

%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*
%doc LICENSE

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.9-alt1_1jpp7
- new version

