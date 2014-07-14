Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:                 jboss-parent
Version:              6
Release:              alt2_8jpp7
Summary:              JBoss Parent POM
Group:                Development/Java
License:              LGPLv2+
URL:                  http://www.jboss.org/

# git clone git://github.com/jboss/jboss-parent-pom.git
# cd jboss-parent-pom/ && git archive --format=tar --prefix=jboss-parent-6/ 6 | xz > jboss-parent-6.tar.xz
Source0:              %{name}-%{version}.tar.xz
# Removing unavailable deps
Patch0:               %{name}-%{version}-deps.patch
BuildArch:            noarch

BuildRequires:        jpackage-utils
BuildRequires:        maven
BuildRequires:        maven-install-plugin
BuildRequires:        maven-javadoc-plugin
BuildRequires:        maven-release-plugin
BuildRequires:        maven-resources-plugin
BuildRequires:        maven-enforcer-plugin


Requires:             jpackage-utils
Requires:             maven
Source44: import.info


%description
The Project Object Model files for JBoss packages.

%prep
%setup -q
%patch0 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.jboss-%{name}.pom

%add_maven_depmap JPP.jboss-%{name}.pom

%files
%doc README.md
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:6-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:6-alt1_8jpp7
- new version

* Thu Sep 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_0.CR1.1jpp6
- jpp 6.0 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:1-alt1_4jpp5
- new version

