%def_without direct_io

Name: fmio
Version: 2.0.8
Release: alt2.1

Summary: fmio, FM radio card manipulation utility
License: BSD
Group: Sound

Url: http://jumbo.narod.ru/fmio.html
Source0: http://jumbo.narod.ru/src/fmio/%name-%version.tar.gz
Source1: http://smile.org.ua/~andy/prj/patch/fmio-gq-wrapper.py
Source2: README.fedora
Patch0: fmio-2.0.8-build.asp.patch
Patch1: fmio-2.0.8-sysconfdir.asp.patch
Patch2: fmio-2.0.8-dyn.asp.patch
# Do not build drivers with direct I/O by default
# (https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=205721)
Patch3: fmio-2.0.8-nodirectio.patch

# Automatically added by buildreq on Sat Nov 06 2010
BuildRequires: libXext-devel libXpm-devel

ExclusiveArch: %ix86 x86_64

%description
The fmio is a small program to set and change fm radio card parameters.
It sets frequency, volume of the card, reports signal strength on the
working frequency and can set the radio card output to mono (if the card
driver supports it). Supports a lot of card types.

%package devel
Summary: Header files and libraries for developing apps which will use fmio
Group: Development/C
Requires: %name = %version

%description devel
The fmio-devel package contains libradio.a and radio.h needed
to develop programs that use fmio library.

Install the fmio-devel package if you want to develop applications
that will use the fmio library.

%package -n wmfmio
Summary: WindowMaker dockable application to manipulate FM radio card
Group: Graphical desktop/Window Maker
Requires: %name = %version-%release

%description -n wmfmio
wmfmio is a WindowMaker dockapp to manipulate FM radio card.

%prep
%setup
%patch0 -p1 -b .build
%patch1 -p1 -b .sysconfdir
%patch2 -p1 -b .dyn
%patch3 -p1 -b .nodirectio

# make LICENSE file
pushd utils
sh license.sh > ../LICENSE
popd

%build
export CFLAGS="-DSYSCONFDIR=\\\"%_sysconfdir\\\" $RPM_OPT_FLAGS -fPIC"
export LIBDIR="-L%_libdir"
%if_with direct_io
export WITH_DIRECT_IO=y
# FIXME: need proper build then, and proper install
%endif
%make_build

%install
%makeinstall
install -pDm755 %SOURCE1 %buildroot%_bindir/fmio-wrapper.py
install -pm644 %SOURCE2 README.fedora

%files
%_bindir/fmio
%if_with direct_io
%_bindir/bktrctl
%_bindir/fmrinit
%endif
%_bindir/fmio-wrapper.py
%_libdir/libradio.so
%_man1dir/fmio.1*
%doc Changelog doc/FAQ README
%doc LICENSE README.fedora
%lang(ru) %doc doc/FAQ.ru

%files devel
%_includedir/%name/

%files -n wmfmio
%_bindir/wmfmio
%_man1dir/wmfmio.1*
%config(noreplace) %_sysconfdir/wmfmiorc

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.8-alt2.1
- Rebuild with Python-2.7

* Sat Nov 06 2010 Michael Shigorin <mike@altlinux.org> 2.0.8-alt2
- refactored the package fedora one by Andy Shevchenko
  + added Andy's gq python wrapper (closes: #14166)
  + introduced wmfmio subpackage
  + disabled suid bit (see README.fedora)
  + conditional directio drivers build
  + shared library build
- buildreq
- NB: this package might benefit with a proper maintainer/upstream

* Mon Aug 23 2004 Fr. Br. George <george@altlinux.ru> 2.0.8-alt1
- Initial ALT Linux build

