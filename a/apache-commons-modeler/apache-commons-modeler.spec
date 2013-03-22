Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       modeler
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.0.1
Release:          alt1_9jpp7
Summary:          Model MBeans utility classes
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    junit

Requires:         jpackage-utils
Requires:         apache-commons-beanutils
Requires:         apache-commons-digester
Requires:         apache-commons-logging
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils

# This should go away with F-17
Provides:         jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 0:2.0.1-6
Source44: import.info

%description
Commons Modeler makes the process of setting up JMX (Java Management 
Extensions) MBeans easier by configuring the required meta data using an XML 
descriptor. In addition, Modeler provides a factory mechanism to create the 
actual Model MBean instances.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
# This should go away with F-17
Obsoletes:        jakarta-%{short_name}-javadoc < 0:2.0.1-6
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

%build
# TODO: Use Maven for building as soon as upstream provides proper build.xml. 
export CLASSPATH=$(build-classpath \
                   apache-commons-logging \
                   apache-commons-digester \
                   apache-commons-beanutils \
                   junit )

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first test dist

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 dist/%{short_name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_9jpp7
- fc update

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_0.r832084.4jpp6
- set target 5

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_0.r832084.4jpp6
- new version

