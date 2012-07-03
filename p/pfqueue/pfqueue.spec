%def_without standalone

Name: pfqueue
Version: 0.5.6
Release: alt2

Summary: Queue Scanner and Frontend for Postfix and Exim
License: GPL
Group: Networking/Mail

Url: http://pfqueue.sourceforge.net
Source: %name-%version.tar
Packager: Vladimir V Kamarzin <vvk@altlinux.ru>

Requires: libpfq = %version-%release

# Automatically added by buildreq on Thu Feb 02 2006
BuildRequires: gcc-c++ libncurses-devel libstdc++-devel libtinfo-devel

%description
pfqueue is an effort to give postqueue/mailq/postsuper/exim4 a console
(ncurses) interface: it won't add any particular functionality to those
provided with MTAs themselves, but will hopefully make them easier to use.

It's a real-time queue scanner, that shows per-queue lists of existing
messages; the messages can be shown, deleted, put on hold, released or
requeued

%package -n libpfq
Summary: %name library
Group: System/Libraries

%description -n libpfq
%summary

%if_with standalone
%package server-standalone
Summary: %name standalone server
Group: System/Servers
Requires: libpfq = %version-%release

%description server-standalone
%summary
%endif standalone

%prep
%setup
autoreconf -fisv

%configure --disable-static

%build
%make

%install
%makeinstall

rm -f "%buildroot%_libdir/libpfqueue.la"
chmod 0644 NEWS README AUTHORS

%files
%_bindir/%name
%_man1dir/%name.1*
%_man5dir/%name.conf.5*
%doc AUTHORS ChangeLog NEWS README TODO

%if_with standalone
%files server-standalone
%_bindir/spfqueue
%endif standalone

%files -n libpfq
%_libdir/libpfq_*.so
%_libdir/libpfq_*.so.*
%_libdir/libpfqueue.so.*
%_libdir/libpfqueue.so

%changelog
* Tue Dec 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.5.6-alt2
- Remove obsolete %%post_ldconfig/%%postun_ldconfig calls
- Minor spec cleanup
- Drop manual dependency on ncurses

* Fri Apr 06 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.6-alt1
- Updated to 0.5.6
- Don't build standalone-server. It's broken.

* Tue Feb 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.2-alt1
- 0.5.2
- Minor spec changes

* Mon Feb 06 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.1-alt2
- Corrected internal requires, added forgotten %%post{un}_ldconfig

* Thu Feb 02 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 0.5.1-alt1
- Initial build for Sisyphus (adopted spec from Pascal Bleser <guru at
  unixtech.be>)
