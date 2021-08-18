Name:     sputnik-browser-preinstall
Version:  5.3.5672.0
Release:  alt1

Summary:  Preinstall packages and repository for install Sputnik Browser
License:  GPL
Group:    Other
Url:      http://altlinux.org

Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: x86_64

Requires: automake-common
Requires: binutils
Requires: emacs-base
Requires: gettext-tools
Requires: libdb4.7-devel
Requires: libgdbm-devel
Requires: libgdk-pixbuf-xlib
Requires: libpng12
Requires: libqt3
Requires: libqt3-settings
Requires: libqt4-core
Requires: libqt4-dbus
Requires: libqt4-gui
Requires: libqt4-network
Requires: libqt4-opengl
Requires: libqt4-sql
Requires: libqt4-svg
Requires: libqt4-xml
Requires: libtextstyle
Requires: lsb
Requires: lsb-core
Requires: lsb-cxx
Requires: lsb-desktop
Requires: lsb-init
Requires: lsb-languages
Requires: lsb-printing
Requires: lsb-release
Requires: m4
Requires: patch
Requires: pax
Requires: perl-Archive-Tar
Requires: perl-Attribute-Handlers
Requires: perl-CGI perl-CPAN
Requires: perl-CPAN-Meta-Requirements
Requires: perl-CPAN-Meta-YAML
Requires: perl-CPAN-Reporter
Requires: perl-Capture-Tiny
Requires: perl-Config-Tiny
Requires: perl-Devel-Autoflush
Requires: perl-File-HomeDir
Requires: perl-File-Which
Requires: perl-Filter-Simple
Requires: perl-HTTP-Tiny
Requires: perl-I18N-LangTags
Requires: perl-IO-String
Requires: perl-IO-Zlib
Requires: perl-IPC-Cmd
Requires: perl-JSON-PP
Requires: perl-Locale-Codes
Requires: perl-Locale-Maketext
Requires: perl-Locale-Maketext-Simple
Requires: perl-Math-BigInt
Requires: perl-Math-BigInt-FastCalc
Requires: perl-Math-BigRat
Requires: perl-Math-Complex
Requires: perl-Memoize
Requires: perl-Module-CoreList
Requires: perl-Module-Load
Requires: perl-Module-Load-Conditional
Requires: perl-Module-Metadata
Requires: perl-NEXT
Requires: perl-Net-Ping
Requires: perl-Params-Check
Requires: perl-Parse-CPAN-Meta
Requires: perl-Perl4-CoreLibs
Requires: perl-Pod-Checker
Requires: perl-Pod-Perldoc
Requires: perl-Probe-Perl
Requires: perl-Switch
Requires: perl-Term-ReadLine-Gnu
Requires: perl-Test-Reporter
Requires: perl-Text-Balanced
Requires: perl-Text-Soundex
Requires: perl-Text-Unidecode
Requires: perl-Unicode-Collate
Requires: perl-Unicode-Normalize
Requires: perl-bignum
Requires: perl-devel
Requires: perl-local-lib
Requires: perl-ph
Requires: perl-threads
Requires: perl-unicore
Requires: qt4-common
Requires: fsprot-control

%description
This metapackage requires all needed packages for install Sputnik
Browser to the ALT.

You can install the Sputnik Browser with the command:

 ./web-installer-5.3.5672.0.run

%post
if mountpoint -q /home; then
    if [ ! -f /_NEW_SYSTEM_ ]; then
	control homedir exec
    else
	echo "Don't forget to remove 'noexec' from" >&2
	echo "/home mount options in /etc/fstab!" >&2
	echo "Use command: control homedir exec" >&2
    fi
fi

%files

%changelog
* Thu Jul 22 2021 Anna Khrustova <khab@altlinux.org> 5.3.5672.0-alt1
- Update to 5.3.5672.0

* Mon Apr 15 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.2537.0-alt2
- Adapt for Sisyphus.

* Thu Apr 11 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.2537.0-alt0.M80C.1
- Backport to c8 branch.
- Provides menu and /usr/sbin/update-alternatives.

* Tue Apr 09 2019 Andrey Cherepanov <cas@altlinux.org> 4.1.2537.0-alt1
- Initial build.
