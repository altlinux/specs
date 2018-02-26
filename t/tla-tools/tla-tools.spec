Name: tla-tools
Version: 20050325
Release: alt1

Summary: Helpful utilities for use with tla
License: GPL
Group: Development/Other
Url: http://wiki.gnuarch.org/moin.cgi/tla_2dtools

BuildArch: noarch

Source: %name-%version.tar.bz2
Patch: %name-alt-deps.patch

# Automatically added by buildreq on Mon Oct 04 2004
BuildRequires: tla

%description 
tla-switch     Switches an arch project tree's current branch to another
	       branch, changing the actual source files to match (unlike the
               builtin tla command tla set-tree-version)
tla-fork       Makes a new arch branch forking off the current branch in a
               project tree, and makes that the tree's current branch.
tla-cvs-sync   Does bi-directional gatewaying of an arch branch with a CVS
               branch.
tla-svn-sync   Does bi-directional gatewaying of an arch branch with a
               Subversion branch.
tla-update-ids  Goes through a project tree, and automatically adds or updates
               taglines and explicit id-tags.
tla-file-log   Outputs arch changeset logs which affect a specified file.
tla-fix-changelog-conflicts  Looks through a project tree for ChangeLog.rej
               files (containing conflicts from merging changes to the
	       ChangeLog file), and tries to automatically fix them up, using a
	       simple rule.
tla-copy-changes  Copies changesets from one arch branch to another.
tla-partner    Runs a tla command using the "partner version" of a project tree
               (defined by the contents of the file {arch}/+partner).

Some other handy commands include:

tla-changelogs-to-log Turns any changes in (GNU-style) ChangeLog files in a
	       project tree into a single log text appropriate for including in
               a tla commit log.
tla-commit-merge  Does a tla commit with a log text appropriate for a merge:
	       the Summary: line mentions the merged version, and the body is
               the output of tla log-for-merge filtered through
               tla-abbrev-merge-log.
tla-abbrev-merge-log  A filter for the output of tla log-for-merge which
	       replace repetitive sequences of entries with an abbreviated
               form.
tla-log-to-cvs-log  Converts an arch changeset commit log into a compact form
               suitable for including in a CVS commit log.
tla-fork-archive  Forks branches from one archive into another.

%prep
%setup -q -n %name
%patch -p1

%build
./configure --prefix=%_prefix
make

%install
%makeinstall

%files
%_bindir/*

%changelog
* Fri Mar 25 2005 Alexey Voinov <voins@altlinux.ru> 20050325-alt1
- new snapshot

* Mon Oct 04 2004 Alexey Voinov <voins@altlinux.ru> 20041004-alt1
- initial build

