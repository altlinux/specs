Name: dvorak7min
Version: 1.6.1
Release: alt1

Summary: Typing tutor for dvorak keyboards

License: GPLv2+
Group: Games/Other
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: dvorak7min_1.6.1.orig.tar
# debian patch
Patch: dvorak7min_1.6.1-9.diff.gz

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: libncurses-devel

%description
dvorak7min is a typing tutor to help you learn dvorak.

%prep
%setup
%patch0 -p1

%build
%make_build PROF="%optflags"

%install
mkdir -p %buildroot%_bindir
cp -p %name %buildroot%_bindir

%files
%doc ChangeLog COPYING README
%_bindir/%name

%changelog
* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- initial build for ALT Linux Sisyphus
- drop precompiled binaries, use optflags

* Fri Oct 17 2008 Nicolas Vigier <nvigier@mandriva.com> 1.6.1-1mdv2009.1
+ Revision: 294734
- import dvorak7min

