Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 0a3b42373f38883cc1f68388eba33967baac8980
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           jabrt
Version:        1.0
Release:        alt1_14.git0a3b423jpp11
Summary:        ABRT Java bindings

License:        GPLv2+
URL:            https://github.com/mozeq/%{name}
Source0:        http://jmoskovc.fedorapeople.org/jabrt-1.0-git%{shortcommit}.tar.gz
Source1:        http://www.gnu.org/licenses/gpl-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(junit:junit)
Source44: import.info


%description
ABRT Java bindings providing a convenient way to report problems

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{version}-%{commit}

cp %{SOURCE1} LICENSE

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.0-alt1_14.git0a3b423jpp11
- new version

