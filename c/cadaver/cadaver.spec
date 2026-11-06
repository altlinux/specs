%define _unpackaged_files_terminate_build 1

Name: cadaver
Version: 0.28
Release: alt1

Summary: Command-line WebDAV client
Summary(ru_RU.UTF-8): Консольный клиент WebDAV
License: %gpl2plus
Group: Networking/File transfer
Url: https://notroj.github.io/cadaver/
Vcs: https://github.com/notroj/cadaver

Source0: %name-%version.tar

BuildRequires: rpm-build-licenses
BuildRequires: libncurses-devel
BuildRequires: libneon-devel
BuildRequires: libneon-source
BuildRequires: libreadline-devel

%description
Cadaver is a command-line WebDAV client for Unix. It supports file
upload, download, on-screen display, in-place editing, namespace
operations (move/copy), collection creation and deletion, property
manipulation, and resource locking.

%prep
%setup
# configure.ac expects the neon source tree in neon/ (autoconf macros
# and src/Makefile.in); cadaver is still linked with system libneon.
mkdir -p neon
tar -xf %_usrsrc/libneon-source/neon-*.tar.gz -C neon --strip-components=1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
./autogen.sh
%configure --with-neon
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc FAQ NEWS README.md THANKS TODO
%doc --no-dereference COPYING
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Fri Nov 06 2026 Mikhail Nogin <joycap@altlinux.org> 0.28-alt1
- Updated to 0.28.
- Used neon macros from libneon-source instead of bundled submodule.
- Dropped obsolete patches (manpage hyphen, secure_getenv).
- Cleaned up spec and BuildRequires.

* Wed Dec 07 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.24-alt1
- New version

* Tue Jul 13 2021 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.23.3-alt6.git.4cbea82
- Fixed use of glibc secure_getenv.

* Wed Jun 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.23.3-alt5.git.4cbea82
- Rebuild with libneon 0.31

* Tue Feb 12 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.23.3-alt4
- Rebuild with readline7

* Sun Nov 24 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.3-alt3
- Rebuild with libneon 0.30

* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.3-alt2
- Fix remote args globbing (Closes: #26649)

* Sun Mar 20 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.3-alt1
- New version

* Mon Nov 23 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt3
- Rebuild with libneon-0.29.0-alt1

* Tue May 26 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt2
- Rebuild with libneon-0.28.4-alt1

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt1
- Initial build for ALT Linux Sisyphus

* Sat Dec 06 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.23.2-alt0.1
- Initial build
