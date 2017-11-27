Name: alsa-plugins-equal
Version: 0.6
Release: alt1

Summary: Real-time adjustable equalizer plugin for ALSA
License: GPLv2+
Group: Sound

URL: https://web.archive.org/web/20161105202833/http://thedigitalmachine.net/alsaequal.html
Source: alsaequal-%version.tar
Patch: %name-%version-%release.patch

Requires: %_libdir/ladspa/caps.so

# Automatically added by buildreq on Mon Nov 27 2017
BuildRequires: ladspa_sdk libalsa-devel

%description
Alsaequal is a real-time adjustable equalizer plugin for ALSA. It can be
adjusted using an ALSA compatible mixer, like alsamixergui or alsamixer.

This configuration (/etc/asound.conf or ~/.asoundrc) works fine for me:

ctl.equal {
    type equal;
}
pcm.plugequal {
    type equal;
    slave.pcm "plug:dmix";
}
pcm.!default {
    type plug;
    slave.pcm plugequal;
}

Adjust equalizer settings:
$ alsamixer -D equal

%prep
%setup -q -n alsaequal
%patch -p1

%if "%_libdir" != "/usr/lib"
sed -i~ 's|"/usr/lib/|"%_libdir/|g' *.c
%endif

%build
for m in ctl pcm; do
	gcc %optflags -fPIC -DPIC -shared -o libasound_module_${m}_equal.so \
		${m}_equal.c ladspa_utils.c -lasound -ldl -Wl,--no-undefined
done

%install
mkdir -p %buildroot%_libdir/alsa-lib
cp -pv *.so %buildroot%_libdir/alsa-lib

%files
%doc README
%_libdir/alsa-lib/*.so

%changelog
* Mon Nov 27 2017 Alexey Tourbin <at@altlinux.ru> 0.6-alt1
- initial revision
