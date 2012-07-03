
Name: lingot
Version: 0.9.0
Release: alt2

Summary: LINGOT Is Not a Guitar-Only Tuner
License: GPLv2+
Group: Sound
Url: http://lingot.nongnu.org/

BuildRequires: libjack-devel libalsa-devel
BuildRequires: intltool libgtk+2-devel libglade-devel

Packager: Ivan A. Melnikov <iv@altlinux.org>
Source: %name-%version.tar
Patch0: lingot-0.9.0-hg-749df5080742-fix-jack.patch
Patch1: lingot-0.9.0-alt-desktop-category.patch

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and
highly configurable. Originally conceived to tune electric guitars, it
can now be used to tune other instruments.

It looks like an analogue tuner, with a gauge indicating the relative
shift to a certain note, found automatically as the closest note to the
estimated frequency.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm -rf %buildroot/%_defaultdocdir/%name
%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_desktopdir/*.desktop
%_pixmapsdir/%{name}*
%doc AUTHORS ChangeLog MAINTAINERS NEWS README THANKS TODO


%changelog
* Sat Apr 16 2011 Ivan A. Melnikov <iv@altlinux.org> 0.9.0-alt2
- Import commit 749df5080742 from upstream hg to fix compatibility
  with recent jack;
- Improved categories in desktop file.

* Tue Feb 22 2011 Ivan A. Melnikov <iv@altlinux.org> 0.9.0-alt1
- New version.

* Sat Dec 04 2010 Ivan A. Melnikov <iv@altlinux.org> 0.8.1-alt1
- Initial build for ALTLinux.

