Name: parentlock-sh-functions
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: shell library for parentlock
Group: System/Libraries
License: Artistic-2.0 or ALT-Public-Domain
Source: %name-%version.tar
Url: https:git.altlinux.org/people/viy/packages/parentlock-sh-functions.git

BuildRequires: /usr/bin/parentlock
Requires: /usr/bin/parentlock

%description
parentlock allows sharing a lock among child processes
of given pid. It is useful for shell scripting where there are
lots of nested script calls and we want to share a lock through the
parent - child relationship.

This is a shell library wrapper for parentlock.

%prep
%setup -q

%build

%install
install -m 644 -D parentlock-sh-functions %buildroot%_bindir/parentlock-sh-functions


%files
%doc README.md
%_bindir/parentlock-sh-functions

%changelog
* Fri Jan 20 2023 Igor Vlasenko <viy@altlinux.org> 0.02-alt1
- new version

* Wed Jan 18 2023 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- new version
