Name: 	 be
Version: 1.1.1
Release: alt1
Summary: Bugs Everywhere, a distributed bug tracker

License: GPLv2+
Group:   Development/Tools
URL:	 http://bugseverywhere.org/	

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:  http://download.bugseverywhere.org/releases/be-%version.tar.gz
Source1: _version.py

# remove broken support
Patch1:  be-1.0.1-remove_broken_vcs.patch

BuildArch: noarch

#BuildRequires:  python-docutils
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-docutils
BuildRequires: python-module-docutils-compat
BuildRequires: python-modules-json

# for testing
BuildRequires: bzr
BuildRequires: git-core
BuildRequires: python-module-yaml
BuildRequires: python-module-jinja2
BuildRequires: python-module-cherrypy
BuildRequires: python-module-GitPython

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
%patch1 -p1
rm -rf libbe/storage/vcs/{arch,hg,monotone}.*
sed -i '1d' libbe/version.py
sed -i '1d' misc/completion/be.bash
# remove compiled files
find . -name '*.py?' -exec rm '{}' \;
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
python test.py libbe.storage.{base,util.{config,mapfile,properties,settings_object,upgrade},vcs.{base,git}} || /bin/true

%files
%doc COPYING AUTHORS NEWS README
%_bindir/be
%dir %python_sitelibdir/libbe
%python_sitelibdir/libbe/*
%python_sitelibdir/*.egg-info
%config(noreplace) %_sysconfdir/bash_completion.d/%name.bash
%{_mandir}/man1/%name.1*


%changelog
* Thu Nov 14 2013 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version

* Thu Nov 24 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Return darcs support (thanks vitty@ for package this VCS)

* Wed Nov 23 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial import in Sisyphus
