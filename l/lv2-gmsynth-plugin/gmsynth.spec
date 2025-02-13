Name: lv2-gmsynth-plugin
Version: 0.6.2
Release: alt1

Summary: General MIDI Sample Player Plugin
License: GPLv2
Group: Sound
Url: https://github.com/x42/gmsynth.lv2

Source: %name-%version-%release.tar

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(lv2)

%description
%summary
gmsynth serves as one of default MIDI auditioners in Ardour

%prep
%setup

%build
make CFLAGS='%optflags' STRIP=: gmsynth_VERSION=%version \
%ifarch %ix86 x86_64
        OPTIMIZATIONS='-msse -msse2 -mfpmath=sse -ffast-math'
%endif

%install
make install DESTDIR=%buildroot LV2DIR=%_libdir/lv2
cp -pv sf2/README README.sf2

%files
%doc COPYING README.* sf2/CHANGELOG*
%_libdir/lv2/*

%changelog
* Thu Feb 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.2-alt1
- 0.6.2 released

* Sun Jan 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.1-alt1
- 0.6.1 released

* Fri Feb  9 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- initial
