BuildRequires: /proc
BuildRequires: jpackage-compat
%global git_commit 3e70a1e
%global cluster jruby

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.5
Release:        alt1_1jpp6
Summary:        Java-based codings helper classes for Joni and JRuby

Group:          Development/Java
License:        MIT
URL:            http://github.com/%{cluster}/%{name}
Source0:        http://download.github.com/%{cluster}-%{name}-%{version}-0-g%{git_commit}.tar.gz

BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  jpackage-utils

Requires:       jpackage-utils
Source44: import.info

%description
Java-based codings helper classes for Joni and JRuby.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
echo "See %{url} for more info about the %{name} project." > README.txt

%{ant}


%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_javadir}

%__cp -p target/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/
  %__ln_s %{name}-%{version}.jar %{name}.jar
popd


%files
%{_javadir}/*
%doc README.txt

%changelog
* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1jpp6
- update to new release by jppimport

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp5
- new version

