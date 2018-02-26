Name: yaws
Version: 1.92
Release: alt1
Packager: Sergey Shilov <hsv@altlinux.org>
Group: System/Servers
License: BSD
Url: http://yaws.hyber.org/

Provides: %name = %version-%release

Requires: %name-dyncontent-example %name-doc-pdf

BuildRequires: erlang-devel erlang-otp-devel libpam-devel
BuildRequires: latex2html texlive-latex-recommended

Source0: %name-%version.tar.gz
Source1: yaws.init.d
Source2: yaws.conf


Summary: Yaws webserver virtual package

%description
Yaws - virtual package
to easy select yaws packages during install.


%package server
Summary: A high performance HTTP 1.1 webserver
Group: System/Servers
BuildArch: noarch
Requires: erlang-otp
Requires: %name-drivers
Provides: %name-server = %version-%release

%description server
Yaws is a HTTP high perfomance 1.1 webserver particularly
well suited for dynamic-content webapplications. Two separate
modes of operations are supported.

* Standalone mode where Yaws runs as a regular webserver daemon.
  This is the default mode.
* Embedded mode where Yaws runs as an embedded webserver in another
  erlang application


%package drivers
Summary: Yaws Erlang drivers
Group: System/Servers
Requires: %name-server = %version-%release

%description drivers
Platform depended Erlang drivers binaries

%package  dyncontent-example
Summary: Yaws online manual as dynamic-content example
Group: Development/Documentation
BuildArch: noarch
Requires: %name-server = %version-%release

%description dyncontent-example
The package contains Yaws online manual designed in dynamic-content *.yaws format.
After install Content is accessable by URL http://$HOST:8888 ( see /etc/yaws/yaws.conf for details ).


%package doc-pdf
Summary: Documentation for Yaws HTTP webserver in PDF format
Group: Development/Documentation
BuildArch: noarch
Requires: %name-server = %version-%release

%description doc-pdf
The package contains a Claes Wikstroms - "Yaws - Yet Another Web Server" Book in PDF format.
This Book is a part of official Yaws sources from http://yaws.hyber.org/


%prep
%setup -q
install -p -m755 %_sourcedir/yaws.init.d .
install -p -m644 %_sourcedir/yaws.conf .

%build
# Server
%autoreconf -f
export CFLAGS="-fno-strict-aliasing"
export CXXFLAGS="-fno-strict-aliasing"
%configure \
    --with-ssl=%prefix \
    --with-defaultcharset=UTF-8 \
    --localstatedir=%_localstatedir
%__make  BINDIR=%_bindir LIBDIR=%_libexecdir 
# Documetation
%__make BINDIR=%_bindir LIBDIR=%_libdir docs

