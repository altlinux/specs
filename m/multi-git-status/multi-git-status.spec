Name: multi-git-status
Version: 0
Release: alt1.git20170109

Summary: Show changes in multiple Git repositories
License: MIT
Group: Development/Other

Url: https://github.com/fboender/multi-git-status
Source: %name-%version.tar

BuildArch: noarch

%description
Show uncommited, untracked and unpushed changes
in multiple Git repositories.

multi-git-status shows:
* needs push(BRANCH);
* needs pull(BRANCH);
* uncomitted changes;
* untracked files.

%prep
%setup

%install
install -pDm755 mgitstatus %buildroot%_bindir/mgitstatus

%files
%doc README.md
%_bindir/mgitstatus

%changelog
* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 0-alt1.git20170109
- initial release (thanks freshcode.club)

