Name: paketto
Version: 1.10
Release: alt3

Summary: Unusual TCP/IP testing tools
License: BSD
Group: Monitoring

Url: http://www.doxpara.com/
Source: http://www.doxpara.com/code/paketto-%version.tar.gz
Patch: paketto-1.10-gcc4.patch

# Automatically added by buildreq on Mon Jun 15 2009
BuildRequires: flex

%description
The Paketto Keiretsu is a collection of tools that use new and unusual
strategies for manipulating TCP/IP networks.

This package includes:
scanrand (very fast port, host, and network trace scanner),
minewt (user space NAT/MAT gateway),
linkcat(lc) (provides direct access to the network level 2),
paratrace (traceroute-like tool using existing TCP connections),
and phentropy (plots a large data source onto a 3D matrix).

%prep
%setup
%patch -p0

%build
tar zxvf libtomcrypt.tar.gz
pushd libtomcrypt
subst 's/#elif$/#else/' yarrow.c
%make_build
popd

./configure --prefix=/usr --mandir=%_mandir
%make_build

%install
%makeinstall_std
# Fix file conflict with mono-devel:
subst 's/LC 1/LC 8/' %buildroot%_man1dir/lc.1
install -d %buildroot%_man8dir
mv %buildroot%_man1dir/lc.1 %buildroot%_man8dir/lc.8

%files
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man8dir/lc.8*
%exclude %_includedir

%changelog
* Thu Dec 24 2009 Victor Forsyuk <force@altlinux.org> 1.10-alt3
- Fix file conflict with mono-devel: move lc.1 to section 8.

* Wed Jun 24 2009 Victor Forsyuk <force@altlinux.org> 1.10-alt2
- Fix FTBFS with GCC 4.4.

* Wed Apr 09 2008 Victor Forsyuk <force@altlinux.org> 1.10-alt1
- Initial build.

