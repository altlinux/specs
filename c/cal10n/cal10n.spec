BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cal10n
Version:        0.7.4
Release:        alt2_5jpp6
Epoch:          0
Summary:        Compiler assisted localization library (CAL10N)
Group:          Development/Java
License:        MIT
URL:            http://cal10n.qos.ch/
Source0:        http://cal10n.qos.ch/dist/cal10n-%{version}.tar.gz
Source1:        %{name}-jpp-depmap.xml
Patch0:         %{name}-fix-maven.patch
Requires(post): jpackage-utils >= 1.7.3
Requires(postun): jpackage-utils >= 1.7.3
Requires: jpackage-utils
BuildRequires: apache-commons-parent >= 0:9
BuildRequires: junit4
BuildRequires: maven2
BuildRequires: maven2-plugin-assembly
BuildRequires: maven2-plugin-compiler
BuildRequires: maven2-plugin-install
BuildRequires: maven2-plugin-jar
BuildRequires: maven2-plugin-javadoc
BuildRequires: maven2-plugin-plugin
BuildRequires: maven2-plugin-resources
BuildRequires: maven2-plugin-source
BuildRequires: maven-doxia-sitetools
BuildRequires: maven2-plugin-site
BuildRequires: maven-surefire-maven-plugin
BuildRequires: maven-surefire-provider-junit4
BuildArch:      noarch
Source44: import.info

%description
Compiler Assisted Localization, abbreviated as CAL10N (pronounced as "calion") 
is a java library for writing localized (internationalized) messages.
Features:
    * java compiler verifies message keys used in source code
    * tooling to detect errors in message keys
    * native2ascii tool made superfluous, as you can directly encode bundles 
      in the most convenient charset, per locale.
    * good performance (300 nanoseconds per key look-up)
    * automatic reloading of resource bundles upon change


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package -n maven-cal10n-plugin
Summary:    CAL10N maven plugin
Group:      Development/Java
Requires: maven2
Requires: %{name} = %{version}-%{release}

%description -n maven-cal10n-plugin
Maven plugin verifying that the codes defined in
an enum type match those in the corresponding resource bundles. 

%prep
%setup -q
find -type f -name "*.jar" | xargs -t rm
%patch0 -b .sav0

%build
export LANG=en_US.ISO8859-1
mvn-jpp -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -p -m 644 cal10n-api/target/cal10n-api-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}/cal10n-api-%{version}.jar
install -p -m 644 maven-cal10n-plugin/target/maven-cal10n-plugin-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}/maven-cal10n-plugin-%{version}.jar
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

%add_to_maven_depmap ch.qos.cal10n cal10n-parent %{version} JPP/%{name} cal10n-parent
%add_to_maven_depmap ch.qos.cal10n cal10n-api %{version} JPP/%{name} cal10n-api
%add_to_maven_depmap ch.qos.cal10n maven-cal10n-plugin %{version} JPP/%{name} maven-cal10n-plugin

# poms
install -d -m 755 %{buildroot}%{_datadir}/maven2/poms
install -pm 644 pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}-parent.pom
install -pm 644 cal10n-api/pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-%{name}-api.pom
install -pm 644 maven-cal10n-plugin/pom.xml \
    %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-maven-cal10n-plugin.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr docs/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}*/%{name}
%{_javadir}*/%{name}/cal10n-api.jar
%{_javadir}*/%{name}/cal10n-api-%{version}.jar
%{_datadir}/maven2/poms/JPP.%{name}-%{name}-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-%{name}-api.pom
%{_mavendepmapfragdir}/%{name}

%files -n maven-cal10n-plugin
%{_javadir}/%{name}/maven-cal10n-plugin-%{version}.jar
%{_javadir}/%{name}/maven-cal10n-plugin.jar
%{_datadir}/maven2/poms/JPP.%{name}-maven-cal10n-plugin.pom

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt2_5jpp6
- fixed build with java 7

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt1_5jpp6
- fixed build

