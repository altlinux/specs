Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global githash 3017160f847564879520c564b4bb04abb7b680fe


Name:           signpost-core
Version:        1.2.1.2
Release:        alt1_16jpp8
Summary:        A simple, light-weight, and modular OAuth client library for the Java platform

License:        ASL 2.0
URL:            https://github.com/mttkay/signpost
Source0:        https://github.com/mttkay/signpost/archive/%{githash}/signpost-%{githash}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch 
BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
Source44: import.info

%description
Signpost is the easy and intuitive solution for signing HTTP messages on the 
Java platform in conformance with the OAuth Core 1.0a standard. 
Signpost follows a modular and flexible design, allowing you to combine it with
different HTTP messaging layers

%package -n oauth-signpost
Group: Development/Java
Summary:        Parent POM for %{name}

%description -n oauth-signpost
This package contains the Parent POM for %{name}.

%package -n signpost-commonshttp4
Group: Development/Java
Summary:        Signpost Apache HttpClient Supports

%description -n signpost-commonshttp4
Signpost Apache HttpClient Supports.
 
%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n signpost-%{githash}

# Remove pre-built JAR and class files
find -name '*.jar' -delete
find -name '*.class' -delete

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

# Unneeded modules
%pom_disable_module signpost-jetty6

# Resolve javadoc doclint problems
%pom_remove_plugin :maven-javadoc-plugin
# Unneeded task
%pom_remove_plugin -r :maven-antrun-plugin

%mvn_file :%{name} %{name}
%mvn_file :signpost-commonshttp4 signpost-commonshttp4

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.markdown
%doc --no-dereference LICENSE

%files -n oauth-signpost -f .mfiles-oauth-signpost
%doc --no-dereference LICENSE

%files -n signpost-commonshttp4 -f .mfiles-signpost-commonshttp4

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1.2-alt1_16jpp8
- new version

* Fri May 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1.2-alt1_15jpp8
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1.2-alt1_2jpp7
- new version

