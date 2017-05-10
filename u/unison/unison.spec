Name: unison
Version: 2.48.4
Release: alt1%ubt

Summary: File-synchronization tool

Group: Networking/File transfer
License: GPLv2+
Url: http://www.cis.upenn.edu/~bcpierce/unison
# https://github.com/bcpierce00/unison
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: ocaml >= 4.04
BuildRequires: tetex-latex tetex-dvips ghostscript-utils
BuildRequires(pre):rpm-build-ubt

%description
Unison is a file-synchronization tool. It allows two replicas of a
collection of files and directories to be stored on different hosts
(or different disks on the same host), modified separately, and then
brought up to date by propagating the changes in each replica to the
other.

%prep
%setup
%patch0 -p1

%build
make docs

%install
mkdir -p $RPM_BUILD_ROOT%_bindir
cp -f src/unison $RPM_BUILD_ROOT%_bindir

%files
%doc src/COPYING src/RECENTNEWS src/README
%doc doc/unison-manual.pdf
%_bindir/*

%changelog
* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 2.48.4-alt1%ubt
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 2.45.28-alt1
- new version

* Thu Jul 12 2012 Anton Farygin <rider@altlinux.ru> 2.45.4-alt1
- first build for Sisyphus

