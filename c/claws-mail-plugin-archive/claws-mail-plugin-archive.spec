%define _name archive

Name: claws-mail-plugin-%_name
Version: 0.6.12
Release: alt1

Summary: Mail archiving functionality for Claws Mail
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugins.php

Source: %_name-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

# From configure.ac
BuildPreReq: glib2-devel >= 2.6
BuildPreReq: libgtk+2-devel >= 2.6
BuildPreReq: libarchive-devel

%description
This plugin adds archiving features to Claws Mail.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_libdir/claws-mail/plugins/%_name.so

%exclude %_libdir/*/*/*.la
%exclude %_includedir/claws-mail/plugins/archive/*.h

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.6.12-alt1
- Updated to 0.6.12.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.6.11-alt1
- Updated to 0.6.11.
- Fix summary.

* Tue Sep 06 2011 Mikhail Efremov <sem@altlinux.org> 0.6.10-alt1
- Initial build.
