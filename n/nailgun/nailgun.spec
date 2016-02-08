# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define debug_package %{nil}

Name:     nailgun
Version:  0.9.1
Release:  alt1_1jpp8
Summary:  Framework for running Java from the cli without the JVM startup overhead
Group:    Development/Java
License:  ASL 2.0
URL:      http://martiansoftware.com/nailgun/

# https://github.com/martylamb/nailgun/archive/nailgun-all-0.9.1.zip
Source0:  %{name}-%{name}-all-%{version}.zip
Patch0:   remove-tools-jar-dependencies.patch

BuildRequires:  jpackage-utils
BuildRequires: maven-local
Requires:  jpackage-utils
Source44: import.info

# w/o client it is noarch
BuildArch: noarch

%description
Nailgun is a client, protocol, and server for running Java programs from the 
command line without incurring the JVM startup overhead. Programs run in the 
server (which is implemented in Java), and are triggered by the client 
(written in C), which handles all I/O.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-all-%{version}
#%patch0 -p1

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build -- -Dmaven.javadoc.skip=true

%install
%mvn_install

%files -f .mfiles
%doc README.md

#%files javadoc -f .mfiles-javadoc
#%doc LICENSE.txt

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_6jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_5jpp7
- new version

