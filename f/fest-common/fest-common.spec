# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-common
Version:        1.0.11
Release:        alt2_7jpp7
Summary:        FEST: Fixtures for Easy Software Testing

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org
# git clone https://github.com/alexruiz/fest-maven-setup.git
# cd fest-maven-setup
# git archive --prefix="fest-common-1.0.11/" --format=tar \
#   fe974d5a3844e1af942bec0c602dc1e0e7072c15 | \
#   bzip2 - >../fest-common-1.0.11.tar.bz2
Source0:        %{name}-%{version}.tar.bz2
Patch0:         no-assembly.patch
Patch1:         no-site.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-dependency-plugin

Requires:       jpackage-utils
Source44: import.info

%description
Parent POM for all FEST Modules

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild \
        -e \
        install

%install
# no jars here, no javadoc, no docs, is just a parent pom
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%files
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1_5jpp7
- new version

