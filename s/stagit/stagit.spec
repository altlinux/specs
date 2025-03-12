Name: stagit
Version: 1.2
Release: alt1

Summary: stagit is a static page generator for git
License: MIT
Group: Networking/Other
Url: https://codemadness.org/stagit.html
Vcs: git://git.codemadness.org/stagit

Source: %name-%version.tar

BuildRequires: libgit2-devel

%description
stagit is a static git page generator.
It generates static HTML pages for a git repository.
Features:
* log of all commits from HEAD;
* log and diffstat per commit;
* show file tree with linkable line numbers;
* show references: local branches and tags;
* detect README and LICENSE file from HEAD and link it as a webpage;
* detect submodules (.gitmodules file) from HEAD and link it as a webpage;
* atom feed of the commit log (atom.xml);
* atom feed of the tags/refs (tags.xml);
* make index page for multiple repositories with stagit-index;
* only a HTTP file server is required;
* simple to setup;
* usable with text-browsers such as dillo, links, lynx and w3m.
Cons:
* not suitable for large repositories (2000+ commits);
* not suitable for large repositories with many files;
* not suitable for repositories with many branches;
* relatively slow to run the first time (about 3 seconds for sbase, 1500+ commits);
* does not support some of the dynamic features cgit has, like:
  - snapshot tarballs per commit,
  - file tree per commit,
  - history log of branches diverged from HEAD,
  - stats (git shortlog -s).

%prep
%setup

%build
%make_build CC='gcc -std=c99 -pedantic'
xz -k %name.1 %name-index.1

%install
%makeinstall_std \
	PREFIX=%prefix \
	MANPREFIX=%_mandir \
	DOCPREFIX=%_datadir/doc/%name-%version \
	MAN1='%name.1.xz %name-index.1.xz'

%files
%doc README
%doc style.css favicon.png logo.png example_create.sh example_post-receive.sh
%_bindir/%name
%_bindir/%name-index
%_man1dir/%name.1.xz
%_man1dir/%name-index.1.xz

%changelog
* Fri Feb 21 2025 Ulysses Apokin <ulysses@altlinux.org> 1.2-alt1
- Initial build for Sisyphus.
