%define _unpackaged_files_terminate_build 1

Name: freeplane-twemoji
Version: 12.1.4
Release: alt2

Summary: Emoji package
License: CC-BY-4.0
Group: Development/Java
Url: https://mvnrepository.com/artifact/org.freeplane.emoji/twemoji
Vcs: https://github.com/freeplane/emoji.git
BuildArch: noarch

Source0: %name-%version.tar
# Taken from build/emoji after gradle downloadEmoji.
Source1: emoji.tar

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default

%description
%summary.

%prep
%setup -a1

%build
%gradle_publish

%install
%gradle_register
%gradle_install

%check
%gradle_check

%files -f .mfiles

%changelog
* Wed Apr 22 2026 Arseniy Kostevich <faux@altlinux.org> 12.1.4-alt2
- Include emojilist.txt in jar.

* Mon Apr 20 2026 Arseniy Kostevich <faux@altlinux.org> 12.1.4-alt1
- Initial build for ALT.
