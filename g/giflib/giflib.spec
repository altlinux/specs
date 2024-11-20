%define _unpackaged_files_terminate_build 1
%define abiversion 7

Name: giflib
Version: 5.2.2
Release: alt1
Summary: A Library for Working with GIF Images.
License: MIT
Group: System/Libraries
Url: https://www.scintilla.org/

Source0: %name-%version.tar

BuildRequires: libtool
BuildRequires: /usr/bin/convert

%description
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%package -n lib%{name}_%{abiversion}
Group: Development/C
Summary: A Library for Working with GIF Images

%description -n lib%{name}_%{abiversion}
This Library allows manipulating GIF Image files. Since the LZW patents
have expired, giflib can again be used instead of libungif.

%package -n %name-devel
Summary: Development package for %name
Group: Development/C
Requires:   pkgconfig

%description -n %name-devel
Group: Development/C
Files for development with %name.

%prep
%setup
sed -i '/PREFIX=/s,/usr/local,%prefix,' Makefile

%build
export CFLAGS="%optflags"
%make_build

%install
%makeinstall_std PREFIX="%_prefix" LIBDIR="%_libdir"
find %buildroot%_man1dir -name *.xml* -print -delete
find %buildroot -type f -name "*.la" -delete -print
find doc -name "Makefile*" -print -delete

# Install the manpages
mkdir -p %buildroot%_man1dir/
for i in doc/*.1; do
  install -pm 0644 $i %buildroot%_man1dir/
done

# Drop static library
rm -f %buildroot%_libdir/libgif.a

%files -n %name-devel
%doc README
%_bindir/*
%_libdir/*.so
%_man1dir/*.1*
%_includedir/gif_lib.h


%files -n lib%{name}_%{abiversion}
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%changelog
* Tue Oct 22 2024 Pavel Shilov <zerospirit@altlinux.org> 5.2.2-alt1
- initial build for Sisyphus
