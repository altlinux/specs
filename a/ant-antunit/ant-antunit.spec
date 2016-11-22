# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global base_name       antunit

Name:             ant-%{base_name}
Version:          1.3
Release:          alt1_4jpp8
Summary:          Provide antunit ant task
Group:            Development/Other
License:          ASL 2.0
URL:              http://ant.apache.org/antlibs/%{base_name}/
Source0:          http://www.apache.org/dist/ant/antlibs/%{base_name}/source/apache-%{name}-%{version}-src.tar.bz2
BuildArch:        noarch

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:    ant-junit
BuildRequires:    ant-testutil

Requires: javapackages-tools rpm-build-java
Requires:         ant
Source44: import.info


%description
The <antunit> task drives the tests much like <junit> does for JUnit tests.

When called on a build file, the task will start a new Ant project for that
build file and scan for targets with names that start with "test". For each
such target it then will:

   1. Execute the target named setUp, if there is one.
   2. Execute the target itself - if this target depends on other targets the
      normal Ant rules apply and the dependent targets are executed first.
   3. Execute the target names tearDown, if there is one.


%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n apache-%{name}-%{version}
mv CONTRIBUTORS CONTRIBUTORS.orig
iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS.orig > CONTRIBUTORS
touch -r CONTRIBUTORS.orig CONTRIBUTORS


%build
ant package


%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/ant
install -pm 644 build/lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/ant/%{name}.jar
install -d -m 0755 %{buildroot}%{_datadir}/ant/lib
ln -s ../../java/ant/%{name}.jar %{buildroot}%{_datadir}/ant/lib

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{name}-%{version}.pom %{buildroot}%{_mavenpomdir}/JPP.ant-%{name}.pom
%add_maven_depmap JPP.ant-%{name}.pom ant/%{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}/

# OPT_JAR_LIST fragments
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "%{base_name} ant/%{name}" > %{buildroot}%{_sysconfdir}/ant.d/%{base_name}


%files -f .mfiles
%doc CONTRIBUTORS LICENSE NOTICE README README.html WHATSNEW
%config(noreplace) %{_sysconfdir}/ant.d/%{base_name}
%{_datadir}/ant/lib/%{name}.jar

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- new release

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- build with ant-junit

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp7
- new fc release

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

