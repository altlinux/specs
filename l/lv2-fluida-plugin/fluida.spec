Name: lv2-fluida-plugin
Version: 0.9.2
Release: alt2

Summary: Fluidsynth as LV2 plugin
License: GPLv2
Group: Sound

Url: https://github.com/brummer10/Fluida.lv2

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(lv2)
BuildRequires: xxd


%description
%summary

%prep
%setup

%build
make CFLAGS='%optflags' CXXFLAGS='%optflags'

%install
make install INSTALL_DIR=%buildroot%_libdir/lv2

%files
%doc LICENSE README*
%_libdir/lv2/Fluida.lv2

%changelog
* Thu Jan 25 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt2
- ftbfs fixed by adding workaround for broken xxd

* Tue Jan 16 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1
- 0.9.2 released

* Thu Jan  4 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt1
- initial
