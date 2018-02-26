Name: git-subtree
Version: 0.4
Release: alt1

Group: Development/Other
Summary: Merge git subtrees together and split repository into subtrees
License: %gpl2plus
Url: https://github.com/apenwarr/git-subtree.git
BuildArch: noarch

Source: %name-%version.tar

# Automatically added by buildreq on Fri Apr 15 2011
# optimized out: docbook-dtds docbook-style-xsl libgpg-error python-base python-modules xml-common xml-utils xsltproc
BuildRequires: asciidoc git-core python-modules-encodings time xmlto

BuildRequires(pre): rpm-build-licenses

%description
Subtrees allow subprojects to be included within a subdirectory
of the main project, optionally including the subproject's
entire history.

For example, you could include the source code for a library
as a subdirectory of your application.

Subtrees are not to be confused with submodules, which are meant for
the same task. Unlike submodules, subtrees do not need any special
constructions (like .gitmodule files or gitlinks) be present in
your repository, and do not force end-users of your
repository to do anything special or to understand how subtrees
work. A subtree is just a subdirectory that can be
committed to, branched, and merged along with your project in
any way you want.

They are also not to be confused with using the subtree merge
strategy. The main difference is that, besides merging
the other project as a subdirectory, you can also extract the
entire history of a subdirectory from your project and make it
into a standalone project. Unlike the subtree merge strategy
you can alternate back and forth between these
two operations. If the standalone library gets updated, you can
automatically merge the changes into your project; if you
update the library inside your project, you can "split" the
changes back out again and merge them back into the library
project.

%prep
%setup -q -n %name-%version

%build
make doc

%install
%make install prefix=%_prefix DESTDIR=%buildroot

%files
%doc README todo %name.txt
%_prefix/libexec/git-core/%name
%_man1dir/*

%changelog
* Fri Apr 15 2011 Mykola Grechukh <gns@altlinux.ru> 0.4-alt1
- initial build for ALT Linux
