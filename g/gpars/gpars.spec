Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           gpars
Version:        1.2.1
Release:        alt1_12jpp8
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
Patch2:         0003-Port-build-script-to-current-gradle.patch
Patch3:         gpars-1.2.1-port-to-netty-3.10.6.patch

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
%patch3 -p1

%build
%gradle_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_12jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_11jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_9jpp8
- new release

* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp8
- new fc release

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp8
- unbootstrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

