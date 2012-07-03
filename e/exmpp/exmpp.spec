%def_disable debug

%define upstream_version 0.9.9
# %define gitdate 20110328
Name: exmpp
#Version: %upstream_version.%gitdate
Version: %upstream_version
Release: alt2
Summary: Erlang XMPP library.
License: %epl
Group: Development/Erlang
URL: https://github.com/processone/exmpp
Source: %name-%version.tar
Requires: openssl expat zlib
Requires: erlang-otp
Packager: Sergey Shilov <hsv@altlinux.org>

BuildRequires(pre): rpm-build-erlang rpm-build-licenses

BuildRequires: autoconf automake libtool symlinks
BuildRequires: libssl-devel libexpat-devel zlib-devel
BuildRequires: erlang-devel erlang-otp-devel

%description
Exmpp is an Erlang application which provides the modules to ease the
development of an XMPP/Jabber server or client.

%package devel
Summary: Headers for %name modules
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %version-%release

%description devel
Headers for %name Erlang XMPP library modules.

%package doc
Summary: %name documentation
Group: Development/Erlang
BuildArch: noarch
Requires: %name = %version-%release

%description doc
Documentation for %name Erlang XMPP library in html format.


%prep
%setup -n  %name-%version
find . -name *.erl -exec subst "s/bool()/boolean()/g" {} \;
sed -i 's|\-Werror||g' configure.ac


%build
%autoreconf
%configure --prefix=%buildroot%_otplibdir
%make

%install
%make_install ERLANG_LIBDIR=%buildroot%_otplibdir ERLANG_ILIBDIR=%_otplibdir INSTALL_PREFIX=%buildroot install
# Make symlinks in src to ../include/*.hrl
for l in $(ls -d %buildroot%_otplibdir/*); do
    if [ -d $l/src ]; then
      H=$(find $l/src -type f -name '*.hrl'  | grep -v '.*_internal\.hrl$') ||:
      if [ -n "$H" ]; then
          [ -d $l/include ] || install -d -m 0755 $l/include
          mv $H $l/include/
          for f in $H; do
            ln -sf $l/include/$(basename $f) $f
          done
          find $l/src/* -not -type l -not -type d -delete
      else
          rm -rf $l/src
      fi
    fi
done
rm -rf %buildroot%_otplibdir/%name-%upstream_version/include/internal
mkdir -p %buildroot%_docdir/%name-%version/
cp -r EPL* README %buildroot%_docdir/%name-%version/
ln -sf %buildroot%_otplibdir/%name-%upstream_version/doc %buildroot%_docdir/%name-%version/doc
symlinks -rscd %buildroot%_docdir/%name-%version/


%files
%dir %_otplibdir/%name-*
%_otplibdir/%name-*
%exclude %_otplibdir/*/doc
%exclude %_otplibdir/*/include

%files devel
%dir %_otplibdir/*/include
%_otplibdir/*/include

%files doc
%dir %_otplibdir/*/doc
%_otplibdir/*/doc
%dir %_docdir/%name-*
%_docdir/%name-*

%changelog
* Sun Feb 19 2012 Sergey Shilov <hsv@altlinux.org> 0.9.9-alt2
- Version 0.9.9
- Build with Erlang R15B

* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.1
- Fixed build

* Thu Aug 04 2011 Sergey Shilov <hsv@altlinux.org> 0.9.7-alt1
- Version 0.9.7
- Build with Erlang R14B03

* Fri Apr 15 2011 Sergey Shilov <hsv@altlinux.org> 0.9.6.20110328-alt2
Fix post-install unowned files.

* Thu Apr 14 2011 Sergey Shilov <hsv@altlinux.org> 0.9.6.20110328-alt1
Initial build.


