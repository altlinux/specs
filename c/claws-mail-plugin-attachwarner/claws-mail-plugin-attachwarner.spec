%define _name attachwarner

Name: claws-mail-plugin-%_name
Version: 0.2.24
Release: alt1

Summary: Warn when the user is likely to have forgotten to attach a file.
License: %gpl3plus
Group: Networking/Mail

Url: http://www.claws-mail.org/plugin.php?plugin=%_name

Source: %_name-%version.tar

# The macro is defined inside claws-mail-devel.
# FIXME: Generally, this is bad. Each Claws Mail release causes to rebuild
# each and every plugin for it. Does it really matter so much?
Requires: claws-mail = %_claws_version

BuildRequires(pre): rpm-build-licenses claws-mail-devel

# From configure.ac
BuildPreReq: glib2-devel >= 2.6
BuildPreReq: libgtk+2-devel >= 2.6

%description
The AttachWarner verifies that you have attached something to your email if
you mentioned attachment in the email's body.

%prep
%setup -q -n %_name-%version

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%_libdir/claws-mail/plugins/%_name.so

%exclude %_libdir/*/*/*.la

%changelog
* Fri Jun 29 2012 Mikhail Efremov <sem@altlinux.org> 0.2.24-alt1
- Updated to 0.2.24.

* Wed Jan 18 2012 Mikhail Efremov <sem@altlinux.org> 0.2.23-alt1
- Updated to 0.2.23.

* Fri Sep 02 2011 Mikhail Efremov <sem@altlinux.org> 0.2.22-alt1
- Updated to 0.2.22.

* Tue May 03 2011 Mikhail Efremov <sem@altlinux.org> 0.2.21-alt1
- Minor spec cleanup, sources: tar.bz2 -> tar.
- Updated to 0.2.21.

* Thu Dec 30 2010 Mikhail Efremov <sem@altlinux.org> 0.2.20-alt2
- rebuild for claws-mail 3.7.7

* Mon Nov 29 2010 Mikhail Efremov <sem@altlinux.org> 0.2.20-alt1
- Updated to 0.2.20

* Tue Aug 24 2010 Mikhail Efremov <sem@altlinux.org> 0.2.19-alt1
- New version.

* Sat Jan 16 2010 Alexey Rusakov <ktirf@altlinux.org> 0.2.18-alt1
- New version.

* Wed Jul 08 2009 Alexey Rusakov <ktirf@altlinux.org> 0.2.17-alt1
- New version 0.2.17 (with rpmrb script).

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 0.2.16-alt1
- New version (0.2.16).
- Removed no more necessary libgnutls-devel dependency, it's now
  a dependency of claws-mail-devel.

* Thu Oct 16 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.14-alt1
- New version (0.2.14).
- No more dependency on libssl-devel, Claws Mail uses gnutls from now on.

* Mon May 26 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.12-alt2
- Rebuild for the updated Claws Mail.

* Tue Apr 29 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.12-alt1
- New version (0.2.12).

* Sat Apr 12 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.11-alt2
- Build with updated Claws Mail.

* Mon Mar 24 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.11-alt1
- New version (0.2.11).

* Mon Jan 14 2008 Alexey Rusakov <ktirf@altlinux.org> 0.2.10-alt1
- new version (0.2.10)

* Tue Nov 27 2007 Alexey Rusakov <ktirf@altlinux.org> 0.2.9-alt1
- Initial Sisyphus version

