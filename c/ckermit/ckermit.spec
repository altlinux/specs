%define archiv_name cku302
Name: ckermit
License: BSD-3-Clause
Group: System/Kernel and hardware
Summary: A Combined Serial and Network Communication Software Package
Provides: kermit
Version: 9.0.302
Release: alt1
Url: http://www.columbia.edu/kermit/
Source: %archiv_name.tar.gz
Source1: skel.kermrc
Patch0: cku302-fmt.diff
Patch1: cku211-prototypes.diff
Patch2: cku211-paths.diff
Patch3: cku302-return.diff
Patch4: cku211-EMrename.diff
Patch5: cku211-debug.diff
Patch6: cku211-uninitialized.diff
Patch7: cku211-string_comparison.diff
Packager: Boris Savelev <boris@altlinux.org>

# Automatically added by buildreq on Fri Jul 25 2008
BuildRequires: libncurses-devel libssl-devel zlib-devel libpam0-devel

%description
C-Kermit is a combined serial and network communication software
package offering a consistent, medium-independent, and cross-platform
approach to connection establishment, terminal sessions, file transfer,
character-set translation, and automation of communication tasks.

%prep
%setup -q -c -n %archiv_name
%patch0
%patch1
#%patch2
%patch3
#%patch5
%patch6
#%patch7

%build
%make linux+openssl+shadow KFLAGS="$RPM_OPT_FLAGS" \
    SSLLIB="-L%_libdir" SSLINC="-I%_includedir/openssl"
#    TERMCAPLIB="-L%_libdir/termcap"

%install
install -d -m 755 %buildroot/usr/bin
install -d -m 755 %buildroot%_man1dir
install -m 755 wermit %buildroot%_bindir/kermit
install -m 644 ckuker.nr %buildroot%_man1dir/kermit.1
install -D -m 644 %{S:1} %buildroot%_sysconfdir/skel/.kermrc

%files
%doc COPYING.TXT *.txt *.ini
%doc %_man1dir/*
%config(noreplace) %_sysconfdir/skel/.kermrc
%_bindir/*

%changelog
* Fri Jul 15 2016 Terechkov Evgenii <evg@altlinux.org> 9.0.302-alt1
- 9.0.302
- Patch4, Patch8 dropped (not needed anymore)
- Patch7 turned off (seems unneeded)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 8.0.211-alt1.1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 8.0.211-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 8.0.211-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Jul 25 2008 Boris Savelev <boris@altlinux.org> 8.0.211-alt1
- initial build from suse
