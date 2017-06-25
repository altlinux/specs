Name: git-update-index-keeping-only
Version: 0.3
Release: alt1

Summary: rm all but matching files from Git index. (Helps git-filter-branch.)

# Licensed as Git itself, but later licenses are allowed, too.
License: %gpl2plus
BuildRequires(pre): rpm-build-licenses
Group: Development/Other
Url: http://git.altlinux.org/people/imz/packages/git-update-index-keeping-only.git

Packager: Ivan Zakharyaschev <imz@altlinux.org>

Source1: git-update-index-keeping-only
Source2: git-filter-only-files
Source3: git-ls-paths-modified-since

BuildPreReq: /bin/bash4
BuildArch: noarch

%description
git-update-index-keeping-only
- A simple executable script that removes all but matching files from
  Git index. It is a useful helper for git-filter-branch --index-filter
  (for convenience, git-filter-only-files script is included). It is
  implemented on top of git-rm. It takes the list of files to keep on stdin.

git-filter-only-files OLD_COMMIT NEW_BRANCH
- A wrapper around git-filter-branch to rewrite history so that only
  some specified files are kept.

git-ls-paths-modified-since SINCE CURRENT_COMMIT
- A helper to list the files modified or added in the diff between
  2 commits (SINCE and CURRENT_COMMIT).

Example of usage:

FILES="$(git-ls-paths-modified-since SINCE)"
export FILES
git filter-branch \
   --index-filter 'echo "$FILES" | git-update-index-keeping-only -q'

or simply:

git-ls-paths-modified-since SINCE | git-filter-only-files HEAD NEW_BRANCH

%install
mkdir -p %buildroot%_bindir
install -m0755 %SOURCE1 %SOURCE2 %SOURCE3 -t %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Sun Jun 25 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1
- Split into more scripts which are individually useful:
  git-filter-only-files (to be combined with other criteria for
  selecting files), git-ls-paths-modified-since.
- git filter-branch --prune-empty won't hurt us usually.
- git-update-index-keeping-only fixed in some corner cases
  (how a file list is passed through xargs).

* Thu Dec 22 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1
- git-update-index-keeping-only:
  correct work relative to the current (not toplevel) dir.
- git-filter-only-files-modified-since:
  made independent of the current workdir.

* Tue Dec 20 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus.
