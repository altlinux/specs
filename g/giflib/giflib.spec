%define _unpackaged_files_terminate_build 1
%define abiversion 7

Name: giflib
Version: 6.1.2
Release: alt1
Summary: A Library for Working with GIF Images.
License: MIT
Group: System/Libraries
Url: https://giflib.sourceforge.net/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
#CVE was fixed
#Patch1: alt-Clean-up-memory-better-at-end-of-run-CVE-2021-40633.patch

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
Conflicts: libgif-utils libgif-devel

%description -n %name-devel
Group: Development/C
Files for development with %name.

%prep
%setup
%autopatch -p1
sed -i '/PREFIX=/s,/usr/local,%prefix,' Makefile
# error: missing argument for "-Wl," switch
sed -i 's/$(LIBUTILMAJOR)/$(LIBUTILSOMAJOR)/' Makefile

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
%doc *.adoc TODO NEWS COPYING ChangeLog
%_bindir/*
%_libdir/*.so
%_docdir/%name/
%_man1dir/*.1*
%_man7dir/*.7*
%_includedir/gif_lib.h


%files -n lib%{name}_%{abiversion}
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%changelog
* Thu Mar 12 2026 Pavel Shilov <zerospirit@altlinux.org> 6.1.2-alt1
- Update to new version 6.1.2.

* Fri Feb 20 2026 Pavel Shilov <zerospirit@altlinux.org> 6.1.1-alt1
- 5.2.2 -> 6.1.1

* Fri Jul 25 2025 Pavel Shilov <zerospirit@altlinux.org> 5.2.2-alt2
- Add explicit Conflicts with packages to resolve file and symlink overlaps.

* Thu Jul 24 2025 Pavel Shilov <zerospirit@altlinux.org> 5.2.2-alt1.2
- Update based on upstream (Fixes: CVE-2021-40633)

* Wed Dec 11 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 5.2.2-alt1.1
- Fixed build for Elbrus

* Tue Oct 22 2024 Pavel Shilov <zerospirit@altlinux.org> 5.2.2-alt1
- initial build for Sisyphus
