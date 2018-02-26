Name: sublib
Version: 0.9
Release: alt2.r375
Summary: library that eases the development of subtitling applications
License: GPL2
Group: System/Libraries
Url: http://sublib.sf.net/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.tar
#Sould be http://dl.sf.net/%name/%name-%version.zip

# Automatically added by buildreq on Sat May 17 2008
BuildRequires: libgcc mono-mcs

%description
SubLib is a library that eases the development of subtitling applications. It
supports the most common text-based subtitle formats and allows for subtitle
editing, conversion and synchronization.

SubLib is written in C# and can be used in platforms like Mono or .NET Framework.

%prep
%setup -q -n %name

%build
%autoreconf
%configure
%make_build

%install
chmod -x build/*.dll
%makeinstall_std

%files
%doc AUTHORS CREDITS ChangeLog NEWS README
%_libdir/%name
%_pkgconfigdir/%name.pc

%changelog
* Sat Mar 14 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.9-alt2.r375
- fresh SVN version

* Sat May 17 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.9-alt1
- 1st Sisyphus release
