Name: pidgin-otr
Version: 4.0.2
Release: alt1.1
License: GPLv2
Group: Networking/Instant messaging
Url: http://otr.cypherpunks.ca/
Summary: Off-The-Record Messaging plugin for Pidgin
Source: http://otr.cypherpunks.ca/%name-%version.tar.gz

Requires: pidgin
BuildRequires: glib2-devel gtk2-devel libgcrypt-devel >= 1.2.0
BuildRequires: libgpg-error-devel libotr5-devel
BuildRequires: pidgin-devel perl-XML-Parser intltool

%description
This is a Pidgin plugin which implements Off-the-Record (OTR) Messaging.
It is known to work (at least) under the Linux and Windows versions of
Pidgin.

%prep
%setup
sed -i '/^AM_INIT_AUTOMAKE.*$/{s/-Werror//}' configure.ac
%autoreconf

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README COPYING
%_libdir/pidgin/pidgin-otr.so

%changelog
* Thu Mar 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.2-alt1.1
- Rebuilt to fix requires.

* Wed Mar 09 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.2-alt1
- Updated to 4.0.2.

* Tue Oct 21 2014 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.1-alt1
- New version.

* Sun Nov 03 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.0-alt1
- Initial build.
