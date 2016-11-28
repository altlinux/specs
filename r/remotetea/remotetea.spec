Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          remotetea
Version:       1.1.3
Release:       alt1_1jpp8
Summary:       Java implementation of Sun's ONC/RPC Remote Procedure Protocol
# GPL with exceptions: src/org/acplt/oncrpc/apps/jrpcgen/JrpcgenSHA.java original
# Incorrect Free Software Foundation address https://github.com/remotetea/remotetea/issues/2
License:       LGPLv2+
URL:           http://remotetea.sourceforge.net/

# git clone git://git.code.sf.net/p/remotetea/code remotetea
# (cd remotetea/remotetea/ && git archive --format=tar --prefix=remotetea-1.1.3/ 1.1.3 | xz > ../../remotetea-1.1.3.tar.xz)

Source0:       remotetea-1.1.3.tar.xz
# Use system java_cup
Patch0:        remotetea-1.1.2-system-java_cup.patch

# Remove src/org/acplt/oncrpc/apps/jrpcgen/JrpcgenSHA.java references
# gnu.java.security.provider.SHA.java, bundled libraries without FPC exception
# Clean implementation of JrpcgenSHA.java that calls out to the
# Java standard library's implementation of SHA-1.  It
# should otherwise be interface- and implemenation-compatible with the
# one that depended on bundled code
# https://github.com/remotetea/remotetea/issues/1
Patch1:        remotetea-1.1.2-custom_JrpcgenSHA.patch

BuildRequires: maven-local
BuildRequires: mvn(java_cup:java_cup)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)

BuildArch:     noarch
Source44: import.info

%description
A complete Java-based implementation of Sun's ONC/RPC
Remote Procedure Protocol, including client and server
functionality and some associated tools. No native
code involved, only Java.

%package maven-plugin
Group: Development/Java
Summary:       Remote Tea : ONC/RPC Maven plugin

%description maven-plugin
A Maven Plugin providing access to the
source generator (jrpcgen) in the
Maven life cycle phase 'generate-sources'.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1
rm -rf jrpcgen/src/main/java/org/acplt/oncrpc/apps/jrpcgen/cup_runtime
%patch1 -p1

native2ascii -encoding UTF8 oncrpc/src/main/java/org/acplt/oncrpc/OncRpcUdpClient.java \
 oncrpc/src/main/java/org/acplt/oncrpc/OncRpcUdpClient.java

cp -p information/src/main/resources/META-INF/changelog.html .
cp -p information/src/main/resources/META-INF/docstyle.css .
cp -p information/src/main/resources/META-INF/LICENSE.txt .
cp -p information/src/main/resources/META-INF/readme.html .

%mvn_package :remotetea-maven-plugin maven-plugin
%mvn_alias :remotetea-jportmap org.acplt:portmap
%mvn_alias :remotetea-jrpcgen org.acplt:jrpcgen
%mvn_alias :remotetea-oncrpc org.acplt:oncrpc

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc changelog.html docstyle.css readme.html
%doc LICENSE.txt

%files maven-plugin -f .mfiles-maven-plugin
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_1jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_2jpp8
- new version

