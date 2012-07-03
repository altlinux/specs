%define _unpackaged_files_terminate_build 1

Name: topgit
Version: 0.7
Release: alt3.git20090527

Summary: Patch queue manager for Git
License: GPLv2
Group: Development/Tools
Url: http://repo.or.cz/w/topgit.git
BuildArch: noarch

Packager: Maxim Ivanov <redbaron@altlinux.org>

Source0: topgit-0.7.tar

%description
TopGit is designed especially for the case
when you maintain a queue of third-party patches on top of another
(perhaps Git-controlled) project and want to easily organize, maintain
and submit them - TopGit achieves that by keeping a separate topic
branch for each patch and providing few tools to maintain the branches.

%prep
%setup 

%build
%make_build prefix=%_prefix

%install
%makeinstall

%files 
%_bindir/*
%_datadir/%name
%_prefix/libexec/%name
%doc README COPYING

%changelog
* Fri Jul 24 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt3.git20090527
- Corrected prefix

* Sat Jun 13 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt2.git20090527
- Update from upstream

* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt2.git20090512
- Added README and COPYING files

* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7-alt1.git20090512
- Initial build for Sisyphus

