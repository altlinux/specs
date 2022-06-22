%define _unpackaged_files_terminate_build 1

Name: stow
Version: 2.3.1
Release: alt1

Summary: Manage installation of multiple softwares in the same directory tree
License: GPLv3
Group: System/Base

BuildArch: noarch

#VCS: https://git.savannah.gnu.org/git/stow.git
Url: https://www.gnu.org/software/stow
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: rpm-build-perl
BuildRequires: perl-Test-Output
BuildRequires: perl-podlators
BuildRequires: makeinfo
BuildRequires: texi2dvi
BuildRequires: texlive-dist

%description
GNU Stow is a symlink farm manager program which takes distinct sets
of software and/or data located in separate directories on the
filesystem, and makes them all appear to be installed in a single
directory tree.

%package doc
Summary: Documentation for GNU Stow
Group: System/Base

BuildArch: noarch

%description doc
%summary

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --with-pmdir=%perl_vendor_privlib
%make_build

%install
touch ChangeLog doc/ChangeLog.OLD

%makeinstall_std

rm %buildroot%_defaultdocdir/stow/ChangeLog{,.OLD}
rm %buildroot%_defaultdocdir/stow/*.md

%check
%make check

%files
%doc COPYING README.md
%_bindir/stow
%_bindir/chkstow
%_man8dir/stow.8.*
%_infodir/stow.*
%perl_vendor_privlib/Stow.pm
%perl_vendor_privlib/Stow

%files doc
%_defaultdocdir/stow

%changelog
* Wed Jun 22 2022 Egor Ignatov <egori@altlinux.org> 2.3.1-alt1
- First build for ALT
