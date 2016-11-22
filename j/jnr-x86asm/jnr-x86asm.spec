# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit_hash 1dead92
%global tag_hash 2a7fb9b

Name:           jnr-x86asm
Version:        1.0.2
Release:        alt2_9jpp8
Summary:        Pure-java port of asmjit

Group:          Development/Other
License:        MIT
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
Source1:        MANIFEST.MF
Patch0:         add-manifest.patch
BuildArch:      noarch

BuildRequires:  maven-local
Source44: import.info

%description
Pure-java port of asmjit (http://code.google.com/p/asmjit/)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}
%patch0
cp %{SOURCE1} .
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_9jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_8jpp8
- java 8 mass update

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_8jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_5jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_4jpp7
- new version

