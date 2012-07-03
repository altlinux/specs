Name: cvlview
Version: 1.0.1
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: CVLView is a viewer for arbitrary data that is stored in pfs files
License: GPLv2+
Group: Graphics

Url: http://cvtool.sourceforge.net/cvlview.html
Source: http://downloads.sourceforge.net/cvtool/cvlview-%version.tar.bz2
Patch1: cvlview-0.3.1-gcc43.patch
Patch2: cvlview-0.3.2-include.patch

# Automatically added by buildreq on Mon Jul 06 2009
# libcvl-devel requires versioned, configure checks for this
BuildRequires: gcc-c++ libcvl-devel >= 1.0.0 libglew-devel libqt4-devel

%description
CVLView is a viewer for arbitrary data that is stored in pfs files. It is
similar to the pfsview and pfsglview tools from pfstools, but tries to be
useful for many types of data.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info*

%changelog
* Mon Aug 30 2010 Victor Forsiuk <force@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 0.3.2-alt1
- 0.3.2

* Thu Nov 13 2008 Victor Forsyuk <force@altlinux.org> 0.3.1-alt2
- Fix FTBFS with gcc4.3 (missing include).

* Thu Jul 31 2008 Victor Forsyuk <force@altlinux.org> 0.3.1-alt1
- 0.3.1

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 0.3.0-alt1
- 0.3.0

* Mon Jan 21 2008 Victor Forsyuk <force@altlinux.org> 0.2.1-alt1
- Initial build.
