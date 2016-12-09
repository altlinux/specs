Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           gpars
Version:        1.2.1
Release:        alt1_6jpp8
Summary:        Groovy Parallel Systems
License:        ASL 2.0 and Public Domain
URL:            http://gpars.codehaus.org
BuildArch:      noarch

# ./generate-tarball.sh %{version}
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        generate-tarball.sh

Patch0:         0001-JSR-166.patch
Patch1:         0002-Enable-XMvn-local-mode.patch
Patch2:         0001-Port-build-script-to-current-gradle.patch

BuildRequires:  gradle-local >= 2.1
BuildRequires:  apache-parent
BuildRequires:  extra166y
BuildRequires:  jcsp
BuildRequires:  netty3
BuildRequires:  groovy-lib
BuildRequires:  multiverse
Source44: import.info

%description
The GPars framework offers Java developers intuitive and safe ways to
handle Java or Groovy tasks concurrently. Leveraging the enormous
flexibility of the Groovy programming language and building on proven
Java technologies, we aim to make concurrent programming for
multi-core hardware intuitive, robust and enjoyable.

GPars is a multi-paradigm concurrency framework, offering several
mutually cooperating high-level concurrency abstractions, such as
Dataflow operators, Promises, CSP, Actors, Asynchronous Functions,
Agents and Parallel Collections.

%prep
%setup -q
cp %{SOURCE1} .
rm -rf lib/ gradle/wrapper/
rm -rf src/main/groovy/groovyx/gpars/extra166y/
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%gradle_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE-2.0.txt

%changelog
* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp8
- new fc release

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

