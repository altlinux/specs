# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: maven-clean-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          hawtbuf
Version:       1.9
Release:       alt1_2jpp7
Summary:       A rich byte buffer library
Group:         Development/Java
License:       ASL 2.0
URL:           https://github.com/fusesource/hawtbuf/
# git clone git://github.com/fusesource/hawtbuf.git hawtbuf-1.9
# cd hawtbuf-1.9/ && git archive --format=tar --prefix=hawtbuf-1.9/ hawtbuf-project-1.9 | xz > hawtbuf-1.9.tar.xz
Source0:       hawtbuf-%{version}.tar.xz
BuildRequires: fusesource-pom
BuildRequires: jpackage-utils

BuildRequires: apache-commons-logging

# test deps
BuildRequires: junit
BuildRequires: log4j

BuildRequires: maven1
BuildRequires: javacc-maven-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      apache-commons-logging

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
This library implements a simple interface with working with
byte arrays. It is a shame that the Java SDK did not come with
a built in class that was just simply a byte[], int offset,
int length class which provided a rich interface similar to
what the String class does for char arrays. This library
fills in that void by providing a Buffer class which does provide
that rich interface.

%package proto
Group:         Development/Java
Summary:       A protobuf library
Requires:      %{name} = %{version}-%{release}

%description proto
HawtBuf Proto: A protobuf library.

%package protoc
Group:         Development/Java
Summary:       A protobuf compiler as a maven plugin
Requires:      %{name}-proto = %{version}-%{release}
Requires:      maven1

%description protoc
HawtBuf Protoc: A protobuf compiler as a maven plugin.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %%{name}.

%prep
%setup -q
%pom_remove_plugin org.apache.maven.plugins:maven-assembly-plugin

%build

mvn-rpmbuild -Prun-its install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-project.pom
%add_maven_depmap JPP.%{name}-project.pom

mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 644 %{name}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

for m in \
  proto \
  protoc;do
    install -m 644 %{name}-${m}/target/%{name}-${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
    install -pm 644 %{name}-${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
    %add_maven_depmap -f ${m} JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}/%{name}.jar
%{_mavenpomdir}/JPP.%{name}-project.pom
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc license.txt notice.md readme.md

%files proto
%{_javadir}/%{name}/%{name}-proto.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-proto.pom
%{_mavendepmapfragdir}/%{name}-proto
%doc license.txt notice.md %{name}-proto/readme.md

%files protoc
%{_javadir}/%{name}/%{name}-protoc.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-protoc.pom
%{_mavendepmapfragdir}/%{name}-protoc
%doc license.txt notice.md %{name}-protoc/readme.md

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt notice.md

%changelog
* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2jpp7
- initial build

