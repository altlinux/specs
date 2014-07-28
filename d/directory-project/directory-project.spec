# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          directory-project
Version:       27
Release:       alt2_3jpp7
Summary:       Apache Directory Project Root pom
Group:         Development/Java
License:       ASL 2.0
Url:           http://directory.apache.org/
# svn export http://svn.apache.org/repos/asf/directory/project/tags/27 directory-project-27
# tar czf directory-project-27-src-svn.tar.gz directory-project-27
Source0:       directory-project-27-src-svn.tar.gz
# remove
#     org.apache.geronimo.genesis.plugins tools-maven-plugin 1.4
#     org.apache.xbean maven-xbean-plugin 3.8
#     org.codehaus.mojo clirr-maven-plugin 2.3
#     org.codehaus.mojo dashboard-maven-plugin 1.0.0-beta-1
#     org.codehaus.mojo findbugs-maven-plugin 2.3.2
#     org.codehaus.mojo javancss-maven-plugin 2.0
#     org.codehaus.mojo jdepend-maven-plugi 2.0-beta-2
#     org.codehaus.mojo l10n-maven-plugin 1.0-alpha-2
#     org.codehaus.mojo taglist-maven-plugin 2.4
#     org.codehaus.mojo versions-maven-plugin 1.2
#     com.agilejava.docbkx docbkx-maven-plugin 2.0.13
Patch0:        directory-project-27-pom.patch

BuildRequires: jpackage-utils

BuildRequires: maven-local
BuildRequires: maven-install-plugin

Requires:      maven

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The Apache Directory Project provides directory solutions
entirely written in Java. These include a directory server,
which has been certified as LDAP v3 compliant by the
Open Group (Apache Directory Server), and Eclipse-based
directory tools (Apache Directory Studio).

%prep
%setup -q
%patch0 -p0

%build

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom
%add_maven_depmap JPP.%{name}.pom

%check
mvn-rpmbuild install

%files
%{_mavenpomdir}/JPP.%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt NOTICE.txt README.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_3jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 27-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 27-alt1_1jpp7
- new version

