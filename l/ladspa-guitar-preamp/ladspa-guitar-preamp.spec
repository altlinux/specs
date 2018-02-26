Name: ladspa-guitar-preamp
Version: 1.0
Release: alt1.1
Summary: LADSPA plugin to simulate guitar preamp
Summary(ru_RU.KOI8-R): Плагин LADSPA для иммитации гитарного предусилителя
License: GPL
Group: Sound
Url: http://quitte.de/dsp/
Packager: Mikhail Yakshin <greycat@altlinux.ru>
Source0: preamp.tar.gz
Patch: ladspa-guitar-preamp-options.patch.gz

# Automatically added by buildreq on Tue Sep 30 2003
BuildRequires: ladspa_sdk

%description
These LADSPA plugins, accompanied by some blurbs about motivation and
approach, mostly centered around (but not in the least confined to)
digital guitarist needs.

'preamp' performs approximated tone coloring and hard clipping of an
instrument amplifier's preamp stage (Fender 5F4 type).

%description -l ru_RU.KOI8-R
Эти плагины LADSPA в основном предназначены для нужд цифрового
гитариста (но отнюдь не ограничены ими).

'preamp' придает звуку примерную тембровую окраску и жесткое искажение
гитарного предусилителя (типа Fender 5F4).

%prep
%setup -n preamp
%patch -p1

%build
%add_optflags %optflags_shared
export CFLAGS="%optflags"
%make_build

%install
%__install -D -m644 preamp.so %buildroot%_ladspa_path/preamp.so

%files
%_ladspa_path/*.so

%changelog
* Mon Dec 22 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1.1
- Fixed text relocations

* Tue Sep 30 2003 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1
- Initial build for Sisyphus
