Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global base_name       antunit

Name:           ant-%{base_name}
Version:        1.4
Release:        alt1_2jpp11
Summary:        Provide antunit ant task
License:        ASL 2.0
URL:            http://ant.apache.org/antlibs/%{base_name}/
Source0:        http://www.apache.org/dist/ant/antlibs/%{base_name}/source/apache-%{name}-%{version}-src.tar.bz2
# Do not download ivy
Patch0:         ant-antunit-local.patch
BuildArch:      noarch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  ant-testutil
BuildRequires:  ivy-local
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
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n apache-%{name}-%{version}
%patch0 -p1

cat > build.properties <<EOF
javac.-source=6
javac.-target=1.6
javac.test-source=6
javac.test-target=1.6
EOF
mkdir ivy
build-jar-repository -p ivy ivy
mv CONTRIBUTORS CONTRIBUTORS.orig
iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS.orig > CONTRIBUTORS
touch -r CONTRIBUTORS.orig CONTRIBUTORS


%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  -Divy.mode=local package


%install
%mvn_artifact %{name}-%{version}.pom build/lib/%{name}-%{version}.jar
%mvn_file ":ant-antunit" ant/ant-antunit
%mvn_install -J docs/

# OPT_JAR_LIST fragments
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant/%{name}" > %{buildroot}%{_sysconfdir}/ant.d/%{base_name}


%check
# Not resolving local antunit at the moment
ant -Divy.mode=local -lib build/lib test || :


%files -f .mfiles
%doc --no-dereference common/LICENSE NOTICE
%doc CONTRIBUTORS README README.html WHATSNEW
%config(noreplace) %{_sysconfdir}/ant.d/%{base_name}

%files javadoc -f .mfiles-javadoc
%doc --no-dereference common/LICENSE NOTICE


%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.4-alt1_2jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_13jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_11jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_10jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5jpp8
- new jpp release

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

