Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           juniversalchardet
Version:        2.4.0
Release:        alt1_2jpp11
Summary:        Java character encoding detection

# Choice of licenses offered in each source file
License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            https://github.com/albfernandez/juniversalchardet
BuildArch:      noarch
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
Source44: import.info

%{?javadoc_package}

%description
Juniversalchardet is a Java port of universalchardet, that is, the
encoding detector library of Mozilla.

%prep
%setup -q


# Fix newline encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

# Plugins not needed for an RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Provide alias for the old name
%mvn_alias com.github.albfernandez:juniversalchardet com.googlecode.juniversalchardet:juniversalchardet

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc mozilla_repositories.txt README.md
%doc --no-dereference LICENSE

%changelog
* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 2.4.0-alt1_2jpp11
- new version

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_13jpp8
- fixed build with new java

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_12jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_11jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_10jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_9jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_7jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp8
- new version

