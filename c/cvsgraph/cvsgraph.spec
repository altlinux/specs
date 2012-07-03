Name: cvsgraph
Version: 1.7.0
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Create graphs of branches and revisions for files in a CVS repository
License: GPLv2+
Group: System/Servers

URL: http://www.akhphd.au.dk/~bertho/cvsgraph
Source: %url/release/%name-%version.tar.gz

# Automatically added by buildreq on Thu May 22 2008
BuildRequires: flex libfreetype-devel libgd2-devel

Requires: fonts-ttf-vera

%description
CvsGraph is a utility to make a graphical representation of all revisions and
branches of a file in a CVS/RCS repository.

%prep
%setup

%__subst 's@bitstream-vera@ttf/TrueType-vera@g' cvsgraph.conf

%build
%configure
%make_build

%install
install -Dpm755 cvsgraph %buildroot%_bindir/cvsgraph
install -Dpm644 cvsgraph.conf %buildroot%_sysconfdir/cvsgraph.conf
install -Dpm644 cvsgraph.1 %buildroot%_man1dir/cvsgraph.1
install -Dpm644 cvsgraph.conf.5 %buildroot%_man5dir/cvsgraph.conf.5

%files
%config(noreplace) %_sysconfdir/*
%_bindir/*
%_man1dir/*
%_man5dir/*

%changelog
* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 1.7.0-alt1
- 1.7.0

* Thu Jul 27 2006 Victor Forsyuk <force@altlinux.ru> 1.6.1-alt1
- 1.6.1
- Fixed path to used fonts in config.

* Tue Jan 17 2006 Victor Forsyuk <force@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Tue Jul 19 2005 Victor Forsyuk <force@altlinux.ru> 1.5.2-alt1
- Initial build.
