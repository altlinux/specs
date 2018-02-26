%define _name addresskeeper
%define _name2 address_keeper

Name: claws-mail-plugin-%_name
Version: 1.0.6
Release: alt1

Summary: Keeps all recipient addresses in an addressbook folder.
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugins.php

Source: %_name2-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

# From configure.ac
BuildPreReq: glib2-devel >= 2.6
BuildPreReq: libgtk+2-devel >= 2.6

%description
This plugin allows saving outgoing addresses to a designated folder
in the address book. Addresses are saved only if not found in the
address book to avoid unwanted duplicates.
Selecting which headers are scanned for keeping addresses is also
supported (Any or several of 'To', 'Cc' or 'Bcc').

%prep
%setup -n %_name2-%version

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std
%find_lang %_name2

%files -f %_name2.lang
%_libdir/claws-mail/plugins/%_name2.so

%exclude %_libdir/*/*/*.la

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 1.0.6-alt1
- Updated to 1.0.6.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1
- Updated to 1.0.5.

* Tue Sep 06 2011 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1
- Initial build.

