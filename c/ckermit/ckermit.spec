%define archiv_name cku211
Name: ckermit
License: Artistic License
Group: System/Kernel and hardware
Summary: A Combined Serial and Network Communication Software Package
Provides: kermit
Version: 8.0.211
Release: alt1.1.1
Url: http://www.columbia.edu/kermit/
Source: %archiv_name.tar.bz2
Source1: skel.kermrc
Patch: %archiv_name-fmt.diff
Patch1: %archiv_name-prototypes.diff
Patch2: %archiv_name-paths.diff
Patch3: %archiv_name-return.diff
Patch4: %archiv_name-EMrename.diff
Patch5: %archiv_name-debug.diff
Patch6: %archiv_name-uninitialized.diff
Patch7: %archiv_name-string_comparison.diff
Patch8: %archiv_name-strncat.diff
Packager: Boris Savelev <boris@altlinux.org>

# Automatically added by buildreq on Fri Jul 25 2008
BuildRequires: libncurses-devel libssl-devel

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
%patch4
#%patch5
%patch6
%patch7
%patch8

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
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 8.0.211-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 8.0.211-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Fri Jul 25 2008 Boris Savelev <boris@altlinux.org> 8.0.211-alt1
- initial build from suse
