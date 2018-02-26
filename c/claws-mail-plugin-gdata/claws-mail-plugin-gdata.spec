%define _name gdata
%define _name2 gdata_plugin

Name: claws-mail-plugin-%_name
Version: 0.4
Release: alt1

Summary: Access to GData (Google services) for Claws Mail
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
BuildRequires: libgdata-devel

%description
Access to GData (Google services) for Claws Mail.
The only currently implemented feature is inclusion of
Google contacts into the address completion.

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
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Updated to 0.4.

* Wed Mar 07 2012 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Initial build.

