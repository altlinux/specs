Name: gaffitter
Version: 0.6.0
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Genetic Algorithm File Fitter
License: GPLv3+
Group: File tools

URL: http://gaffitter.sourceforge.net/
Source: http://downloads.sourceforge.net/gaffitter/gaffitter-%version.tar.bz2

# Automatically added by buildreq on Sun Aug 17 2008
BuildRequires: gcc-c++

%description
Genetic Algorithm File Fitter (gaffitter) is a command-line software that
extracts via genetic algorithms subsets of a list of files/directories that
best fit the given volume size (target), such as CD, DVD and others.

%prep
%setup

%build
%make_build

%install
%make_install DESTDIR=%buildroot prefix=/usr install

%files
%_bindir/*

%changelog
* Sun Aug 17 2008 Victor Forsyuk <force@altlinux.org> 0.6.0-alt1
- 0.6.0

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 0.5.2-alt1
- 0.5.2

* Thu Apr 05 2007 Victor Forsyuk <force@altlinux.org> 0.5.1-alt1
- Initial build.
