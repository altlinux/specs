BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.osgi.core

Name:    felix-osgi-core
Version: 1.4.0
Release: alt2_6jpp6
Epoch:   0
Summary: Felix OSGi R4 Core Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org/site/apache-felix-osgi-core.html
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz
Source1: %{name}-%{version}-build.xml.tar.gz

BuildArch: noarch

BuildRequires: ant
BuildRequires: jpackage-utils


Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

tar xf %{SOURCE1}

%{__mkdir_p} .m2/repository

%build
export LANG=en_US.ISO8859-1
%{ant}  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dmaven.settings.offline=true \
       -Dmaven.repo.local=.m2/repository \
       package javadoc

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}/felix
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/felix/%{bundle}.jar

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 pom.xml \
%{buildroot}%{_datadir}/maven2/poms/JPP.felix-%{bundle}.pom
%add_to_maven_depmap org.apache.felix %{bundle} %{version} JPP/felix %{bundle}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE
%{_javadir}*/felix
%{_datadir}/maven2/poms/JPP.felix-%{bundle}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_6jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_6jpp6
- new version

