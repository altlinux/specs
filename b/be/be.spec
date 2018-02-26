Name: 	 be
Version: 1.0.1
Release: alt2
Summary: Bugs Everywhere, a distributed bug tracker

License: GPLv2+
Group:   Development/Tools
URL:	 http://bugseverywhere.org/	

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  http://download.bugseverywhere.org/releases/be-%version.tar.gz
Source1: _version.py

# from commit 2aeaa4e265deb093a5e37c5973deb8d932974491
Patch0:  be-1.0.0-manpage.patch
# remove broken support
Patch1:  be-1.0.1-remove_broken_vcs.patch
# extends bzr module's version parser to handle non-fully-numeric versions
Patch2:  be-1.0.1-bzr_verparse.patch
# fix incorrect version number
Patch3:  be-1.0.1-version.patch

BuildArch: noarch

#BuildRequires:  python-docutils
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-docutils

# for testing
BuildRequires: bzr
BuildRequires: git-core
BuildRequires: python-module-yaml

%description
This is Bugs Everywhere (BE), a bug tracker built on distributed
version control.  It works with Arch, Bazaar, Darcs, Git, Mercurial,
and Monotone at the moment, but is easily extensible.  It can also
function with no VCS at all.

The idea is to package the bug information with the source code, so
that bugs can be marked "fixed" in the branches that fix them.  So,
instead of numbers, bugs have globally unique ids.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
rm -rf libbe/storage/vcs/{arch,hg,monotone}.*
%patch2 -p1
%patch3 -p1
# remove compiled files
cp %SOURCE1 libbe/_version.py

%build
%python_build
make man

%install
%python_install
COMPDIR=%buildroot%_sysconfdir/bash_completion.d
mkdir -p $COMPDIR
cp -p misc/completion/be.bash $COMPDIR/

%check
export LANG=en_US.utf8
git config --global user.email "qa-sisyphus@altlinux.org"
git config --global user.name  "QA Team"
python test.py libbe.storage.{base,util.{config,mapfile,properties,settings_object,upgrade},vcs.{base,git}}

%files
%doc COPYING AUTHORS NEWS README
%_bindir/be
%dir %python_sitelibdir/libbe
%python_sitelibdir/libbe/*
%python_sitelibdir/*.egg-info
%config(noreplace) %_sysconfdir/bash_completion.d/%name.bash
%{_mandir}/man1/%name.1*


%changelog
* Thu Nov 24 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Return darcs support (thanks vitty@ for package this VCS)

* Wed Nov 23 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial import in Sisyphus
