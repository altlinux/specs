Group: System/Base
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Upstream was originally located at http://code.google.com/p/naga/.  The
# primary author later created a github repo and added some documentation, but
# never tagged any releases.  We take his latest github commit.

Name:           naga
Version:        3.0

%global commit  6f1e95ddfdb1aa7719c98168f0a5efc5be191426
%global date    20200930
%global forgeurl https://github.com/lerno/naga

# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/lerno/naga
%global forgesource https://github.com/lerno/naga/archive/6f1e95ddfdb1aa7719c98168f0a5efc5be191426/naga-6f1e95ddfdb1aa7719c98168f0a5efc5be191426.tar.gz
%global archivename naga-6f1e95ddfdb1aa7719c98168f0a5efc5be191426
%global archiveext tar.gz
%global archiveurl https://github.com/lerno/naga/archive/6f1e95ddfdb1aa7719c98168f0a5efc5be191426/naga-6f1e95ddfdb1aa7719c98168f0a5efc5be191426.tar.gz
%global topdir naga-6f1e95ddfdb1aa7719c98168f0a5efc5be191426
%global extractdir naga-6f1e95ddfdb1aa7719c98168f0a5efc5be191426
%global repo naga
#global owner %nil
#global namespace %nil
%global scm git
#global tag %nil
%global commit 6f1e95ddfdb1aa7719c98168f0a5efc5be191426
#global shortcommit %nil
#global branch %nil
%global version 3.0
%global date 20200930
%global distprefix 20200930git6f1e95d
# FedoraForgeMeta2ALT: end generated meta

URL:            %{forgeurl}
Release:        alt1_21jpp11
Summary:        Simplified Java NIO asynchronous sockets

License:        MIT
Source0:        %{forgesource}
# Fix javadoc errors and warnings
Patch0:         %{name}-javadoc.patch
# Build for Java 1.8 and tell javac that the sources are UTF-8 encoded
Patch1:         %{name}-java18.patch

BuildArch:      noarch
BuildRequires:  ant
BuildRequires:  javapackages-tools

Requires:       javapackages-filesystem
Source44: import.info

%description
Naga aims to be a very small NIO library that provides a handful of
java classes to wrap the usual Socket and ServerSocket with
asynchronous NIO counterparts (similar to NIO2 planned for Java 1.7).

All of this is driven from a single thread, making it useful for both
client (e.g. allowing I/O to be done in the AWT-thread without any
need for threads) and server programming (1 thread for all connections
instead of 2 threads/connection).

Internally Naga is a straightforward NIO implementation without any
threads or event-queues thrown in, it is "just the NIO-stuff", to let
you build things on top of it.

Naga contains the code needed to get NIO up and running without having
to code partially read buffers and setting various selection key
flags.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       javapackages-filesystem
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n naga-6f1e95ddfdb1aa7719c98168f0a5efc5be191426
%patch0 -p1
%patch1 -p1


%build
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  build javadoc

%install
mkdir -p %{buildroot}%{_javadir}
install -D -p -m 644 _DIST/naga-3_0.jar %{buildroot}%{_javadir}/naga.jar
ln -s %{_javadir}/naga.jar %{buildroot}%{_javadir}/naga-3_0.jar

# Javadocs
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp _BUILD/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc Echoserver.md Eventmachine.md Gotchas.md PacketReader.md README.md
%doc --no-dereference COPYING
%{_javadir}/naga.jar
%{_javadir}/naga-3_0.jar

%files javadoc
%doc --no-dereference COPYING
%{_javadocdir}/%{name}

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 3.0-alt1_21jpp11
- update

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 3.0-alt1_19jpp11
- update

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 3.0-alt1_17jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 3.0-alt1_16jpp11
- java11 build

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_14.82svnjpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_12.82svnjpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_10.82svnjpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9.82svnjpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_8.82svnjpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_7.82svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_6.82svnjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2.82svnjpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_1.82svnjpp7
- new version

