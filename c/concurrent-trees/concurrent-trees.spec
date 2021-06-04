Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          concurrent-trees
Version:       2.6.1
Release:       alt1_10jpp11
Summary:       Concurrent Trees for Java
License:       ASL 2.0
URL:           https://github.com/npgall/%{name}/
Source0:       https://github.com/npgall/%{name}/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
# for version 2.6.0 add bnd-maven-plugin
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)

BuildArch:     noarch
Source44: import.info

%description
This library provides concurrent Radix Trees and
concurrent Suffix Trees for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn %{name}-%{version}
rm -r documentation/javadoc
rm -r documentation/documents
rm documentation/images/dfs-comic.png

# remove unnecessary dependency on parent POM
%pom_remove_parent code

# Unneeded tasks
%pom_remove_plugin :maven-release-plugin code
%pom_remove_plugin :maven-gpg-plugin code
%pom_remove_plugin :maven-javadoc-plugin code
%pom_remove_plugin :maven-source-plugin code

%mvn_file :%{name} %{name}

%build
# the following does not work in f28, probably a bug
#%%mvn_build -- -f code/pom.xml
cd code
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
cd code
%mvn_install

%files -f code/.mfiles
%doc README.md documentation/
%doc --no-dereference LICENSE.txt

%files javadoc -f code/.mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.6.1-alt1_10jpp11
- new version

