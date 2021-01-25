BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           love
Version:        11.3
Release:        alt1_1
Summary:        A free 2D game engine which enables easy game creation in Lua
Group:          Development/Other
License:        zlib
Url:            https://love2d.org
Source0:        https://github.com/love2d/love/releases/download/%{version}/%{name}-%{version}-linux-src.tar.gz

BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
Source44: import.info

%description
LA.VE is an open source, cross platform 2D game engine which uses the
Lua scripting language. LA.VE can be used to make games of any license
allowing it to be used for both free and non-free projects.

%files
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-%{name}-game.svg
%{_libdir}/lib%{name}-%{version}.so
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q


%build
%configure --bindir=%{_gamesbindir} \
               --with-lua=luajit \
               --enable-gme \
               --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_libdir}/lib%{name}.so
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/games,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done


%changelog
* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 11.3-alt1_1
- update by mgaimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 11.2-alt1_2
- update by mgaimport

* Thu Feb 14 2019 Ivan Razzhivin <underwit@altlinux.org> 11.1-alt1_3
- GCC8 fix

* Thu Jan 03 2019 Igor Vlasenko <viy@altlinux.ru> 11.1-alt1_2
- resurrected as mageia import

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 0.10.2-alt1
- Autobuild version bump to 0.10.2

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.10.1-alt1
- Autobuild version bump to 0.10.1

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.9.2-alt3
- Fix build

* Tue Aug 11 2015 Fr. Br. George <george@altlinux.ru> 0.9.2-alt2
- Re-release with fixes

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 0.9.2-alt1
- Autobuild version bump to 0.9.2

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 0.9.1-alt1
- Autobuild version bump to 0.9.1

* Mon Feb 24 2014 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1
- Autobuild version bump to 0.9.0
- Fix buildreq (introducing chrpath hack)

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Autobuild version bump to 0.8.0
- Fix build

* Fri Sep 02 2011 Fr. Br. George <george@altlinux.ru> 0.7.2-alt1
- Initial build from scratch

