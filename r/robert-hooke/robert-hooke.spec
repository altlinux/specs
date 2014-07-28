Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global upstream    technomancy
%global groupId     robert
%global artifactId  hooke
%global commit_hash 30d2f8f

Name:           %{groupId}-%{artifactId}
Version:        1.2.0
Release:        alt2_4jpp7
Summary:        Extension mechanism for Clojure functions

# upstream asked to include license text:
# https://github.com/technomancy/robert-hooke/issues/9
License:        EPL
URL:            https://github.com/%{upstream}/%{name}/
# wget --content-disposition %%{url}/tarball/%%{commit_hash}
# upstream has not pushed post-1.1.2 tags yet, thus the odd source filename:
# https://github.com/technomancy/robert-hooke/issues/8
Source0:        %{upstream}-%{name}-1.1.2-18-g%{commit_hash}.tar.gz
# generated using 'lein pom' using Leiningen 2.0.0-preview6
# as we don't have leiningen 2.x packaged yet
# (Leiningen 2.x is needed as project.clj uses new-style profiles
#  not supported by Leiningen 1.x)
Source1:        %{name}-pom.xml

BuildArch:      noarch

BuildRequires:  jpackage-utils


Requires:       jpackage-utils
%if 0%{?rhel}
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
%endif

Requires:       clojure
Source44: import.info

%description
Robert Hooke provides a flexible, composable mechanism by which you
can extend behavior of functions after they've been defined. It's
named after Robert Hooke FRS, a founding member of the Royal Society
who made many important discoveries in the fields of Gravitation,
Microscopy, and Astronomy.


%prep
%setup -q -n %{upstream}-%{name}-%{commit_hash}
cp -p %{SOURCE1} pom.xml


%build
jar cf %{name}.jar -C src .


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 %{name}.jar \
    $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
pushd $RPM_BUILD_ROOT/%{_javadir}
# so developers can find this by the upstream name
ln -s %{name}.jar %{artifactId}.jar
popd

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
    $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%if 0%{?add_maven_depmap:1}
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%else
%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP %{name}.jar
%endif


%files
%doc README.md Changelog
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom
%{_javadir}/%{name}.jar
%{_javadir}/%{artifactId}.jar


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3jpp7
- new version

