# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: stgit
Version: 0.14.3
Release: alt2.1.1
%setup_python_module stgit

Summary: Stacked GIT
License: GPLv2
Group: Development/Tools
BuildArch: noarch
Url: http://www.procode.org/stgit/

Packager: Slava Semushin <php-coder@altlinux.ru>

Source: %modulename-%version.tar
Patch0: stgit-upstream-dont_package_empty_doc_dir.patch
Patch1: stgit-alt-makefile-install_man_pages.patch
Patch2: stgit-alt-port_testsuite_to_new_git.patch

BuildRequires: asciidoc git-core xmlto
Requires: git-core

%description
StGit is a Python application providing similar functionality to Quilt
(i.e. pushing/popping patches to/from a stack) on top of Git. These
operations are performed using Git commands and the patches are stored
as Git commit objects, allowing easy merging of the StGit patches into
other repositories using standard Git functionality.

Note that StGit is not an SCM interface on top of Git and it expects a
previously initialised Git repository.

%prep
%setup -n %modulename-%version
%patch0 -p1
%patch1 -p2
%patch2 -p2

%build
%__python setup.py build

# generate manual pages
make -C Documentation man

# run tests
make -C t

%install
%__python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES
%makeinstall_std -C Documentation
bzip2 ChangeLog

%files -f INSTALLED_FILES
%doc AUTHORS ChangeLog.bz2 README TODO
%_man1dir/stg*.1.*
%dir %python_sitelibdir/%name/
%dir %python_sitelibdir/%name/commands/
%dir %_datadir/%name/
%dir %_datadir/%name/contrib/
%dir %_datadir/%name/examples/
%dir %_datadir/%name/templates/

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14.3-alt2.1.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.3-alt2.1
- Rebuilt with python 2.6

* Sat May 30 2009 Slava Semushin <php-coder@altlinux.ru> 0.14.3-alt2
- Fixed build with fresh git
- Added git-core to Requires
- Compress ChangeLog (noted by repocop)
- Updated %%description (don't mention about Cogito)

* Fri May 01 2009 Slava Semushin <php-coder@altlinux.ru> 0.14.3-alt1
- New maintainer
- Updated to 0.14.3 (Closes: #15198)
- Updated %%description
- Changed Group to Development/Tools
- Don't package empty /usr/share/doc/stgit directory
- Some directories created by package now belongs to package
- Packaged more documentation files
- Install and package manual pages
- Run test suite during build
- Enable _unpackaged_files_terminate_build

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 0.12.1-alt1.1
- Rebuilt with python-2.5.

* Wed Mar 21 2007 Alex V. Myltsev <avm@altlinux.ru> 0.12.1-alt1
- Initial build for Sisyphus

