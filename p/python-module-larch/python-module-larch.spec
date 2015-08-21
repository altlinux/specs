%define oldname python-larch
%global pkgname larch

Name: python-module-larch
Version: 1.20131130
Release: alt1

Summary: Python B-tree library

License: GPLv3+
Group: Development/Python
Url: http://liw.fi/%pkgname/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://code.liw.fi/debian/pool/main/p/%oldname/%{oldname}_%version.orig.tar.gz
Source: %name-%version.tar

BuildArch: noarch

# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)

# build-time only
BuildRequires: cmdtest
BuildRequires: python-module-coverage-test-runner
BuildRequires: python-module-sphinx
# build- and run-time
BuildRequires: python-module-cliapp
BuildRequires: python-module-tracing
BuildRequires: python-module-ttystatus
Source44: import.info

%description
This is an implementation of particular kind of B-tree, based on
research by Ohad Rodeh. See "B-trees, Shadowing, and Clones" (copied
here with permission of author) for details on the data
structure. This is the same data structure that btrfs uses. Note that
my implementation is independent from the btrfs one, and might differ
from what the paper describes.

The distinctive feature of this B-tree is that a node is never
modified (sort-of). Instead, all updates are done by
copy-on-write. Among other things, this makes it easy to clone a tree,
and modify only the clone, while other processes access the original
tree. This is utterly wonderful for my backup application, and that's
the reason I wrote larch in the first place.

I have tried to keep the implementation generic and flexible, so that
you may use it in a variety of situations. For example, the tree
itself does not decide where its nodes are stored: you provide a class
that does that for it. I have two implementations of the NodeStore
class, one for in-memory and one for on-disk storage.

The tree attempts to guarantee this: all modifications you make will
be safely stored in the node store when the larch.Forest.commit method
is called. After that, unless you actually modify the committed tree
yourself, it will be safe from further modifications. (You need to
take care to create a new tree for further modifications, though.)

%package -n python-module-larch-doc
Group: Other
Summary: Documentation for %pkgname

%description -n python-module-larch-doc
This package contains the documentation for %pkgname, a Python
framework for Unix command line programs.

%prep
%setup

%build
%python_build
# Build documentation
make

%install
%python_install
# manpage not installed automatically yet
mkdir -p %buildroot%_man1dir
cp -p fsck-larch.1 %buildroot%_man1dir/

%check
exit 0
# TODO: fix rm .coverage issue
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
make check

%files
%doc COPYING NEWS README
%_man1dir/fsck-larch.1*
%_bindir/fsck-larch
%python_sitelibdir_noarch/*

%files -n python-module-larch-doc
%doc doc/_build/html/*

%changelog
* Fri Aug 21 2015 Vitaly Lipatov <lav@altlinux.ru> 1.20131130-alt1
- new version 1.20131130 (with rpmrb script)

* Thu Aug 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.20130808-alt3
- human build for ALT Linux Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.20130808-alt1_2
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130808-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130316-alt1_2
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130316-alt1_1
- update to new release by fcimport

* Thu Mar 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121216-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121006-alt1_2
- update to new release by fcimport

* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121006-alt1_1
- initial fc import

