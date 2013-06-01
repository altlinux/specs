# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
Name:          znerd-oss-parent
Version:       3
Release:       alt1_5
Summary:       Znerd.org OSS Parent
Group:         Development/C
License:       BSD
URL:           https://github.com/znerd/znerd-oss-parent
# git clone git://github.com/znerd/znerd-oss-parent.git znerd-oss-parent-3
# (cd znerd-oss-parent-3/ && git archive --format=tar --prefix=znerd-oss-parent-3/ znerd-oss-parent-3 | xz > ../znerd-oss-parent-3-src-git.tar.xz)
Source0:       %{name}-%{version}-src-git.tar.xz

BuildRequires: java-devel
BuildRequires: jpackage-utils

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
# required by enforcer-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Parent for znerd.org OSS Projects.

%prep
%setup -q

%build
# Nothing to do
%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-parent.pom

%check
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP.%{name}-parent.pom
%{_mavendepmapfragdir}/%{name}
%doc CHANGES.txt COPYRIGHT.txt README.txt

%changelog
* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 3-alt1_5
- new version

