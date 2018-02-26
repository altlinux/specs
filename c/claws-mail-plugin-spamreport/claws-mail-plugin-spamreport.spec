%define _name spamreport
%define _name2 spam_report

Name: claws-mail-plugin-%_name
Version: 0.3.16
Release: alt1

Summary: This plugin reports spam to various places.
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
BuildPreReq: libcurl-devel

%description
This Claws Mail plugin allows you to upload your spams to various spam
reporting places, like http://www.signal-spam.fr/ or http://www.spamcop.net/.

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
%_libdir/claws-mail/plugins/%_name.so

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.3.16-alt1
- Updated to 0.3.16.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.3.15-alt1
- Updated to 0.3.15.

* Tue Dec 13 2011 Mikhail Efremov <sem@altlinux.org> 0.3.14-alt1
- Initial build.
