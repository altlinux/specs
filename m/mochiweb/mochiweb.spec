%def_disable debug

%define upstream_version 1.5.2
%define gitdate 20110728

Name: mochiweb
Version: %upstream_version.%gitdate
Release: alt1
Summary: Erlang library for building lightweight HTTP servers.
License: %mit
Group: Development/Erlang
URL: https://github.com/mochi/mochiweb
Source: %name-%version.tar
Packager: Sergey Shilov <hsv@altlinux.org>
BuildArch: noarch
Requires: erlang-otp

BuildRequires(pre): rpm-build-erlang rpm-build-licenses
BuildRequires: erlang-otp-devel rebar symlinks

%description
MochiWeb is an Erlang library for building lightweight HTTP servers.

%package devel
Summary: Headers for %name modules
Group: Development/Erlang
Requires: %name = %version-%release

%description devel
Headers for %name library modules.


%prep
%setup -n  %name-%version

%build
%make

%install
mkdir -p %buildroot%_otplibdir/%name-%upstream_version
cp -rf ebin examples include scripts support %buildroot%_otplibdir/%name-%upstream_version/
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
cp -r LICENSE README %buildroot%_docdir/%name-%version/
ln -sf %buildroot%_otplibdir/%name-%upstream_version/examples %buildroot%_docdir/%name-%version/examples
ln -sf %buildroot%_otplibdir/%name-%upstream_version/scripts %buildroot%_docdir/%name-%version/scripts
ln -sf %buildroot%_otplibdir/%name-%upstream_version/support %buildroot%_docdir/%name-%version/support
cp -rf Makefile rebar.config %buildroot%_docdir/%name-%version/
symlinks -rscd %buildroot%_docdir/%name-%version/


%files
%dir %_otplibdir/%name-%upstream_version
%_otplibdir/%name-%upstream_version/ebin
%dir %_docdir/%name-%version
%_docdir/%name-%version

%files devel
%_otplibdir/%name-%upstream_version/*
%exclude %_otplibdir/%name-%upstream_version/ebin


%changelog
* Thu Aug 04 2011 Sergey Shilov <hsv@altlinux.org> 1.5.2.20110728-alt1
- Version upstream from git 2011-07-28
- rebuild with Erlang R14B03

* Sun Apr 17 2011 Sergey Shilov <hsv@altlinux.org> 1.5.2.20110413-alt1
Initial build.



