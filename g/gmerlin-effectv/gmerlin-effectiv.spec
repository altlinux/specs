Name: gmerlin-effectv
Version: 1.1.2
Release: alt1
Summary: This package contains most effects from EffecTV for gmerlin

Group: Sound
License: GPL
Url: http://gmerlin.sourceforge.net/
Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar.gz
Patch0: %name-%version-autotools.patch

# Automatically added by buildreq on Sun Apr 25 2010
BuildRequires: cvs libgmerlin-devel

%description
This package contains most effects from EffecTV ported to gmerlin
(see http://effectc.sourceforge.net)

Missing Effects are mostly the ones, which do things, which cannot
be done within a generic filter API.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/gmerlin/plugins/*.la

%files -f %name.lang
%doc ChangeLog COPYING README
%dir %_libdir/gmerlin/plugins
%_libdir/gmerlin/plugins/*.so

%changelog
* Sun Apr 25 2010 Hihin Ruslan <ruslandh@altlinux.ru> 1.1.2-alt1
- initial build for ALT Linux Sisyphus

