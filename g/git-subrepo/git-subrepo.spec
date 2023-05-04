# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: git-subrepo
Version: 0.4.6
Release: alt1

Group: Development/Other
Summary: git submodule alternative
License: MIT
Url: https://github.com/ingydotnet/git-subrepo

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: git-core

%description
git-subrepo command "clones" an external git repo into a subdirectory
of your repo. Later on, upstream changes can be pulled in, and local
changes can be pushed back. Simple.

%prep
%setup

%build

%install

%_make_bin install DESTDIR=%buildroot PREFIX=%_prefix

%files
%doc ReadMe.pod License
%_prefix/libexec/git-core/git-subrepo
%_prefix/libexec/git-core/git-subrepo.d/bash+.bash
%_prefix/libexec/git-core/git-subrepo.d/help-functions.bash
%_man1dir/git-subrepo.1*

%changelog
* Thu May 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.4.6-alt1
- Initial build for ALT Sisyphus.
