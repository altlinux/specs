BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           cargo-parent
Version:        4.7
Release:        alt1_1jpp7
Summary:        Parent pom file for cargo.codehaus.org project

Group:          Development/Java
License:        ASL 2.0
URL:            http://cargo.codehaus.org/
#svn export http://svn.codehaus.org/cargo/pom/tags/cargo-parent-4.7/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:  codehaus-parent

Requires:       jpackage-utils
Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils
Requires:       codehaus-parent
Source44: import.info

%description
This package contains the cargo parent pom.

%prep
%setup -q


%build
mvn-rpmbuild install


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_to_maven_depmap org.codehaus.cargo cargo-parent %{version} JPP %{name}


%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Thu Jun 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.7-alt1_1jpp7
- new version

