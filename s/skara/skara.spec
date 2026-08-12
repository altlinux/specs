%define _unpackaged_files_terminate_build 1
%define javaver 21
%define githash 4b951a3c

Name:    skara
Version: 20260810
Release: alt2.%githash

Summary: The goal of this Project is to investigate alternative SCM and code review options for the JDK source code
License: GPL-2.0
Group:   Development/Java
Url:     https://openjdk.org/projects/skara
VCS:     https://github.com/openjdk/skara.git

Source: %name-%version.tar

Patch0: %name-publish-modules.patch

ExclusiveArch: %java_arches

Requires: java-%javaver-openjdk-headless

BuildRequires(pre): rpm-macros-java
BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java
BuildRequires: java-%javaver-openjdk-devel
BuildRequires: java-%javaver-openjdk-jmods
BuildRequires: /proc
BuildRequires: xgradle
BuildRequires: git
BuildRequires: mockito-junit-jupiter
BuildRequires: junit
BuildRequires: apiguardian
BuildRequires: opentest4j
BuildRequires: univocity-parsers

%description
The goal of Project Skara was to investigate alternative SCM and code
review options for the OpenJDK source code, including options based upon
Git rather than Mercurial, and including options hosted by third parties.
That part of the project has now concluded and all active OpenJDK
projects have migrated to GitHub. The continuation of project Skara is
now about operating and maintaining the infrastructure necessary to
support the current development processes of the OpenJDK organization.

The technical parts of project Skara include several server-side tools
also called bots aiding contributors during code reviews. The Skara
technical tooling also includes several command-line utilities for
interacting with Git source code hosting providers from the command-line/

%prep
%setup
%autopatch -p1

%build
%gradle_publish offline

%install
%gradle_register --exclude-artifacts=test
%gradle_install

mkdir -pv %buildroot%_man1dir
for var in $(ls build/bin/man/man1); do
  install -m 444 build/bin/man/man1/$var %buildroot%_man1dir/$var ;
done
rm -rv build/bin/man
mkdir -pv %buildroot%_bindir
for var in $(ls build/bin/); do
install -m 755 build/bin/$var %buildroot%_bindir/$var ;
done

find %buildroot%_bindir -type f -exec sed -i 's|JAVA_LAUNCHER="${DIR}/../image/bin/java"|JAVA_LAUNCHER="/usr/lib/jvm/jre-%javaver/bin/java"|g' {} +
find %buildroot%_bindir -type f -exec sed -i '1a export SKARA_JAVA_OPTS=\"--module-path %_javadir/%name \$SKARA_JAVA_OPTS\"' {} +

mkdir -pv %buildroot%_sysconfdir/%name
install -m 644 %name.gitconfig %buildroot%_sysconfdir/%name/%name.gitconfig

%post
echo "Fore using skara cli tools run:"
echo "\$ git config --global include.path /etc/skara/skara.gitconfig"

%files -f .mfiles
%doc README.md
%_sysconfdir/%name/%name.gitconfig
%_bindir/*
%_man1dir/*

%changelog
* Wed Aug 12 2026 Artem Semenov <savoptik@altlinux.org> 20260810-alt2.4b951a3c
- Change group to Development/Java

* Tue Aug 11 2026 Artem Semenov <savoptik@altlinux.org> 20260810-alt1.4b951a3c
- Initial build for Sisyphus
