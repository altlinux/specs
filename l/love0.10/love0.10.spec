# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name love0.10
%define uname   love
%define api     0.10

%define major     0
%define libname   lib%{name}%{major}
%define develname lib%{name}-devel

Name:           love0.10
Version:        0.10.2
Release:        alt1_1
Summary:        A free 2D game engine which enables easy game creation in Lua
Group:          Development/Other
# All is licensed as zlib with one exception:
# SOURCE/platform/unix/ltmain.sh is public domain
License:        zlib and Public domain
Url:            http://love2d.org
Source0:        https://github.com/love2d/love/releases/download/%{version}/%{uname}-%{version}-linux-src.tar.gz
#From upstream:
#https://bitbucket.org/rude/love/commits/10f58e78bbfd82b681a45aeaf1177a765726bb31
Patch1:         love-0.10.2-luajit2.1.0beta3.patch

BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(physfs)
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
%{_mandir}/man1/%{name}.1*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{uname}-%{version}
%patch1 -p1


%build
%configure \
  --bindir=%{_gamesbindir} \
  --program-suffix=%{api} \
  --with-lua=luajit \
  --enable-gme \
  --disable-shared
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.a' -delete -o -name '*.la' -delete

# Rename to avoid conflicts with main `love` package.
mv %{buildroot}%{_datadir}/mime/packages/{%{uname},%{name}}.xml
mv %{buildroot}%{_datadir}/pixmaps/{%{uname},%{name}}.svg
mv %{buildroot}%{_iconsdir}/hicolor/scalable/mimetypes/application-x-{%{uname},%{name}}-game.svg

# Override with proper renames.
rm -f %{buildroot}%{_datadir}/applications/%{uname}.desktop
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=LÖVE %{version}
Comment=The unquestionably awesome 2D game engine
MimeType=application/x-%{name}-game;
Exec=%{_gamesbindir}/%{name} %f
Type=Application
Categories=Development;Game;
Terminal=false
Icon=%{name}
NoDisplay=true
EOF


%changelog
* Thu Oct 21 2021 Igor Vlasenko <viy@altlinux.org> 0.10.2-alt1_1
- compat version

