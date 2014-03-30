Name: libtaginfo
Version: 0.2.1
Release: alt1
Summary: A library for reading media metadata (tags)

License: LGPLv2+
Url: https://bitbucket.org/shuerhaaken/libtaginfo
Source0: https://bitbucket.org/shuerhaaken/libtaginfo/downloads/libtaginfo-%version.tar.gz
Group: System/Libraries
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires: pkgconfig(taglib_c)
# for removing rpath
BuildRequires: chrpath gcc-c++

%description
TagInfo is a convenience wrapper for taglib with C and vala bindings.

Features are reading/writing fields like: Artist, Album, Title, Genre,
AlbumArtist, Comments, Disk number, Compilation flag, User labels,
Embedded Images, Lyrics, Audio properties (length, bitrate,
samplerate, channels ...), ...

%package devel
Summary: Development files for %name
Requires: %name%{?_isa} = %version-%release
Group: System/Libraries

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Remove RPATHs
chrpath --delete $RPM_BUILD_ROOT%_libdir/libtaginfo_c.so.0.0.0

%check
make check

%files
%doc COPYING AUTHORS NEWS README TODO
%_libdir/*.so.*

%files devel
%doc examples
%_includedir/*
%dir %_libdir/libtaginfo
%_libdir/libtaginfo/include
%_libdir/*.so
%_libdir/pkgconfig/libtaginfo*.pc
%dir %_datadir/vala
%dir %_datadir/vala/vapi
%_datadir/vala/vapi/libtaginfo_c.vapi

%changelog
* Sun Mar 30 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.1-alt1
- Build for Sisyphus

* Tue Dec 17 2013 Michel Salim <salimma@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Sat Apr 20 2013 Michel Salim <salimma@fedoraproject.org> - 0.1.6-1
- Update to 0.1.6

* Mon Apr  8 2013 Michel Salim <salimma@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Fri Mar 22 2013 Michel Salim <salimma@fedoraproject.org> - 0.1.4-2
- Enable tests

* Fri Mar 22 2013 Michel Salim <salimma@fedoraproject.org> - 0.1.4-1
- Update to 0.1.4

* Fri Mar  8 2013 Michel Salim <salimma@fedoraproject.org> - 0.1.3-1
- Initial package