%install
%makeinstall BINDIR=%_bindir LIBDIR=%_libexecdir  INSTALL_PREFIX=%buildroot DESTDIR=%buildroot
# Remove not needed (created by makeinstall) dirs
%__rm -Rf %buildroot/%_sysconfdir/init.d
%__rm -Rf %buildroot/usr/etc
%__rm -Rf %buildroot/%_var/lib/log
%__rm -Rf %buildroot/%_libexecdir/pkgconfig
%__mkdir_p %buildroot/%_initrddir
%__install -m755 yaws.init.d %buildroot/%_initrddir/%name
%__install -m640 yaws.conf %buildroot/%_sysconfdir/%name
%__mkdir_p %buildroot/%_docdir/%name-%version
%__install -m644 README ChangeLog %buildroot/%_docdir/%name-%version
%__mv -f %buildroot/%_docdir/%name/* %buildroot/%_docdir/%name-%version
%__rm -rf %buildroot/%_docdir/%name
%__mkdir_p %buildroot/%_localstatedir/%name/dyncontent-example
%__mv -f %buildroot/%_localstatedir/%name/www/* %buildroot/%_localstatedir/%name/dyncontent-example
# Create default log dir
%__mkdir_p %buildroot/%_logdir/%name

%post  server
%post_service %name

%preun server 
%preun_service %name
%__rm -f %_logdir/%name/*

%post dyncontent-example
# Add dyncontent-example section to Yaws config  if it NOT exists
egrep -q '/var/lib/yaws/dyncontent-example' %_sysconfdir/%name/yaws.conf ||
echo "
<server $HOSTNAME >
        port = 8888
        listen = 0.0.0.0
        docroot = /var/lib/yaws/dyncontent-example
        appmods = <cgi-bin, yaws_appmod_cgi>
</server>
">>%_sysconfdir/%name/yaws.conf

%postun dyncontent-example
# Delete dyncontent-example section from config
RR=`cat %_sysconfdir/%name/yaws.conf | \
    egrep -n '<server|\/var\/lib\/yaws\/dyncontent-example|server>' | \
    egrep -B1 -A1 '\/var\/lib\/yaws\/dyncontent-example' | \
    awk -F: '{ print $1 }' | xargs echo | awk '{ ORS="," ; print $1 ; ORS="" ; print $3 }'`
[ $RR == "," ] || sed -i -e "$RR d " %_sysconfdir/%name/yaws.conf


%files

%files server
%dir %_sysconfdir/%name
%dir %_libexecdir/%name
%dir %_localstatedir/%name
%dir %_logdir/%name
%dir %_docdir/%name-%version
%_bindir/*
%config(noreplace) %_sysconfdir/%name/*
%_initrddir/%name
%_libexecdir/%name/*
%exclude %_libexecdir/%name/priv/lib/*
%_localstatedir/%name/ebin
%_localstatedir/%name/www
%_man1dir/*
%_man5dir/*
%_docdir/%name-%version/README
%_docdir/%name-%version/ChangeLog

%files drivers
%_libexecdir/%name/priv/lib/*

%files doc-pdf
%_docdir/%name-%version/%name.pdf

%files dyncontent-example
%dir %_localstatedir/%name/dyncontent-example
%_localstatedir/%name/dyncontent-example/*

%changelog
* Tue Mar 13 2012 Sergey Shilov <hsv@altlinux.org> 1.92-alt1
- 1.92 (ALT #26972)
- rebuild with Erlang R15B

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.89-alt2.1
- Rebuild with Python-2.7

* Fri Mar 18 2011 Sergey Shilov <hsv@altlinux.org> 1.89-alt2
- rebuild with Erlang R14B02;
- fix TeTeX obsolete dependencies.

* Tue Feb 22 2011 Sergey Shilov <hsv@altlinux.org> 1.89-alt1
- 1.89.

* Mon Apr 26 2010 Sergey Shilov <hsv@altlinux.org> 1.88-alt5
- fix "Macro %%s not found" warning;
- fix repocop altlinux-policy-tex-buildreq-tetex warning.

* Fri Apr 23 2010 Sergey Shilov <hsv@altlinux.org> 1.88-alt4.1
- fix tag ... is not inherited from /gears/y/yaws.git after nmu

* Thu Apr 22 2010 Sergey Shilov <hsv@altlinux.org> 1.88-alt4
- fix build tags.

* Thu Apr 22 2010 Sergey Shilov <hsv@altlinux.org> 1.88-alt3
- fix post-install unowned files

* Thu Apr 22 2010 Sergey Shilov <hsv@altlinux.org> 1.88-alt2
- fix set_gc_flags() error on set of GC_USE_OLD_SSL value.

* Wed Apr 07 2010 Sergey Shilov <hsv@altlinux.org> 1.88-alt1
- 1.88.

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.84-alt2.1
- Rebuilt with python 2.6

* Thu Jul 30 2009 Sergey Shilov <hsv@altlinux.org> 1.84-alt2
- fix x86_64 build.

* Tue Jul 28 2009 Sergey Shilov <hsv@altlinux.org> 1.84-alt1
- initial build.


