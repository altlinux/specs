BuildRequires: oss-parent
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

%global group_id  biz.source_code
%global long_ver  2010-12-19

Name:             base64coder
Version:          20101219
Release:          alt1_2jpp7
Summary:          Fast and compact Base64 encoder/decoder Java library
License:          EPL or LGPLv2+ or GPLv2+ or ASL 2.0+ or BSD
Group:            Development/Java
# http://www.source-code.biz/base64coder/java/
URL:              http://www.source-code.biz/%{name}/java/
# http://repo2.maven.org/maven2/biz/source_code/base64coder/2010-12-19/base64coder-2010-12-19-distribution.zip
Source0:          http://repo2.maven.org/maven2/biz/source_code/%{name}/%{long_ver}/%{name}-%{long_ver}-distribution.zip

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-surefire-provider-junit4

Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
Base64Coder is a fast and compact Base64 encoder/decoder class.

There is no Base64 encoder/decoder in the standard Java SDK class library.
The undocumented classes sun.misc.BASE64Encoder and sun.misc.BASE64Decoder
should not be used.

Explanation:
http://java.sun.com/products/jdk/faq/faq-sun-packages.html

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{long_ver}

# convert CR+LF to LF
sed -i 's/\r//g' README.txt CHANGES.txt

%build
mvn-rpmbuild install

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{name}-%{long_ver}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap %{group_id} %{name} %{long_ver} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc README.txt CHANGES.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_2jpp7
- new version

