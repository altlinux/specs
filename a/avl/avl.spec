# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/col /usr/bin/dvipdf /usr/bin/dvips /usr/bin/emacs /usr/bin/emacsclient /usr/bin/gconftool-2 /usr/bin/gdb /usr/bin/groff /usr/bin/gvim /usr/bin/gzip /usr/bin/ldd /usr/bin/md5sum /usr/bin/perl /usr/bin/pkg-config /usr/bin/valgrind /usr/bin/xemacs bzlib-devel gcc-c++ gcc-fortran glib2-devel libX11-devel libao-devel libdbus-devel libfuse-devel libgcrypt-devel libgmp-devel libncurses-devel libreadline-devel libxml2-devel pkgconfig(gconf-2.0) pkgconfig(gdk-pixbuf-xlib-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(x11) python-devel unzip zlib-devel
# END SourceDeps(oneline)
# Name of the project is avl, despite Debian using libavl, because they cannot
# do otherwise.
Name:           avl
Version:        0.3.5
Release:        alt1_2
Summary:        AVL tree manipulation library

Group:          System/Libraries
License:        LGPLv2+
URL:            http://git.fruit.je/avl
# Upstream development is API-incompatible per discussion with its author,
# he suggested using Debian orig.tar.gz
Source0:        http://ftp.debian.org/debian/pool/main/liba/libavl/libavl_0.3.5.orig.tar.gz
Patch0:         avl-0.3.5-build.patch
Source44: import.info

%description
This library consists of a set of functions to manipulate AVL trees. AVL
trees are very efficient balanced binary trees, similar to red-black
trees. The functions in this library can handle any kind of payload and
search key type.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .build

%build
export CFLAGS="%{optflags}"
make -f GNUmakefile %{?_smp_mflags}  libdir=%{_libdir}


%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} libdir=%{_libdir}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT%{_libdir} -type f -exec chmod +x '{}' \;

%files
%doc README COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_2
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.5-alt1_1
- initial release by fcimport

