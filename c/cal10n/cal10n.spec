BuildRequires: maven-plugin-plugin
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cal10n
Version:        0.7.4
Release:        alt4_9jpp7
Summary:        Compiler assisted localization library (CAL10N)

Group:          Development/Java
License:        MIT
URL:            http://cal10n.qos.ch
Source0:        http://cal10n.qos.ch/dist/cal10n-%{version}.tar.gz
Patch0:         %{name}-fix-maven.patch

BuildArch: noarch

BuildRequires: junit4
BuildRequires: maven
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
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
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package -n maven-cal10n-plugin
Summary:    CAL10N maven plugin
Group:      Development/Java
Requires:   maven
Requires:   %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n maven-cal10n-plugin
Maven plugin verifying that the codes defined in
an enum type match those in the corresponding resource bundles. 

%prep
%setup -q 
find . -name "*.jar" | xargs rm
%patch0

%build
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 -Dmaven.javadoc.source=1.5  -Dproject.build.sourceEncoding=ISO-8859-1 install javadoc:aggregate

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 cal10n-api/target/cal10n-api-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}/cal10n-api.jar
install -m 644 maven-cal10n-plugin/target/maven-cal10n-plugin-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}/maven-cal10n-plugin.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom
install -pm 644 cal10n-api/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-api.pom
install -pm 644 maven-cal10n-plugin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-cal10n-plugin.pom

%add_maven_depmap JPP.%{name}-%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-api.pom %{name}/cal10n-api.jar
%add_maven_depmap JPP.%{name}-maven-cal10n-plugin.pom %{name}/maven-cal10n-plugin.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}*.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-parent*
%{_mavenpomdir}/JPP.%{name}-%{name}-api*
%{_mavendepmapfragdir}/%{name}

%files -n maven-cal10n-plugin
%{_javadir}/%{name}/maven*.jar
%{_mavenpomdir}/JPP.%{name}-maven*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt4_9jpp7
- fixed build

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt3_9jpp7
- fc update

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt3_5jpp6
- applied repocop patches

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt2_5jpp6
- fixed build with java 7

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt1_5jpp6
- fixed build

