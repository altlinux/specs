%def_enable devel
%def_disable utils

%define libname libotr2
Name: libotr
Version: 3.2.1
Release: alt2.qa1

Group: System/Legacy libraries
Summary: Off-The-Record Messaging library and toolkit
License: LGPL/GPL
Url: http://www.cypherpunks.ca/otr/

Source0: http://www.cypherpunks.ca/otr/%name-%version.tar.gz
Packager: Sergey V Turchin <zerg@altlinux.org>

BuildRequires: libgcrypt-devel >= 1.2.0

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

%package -n %libname
Summary: Off-The-Record Messaging library and toolkit
Group: Networking/Instant messaging
License: LGPL
Provides: %name = %version-%release

%description -n %libname
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

%package -n %libname-devel
Summary: Development related files of %name
Group: Development/C
License: LGPL
Requires: %libname = %version-%release
Requires: libgcrypt-devel

%description -n %libname-devel
%name is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains development related files of %name.

%package -n %libname-utils
Summary: Helper utilities of %name
Group: Networking/Instant messaging
License: GPL
Requires: %libname = %version-%release

%description -n %libname-utils
%name is a library and toolkit which implements Off-the-Record (OTR)
Messaging. This package contains various helper utilities from %name.

%prep
%setup -q

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


%files -n %libname
%doc AUTHORS
%_libdir/lib*.so.*

%if_enabled devel
%files -n %libname-devel
%doc ChangeLog INSTALL Protocol-v2.html NEWS README
%_datadir/aclocal/*.m4
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%endif

%if_enabled utils
%files utils
%doc AUTHORS
%_bindir/*
%_man1dir/*
%endif

%changelog
* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.2.1-alt2.qa1
- NMU: rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Mon Jan 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.1-alt2
- Renamed devel subpackage.
- Disabled utils subpackage.

* Tue Nov 12 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.2.1-alt1
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

