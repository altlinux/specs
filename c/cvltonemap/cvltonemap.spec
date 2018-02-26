Name: cvltonemap
Version: 0.2.4
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: CVLTonemap is an interactive tone mapping tool for high dynamic range images
License: GPLv2+
Group: Graphics

Url: http://cvtool.sourceforge.net/cvltonemap.html
Source: http://download.sourceforge.net/cvtool/cvltonemap-%version.tar.bz2

# Automatically added by buildreq on Mon Nov 08 2010
# See configure.ac for required libcvl-devel version
BuildRequires: gcc-c++ libGLU-devel libcvl-devel >= 1.0.0 libglew-devel libqt4-devel

%description
CVLTonemap is an interactive viewer and tone mapping tool for high dynamic range
(HDR) images. By performing the tone mapping on the graphics processing unit
(GPU), CVLTonemap can immediately display the results of method and parameter
changes.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_infodir/cvl*

%changelog
* Mon Nov 08 2010 Victor Forsiuk <force@altlinux.org> 0.2.4-alt2
- Renew build requirements (libGLU-devel was optimized out and lost due to
  changes in dependency chain).

* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 0.2.4-alt1
- 0.2.4

* Thu Jul 16 2009 Victor Forsyuk <force@altlinux.org> 0.2.3-alt1
- Initial build.
