%define sover 5
Name: libotr%sover
Version: 4.1.1
Release: alt2

Group: System/Libraries
Summary: Off-The-Record Messaging library and toolkit
# SrcLicense: LGPL-2.1-only and GPL-2.0-only
License: LGPL-2.1-only
Url: https://otr.cypherpunks.ca/

# Repacked https://www.cypherpunks.ca/otr/libotr-%version.tar.gz
Source0: libotr-%version.tar
Patch0: libotr-4.1.1-debian-fix-include-socket.h.patch

# Automatically added by buildreq on Wed Mar 09 2016
# optimized out: gnu-config libgpg-error libgpg-error-devel
BuildRequires: libgcrypt-devel

BuildPreReq: libgcrypt-devel >= 1.2.0

# unit/test_privkey requires /proc
%{?!_without_check:%{?!_disable_check:BuildPreReq: /proc perl-devel}}

%description
%name is a library and toolkit which implements Off-the-Record (OTR)
Messaging.

OTR allows you to have private conversations over IM by providing:
 - Encryption
   - No one else can read your instant messages.
 - Authentication
   - You are assured the correspondent is who you think it is.
 - Deniability
   - The messages you send do _not_ have digital signatures that are
     checkable by a third party.  Anyone can forge messages after a
     conversation to make them look like they came from you.  However,
     _during_ a conversation, your correspondent is assured the messages
     he sees are authentic and unmodified.
 - Perfect forward secrecy
   - If you lose control of your private keys, no previous conversation
     is compromised.

%package -n libotr-devel
Summary: Development related files of %name
Group: Development/C
License: LGPL-2.1-only
Requires: %name = %version-%release
Requires: libgcrypt-devel
Provides: libotr5-devel = %EVR
Conflicts: libotr2-devel

%description -n libotr-devel
%name is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains development related files of %name.

%package -n libotr-utils
Summary: Helper utilities of %name
Group: Networking/Instant messaging
License: GPL-2.0-only
Requires: %name = %version-%release
Provides: libotr5-utils = %EVR

%description -n libotr-utils
%name is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains various helper utilities from %name.

%prep
%setup -q -n libotr-%version

%patch -p1

# This test is unstable.
sed '/random-msg-disconnect-frag-auth.sh$/d' -i tests/test_list

%build
%configure \
    --disable-static \
    --enable-shared \
    --with-pic \
    --disable-rpath
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make install DESTDIR=%buildroot

%check
LD_LIBRARY_PATH=$PWD/src/.libs %make check ||:

%files -n %name
%doc AUTHORS
%_libdir/lib*.so.*

%files -n libotr-devel
%doc ChangeLog INSTALL Protocol-v3.html NEWS README
%_datadir/aclocal/*.m4
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%files -n libotr-utils
%doc AUTHORS
%_bindir/*
%_man1dir/*

%changelog
* Sat Nov 12 2022 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.1.1-alt2
- Applied patch from Debian (thx Rhonda D'Vine) to fix FTBFS with
  libgcrypt >= 1.10.0.
- Fixed License: tags.

* Thu Jan 10 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.1.1-alt1.2
- Fixed testsuite:
  + added BR: /proc to fix test;
  + disabled unstable test.

* Thu Mar 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.1.1-alt1.1
- Rebuilt to fix requires.

* Wed Mar 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.1.1-alt1
- Updated to 4.1.1 (fixes CVE-2016-2851).

* Thu Jun 25 2015 Sergey V Turchin <zerg@altlinux.org> 4.1.0-alt2.1
- Rebuild with new libgcrypt

* Mon Jan 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.1.0-alt2
- Renamed {devel,utils} subpackages to libotr-{devel,utils}.

* Tue Oct 21 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.1.0-alt1
- New version.

* Tue Nov 12 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.0-alt1
- New version.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.2.0-alt3.1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt3.1
- Removed bad RPATH

* Tue Dec 07 2010 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt3
- rebuilt

* Fri Jan 30 2009 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt2
- fix requires

* Thu Jan 29 2009 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- initial specfile

