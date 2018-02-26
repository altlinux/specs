
Summary: Extracts attachments out of mailpack format emails
Name: ripmime
Version: 1.4.0.9
Release: alt1
License: BSD
Group: Networking/Mail
Url: http://www.pldaniels.com/ripmime/
Packager: Alexey Shabalin <shaba@altlinux.org>
Source0: http://www.pldaniels.com/ripmime/%name-%version.tar.gz
Patch0: ripmime-1.4.0.9-shared.patch
BuildRequires: libripole-devel

%description
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

%package -n	lib%name
Summary: Shared %name library
Group: System/Libraries
Requires: libripole

%description -n	lib%name
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

This package provides the shared %name library.

%package -n	lib%name-devel
Summary: Development files for the %name library
Group: Development/C
Provides: %name-devel = %version
PreReq: lib%name = %version-%release
Requires: libripole-devel

%description -n	lib%name-devel
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com).

ripMIME has been written with one sole purpose in mind, to extract
the attached files out of a MIME encoded email package.

This package provides development files for the %name library.

%prep
%setup -n %name-%version
%patch0 -p1
#  rm -rf ripOLE

%build

%make \
    CFLAGS="$CFLAGS" \
    libdir=%_libdir

%install
%makeinstall

%files
%doc CHANGELOG CONTRIBUTORS INSTALL LICENSE README
%_bindir/*
%_mandir/man1/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc TODO
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/*.so
%_libdir/*.a

%changelog
* Thu Jul 02 2009 Alexey Shabalin <shaba@altlinux.ru> 1.4.0.9-alt1
- 1.4.0.9
- rewrite patch0 and specify a tag with `--tag'

* Fri Jul 20 2007 Alexey Shabalin <shaba@altlinux.ru> 1.4.0.7-alt2
- fix build on x86_64 (change %%make_install to %%makeinstall)

* Fri Jul 20 2007 Alexey Shabalin <shaba@altlinux.org> 1.4.0.7-alt1
- Initial build for ALTLinux
