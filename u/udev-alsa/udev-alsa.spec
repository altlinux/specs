Name: udev-alsa
Version: 0.3
Release: alt2
Summary: The system sound initialization
License: GPL
Group: System/Base
Url: http://git.altlinux.org/people/shrek/packages/udev-alsa.git
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: udev
Obsoletes: rhsound sound-scripts
Provides: sound-scripts = 20091231:3.0-alt1

Source: %name-%version.tar
Patch: udev-alsa-0.3-alt-udev-187.patch

BuildRequires: libalsa-devel libudev-devel

%description
The %name package contains the udev rules used to setup sound devices

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--libexecdir=/lib/udev \
	--localstatedir=%_var
%make_build

%install
%make DESTDIR=%buildroot install

%pre
if [ -d %_localstatedir/hotplug ]; then
	rm -fr %_localstatedir/hotplug
fi

%triggerin -- sound-scripts
for i in $(seq 0 30); do
  if [ -f %_localstatedir/hal/asound/$i.state ]; then
    mv %_localstatedir/hal/asound/$i.state %_localstatedir/alsa/controlC$i >/dev/null 2>&1
  fi
done

%files
/lib/udev/alsa-control
/lib/udev/rules.d/*.rules
%_prefix/libexec/ConsoleKit/run-seat.d/alsa-control.ck
%dir %_localstatedir/alsa
%ghost %_localstatedir/alsa/controlC*

%changelog
* Wed Mar 01 2017 Anton Midyukov <antohami@altlinux.org> 0.3-alt2
- remove requires ConsoleKit (no needed)

* Sun Dec 30 2012 L.A. Kostis <lakostis@altlinux.ru> 0.3-alt1.2
- NMU:
  + sync with alsactl from 1.0.26.

* Mon Jul 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.1
- Fixed build

* Thu Mar 31 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.3-alt1
- 0.3

* Sun Oct 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt3
- udev rules: fixed typo

* Mon Jan 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt2
- rewrited triggerin

* Sat Jan 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2-alt1
- 0.2

* Thu Dec 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1-alt1
- initial release

