%define _unpackaged_files_terminate_build 1

Name: git-publish
Version: 1.8.2
Release: alt1

Summary: Prepare and store patch revisions as git tags
License: MIT
Group: Development/Other
Url: https://github.com/stefanha/git-publish
Vcs: https://github.com/stefanha/git-publish.git
BuildArch: noarch

Source: %name-%version.tar

Conflicts: skara

BuildRequires: rpm-build-python3
BuildRequires: perl-podlators

%description
Tired of manually creating patch series emails?

git-publish prepares patches and stores them as git tags for future
reference. It works with individual patches as well as patch series.
Revision numbering is handled automatically.

No constraints are placed on git workflow, both vanilla git commands
and custom workflow scripts are compatible with git-publish.

Email sending and pull requests are fully integrated so that publishing
patches can be done in a single command.

Hook scripts are invoked during patch preparation so that custom checks
or test runs can be automated.

%prep
%setup

%build
pod2man --center "git-publish Documentation" --release "%{version}" git-publish.pod git-publish.1

%install
install -Dm755 git-publish "%buildroot%_bindir/git-publish"
install -Dm644 git-publish.1 "%buildroot%_man1dir/git-publish.1"

%files
%doc LICENSE README.md
%_bindir/git-publish
%_man1dir/git-publish.*

%changelog
* Fri Aug 14 2026 Sergey Zhidkih <rx1513@altlinux.org> 1.8.2-alt1
- Initial build.
