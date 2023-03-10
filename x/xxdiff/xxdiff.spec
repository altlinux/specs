## https://github.com/blais/xxdiff.git
## git archive --prefix xxdiff-`cat VERSION`/ master > ~/RPM/SOURCES/xxdiff-`cat VERSION`.tar.gz

Summary: A graphical front end to the diff command
Name: xxdiff
Version: 5.1
Release: alt1
License: GPLv2
Group: Development/Tools
Source: %name-%version.tar.gz
Url: https://furius.ca/xxdiff/

# Automatically added by buildreq on Fri Mar 10 2023
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libqt6-core libqt6-dbus libqt6-gui libqt6-widgets libstdc++-devel python3 python3-base python3-dev python3-module-pkg_resources sh4
BuildRequires: flex python3-module-setuptools qt6-base-devel

%description
xxdiff is a graphical browser for viewing the differences between two
files and can be used to produce a merged version.  The text of the
two or three files are presented side by side with their differences
highlighted for easy identification.

%package tools
Summary: tools for xxdiff, %summary
Group: Development/Tools
Buildarch: noarch

%description tools
%summary

%prep
%setup

%build
make -C src -f Makefile.bootstrap
%make_build -C src
%python3_build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_mandir/man1

install -D bin/xxdiff %buildroot%_bindir/
install -D src/xxdiff.1 %buildroot%_man1dir/
%python3_install

%files
%doc README* TODO PKGINFO CHANGES
%doc doc
%_bindir/xxdiff
%_mandir/man1/xxdiff.1*

%files tools
%python3_sitelibdir_noarch/*
%exclude %_bindir/xxdiff
%_bindir/*
# XXX python2 legacy scripts
%exclude %_bindir/termdiff
%exclude %_bindir/xx-p4-unmerge
%exclude %_bindir/xx-svn-review

%changelog
* Fri Mar 10 2023 Fr. Br. George <george@altlinux.ru> 5.1-alt1
- Initial build for ALT
