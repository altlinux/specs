Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           plexus-interpolation
Version:        1.14
Release:        alt1_3jpp7
Summary:        Plexus Interpolation API

Group:          Development/Java
License:        ASL 2.0 and ASL 1.1 and MIT
URL:            http://plexus.codehaus.org/plexus-components/plexus-interpolation
#svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-interpolation-1.14/
#tar caf plexus-interpolation-1.14.tar.xz plexus-interpolation-1.14/
Source0:        %{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: junit
BuildRequires: maven
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-shared-reporting-impl
BuildRequires: maven-doxia-sitetools
Source44: import.info

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/plexus
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/interpolation.jar


# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom

%add_maven_depmap JPP.%{name}.pom plexus/interpolation.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/plexus/interpolation.jar
%{_mavenpomdir}/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_3jpp7
- fc version

* Sat Jan 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.14-alt1_1jpp6
- new jpp relase

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.12-alt1_1jpp6
- new version

