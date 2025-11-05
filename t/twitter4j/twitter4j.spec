%define _unpackaged_files_terminate_build 1

Name: twitter4j
Version: 4.1.2
Release: alt1

Summary: A 100%% pure Java library for the Twitter API with no extra dependency
License: Apache-2.0
Group: Development/Java
Url: http://twitter4j.org
Vcs: https://github.com/Twitter4J/Twitter4J.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Compatibility-with-Gradle-8-alt-patch.patch
Patch1: 0002-Disable-signing-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: jetbrains-annotations
BuildRequires: slf4j
BuildRequires: log4j
BuildRequires: jansi

%description
Twitter4J is an unofficial, open-source Java library for the Twitter API. It
provides a robust and straightforward way for your Java applications to
interact with Twitter's platform. With it, you can easily read timelines, post
tweets, stream data in real-time, and manage your account. The library handles
the underlying HTTP requests and authentication for you. It is the go-to
solution for Java developers needing reliable Twitter integration.

%package javadoc
Group: Development/Java
Summary: API documentation for %name
BuildArch: noarch

%description javadoc
This package contains the %summary.

%prep
%setup
%autopatch -p1

sed -i 's/classifier =/archiveClassifier =/g' twitter4j-core/build.gradle

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sun Nov 02 2025 Ivan Khanas <xeno@altlinux.org> 4.1.2-alt1
- First build for ALT.
