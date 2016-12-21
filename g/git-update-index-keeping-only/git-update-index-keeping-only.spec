Name: git-update-index-keeping-only
Version: 0.1
Release: alt1

Summary: rm all but matching files from Git index. (Helps git-filter-branch.)

# Licensed as Git itself, but later licenses are allowed, too.
License: %gpl2plus
BuildRequires(pre): rpm-build-licenses
Group: Development/Other
Url: http://git.altlinux.org/people/imz/packages/git-update-index-keeping-only.git

Packager: Ivan Zakharyaschev <imz@altlinux.org>

Source1: git-update-index-keeping-only
Source2: git-filter-only-files-modified-since

BuildPreReq: /bin/bash4
BuildArch: noarch

%description
git-update-index-keeping-only
- A simple executable script that removes all but matching files from
Git index. It is a useful helper for git-filter-branch --index-filter
(example: the included git-filter-only-files-modified-since script).
It is implemented on top of git-rm. It takes the list of files to keep
on stdin.

git-filter-only-files-modified-since SINCE OLD_COMMIT NEW_BRANCH
- A command to rewrite history so that only the files modified or
added in the diff between 2 commits (SINCE and OLD_COMMIT) are kept.

Example (similar to: git-filter-only-files-modified-since SINCE HEAD):

FILES="$(git diff-tree "$SINCE": HEAD: -r --name-only --diff-filter=MACRT)"
export FILES
git filter-branch \
   --index-filter 'echo "$FILES" | git-update-index-keeping-only -q'

%install
mkdir -p %buildroot%_bindir
install -m0755 %SOURCE1 %SOURCE2 -t %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Tue Dec 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus.
