Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           jeromq
Version:        0.3.5
Release:        alt1_5jpp8
Summary:        Pure Java implementation of libzmq
# License headers in source files seem to indicate LGPLv3+, but pom.xml as well
# as upstream licensing page (http://zeromq.org/area:licensing) specify license
# as LGPLv3 only - lets use stricter variant as safer choice.
License:        LGPLv3
URL:            https://github.com/zeromq/jeromq
BuildArch:      noarch

Source0:        https://github.com/zeromq/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Pure Java implementation of libzmq.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin :maven-checkstyle-plugin

%build
# Tests require network access and fail on Koji.
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md CHANGELOG.md AUTHORS
%doc COPYING.LESSER

%files javadoc -f .mfiles-javadoc
%doc COPYING.LESSER

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_5jpp8
- new fc release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_4jpp8
- new version

