Name:    tomcat-jakartaee-migration
Version: 1.0.9
Release: alt3
Summary: Apache Tomcat migration tool for Jakarta EE

License: Apache-2.0
Group:   Development/Java
URL:     https://tomcat.apache.org
Vcs:     https://github.com/apache/tomcat-jakartaee-migration.git
Source:  %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel >= 17.0
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apache.bcel:bcel)

BuildArch: noarch
Requires: java

%description
The purpose of the tool is to take a web application written for Java EE 8 that
runs on Apache Tomcat 9 and convert it automatically so it runs on Apache
Tomcat 10 which implements Jakarta EE 9.

The tool can be used from the command line or as an Ant task.

%prep
%setup
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build --skip-javadoc

%install
%mvn_install
install -Dpm 644 pom.xml %buildroot%_mavenpomdir/JPP-%name.pom

# CLI helper
install -d -m 0755 %buildroot%_bindir
cat > %buildroot%_bindir/javax2jakarta <<'_EOF'
#!/bin/sh

java -cp "/usr/share/java/tomcat-jakartaee-migration/*:/usr/share/java/*" org.apache.tomcat.jakartaee.MigrationCLI "$@"
_EOF
chmod +x %buildroot%_bindir/javax2jakarta

%files -f .mfiles
%doc *.md
%_bindir/javax2jakarta
%_mavenpomdir/*.pom

%changelog
* Thu Jun 18 2026 Andrey Cherepanov <cas@altlinux.org> 1.0.9-alt3
- Rebuilt with java >= 17.0

* Fri Dec 26 2025 Stanislav Levin <slev@altlinux.org> 1.0.9-alt2
- Package CLI tool (javax2jakarta) (closes: #57376).

* Mon Dec 08 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.0.9-alt1
- Initial build for Sisyphus.
