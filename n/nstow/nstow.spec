Name: nstow
Version: 1.0
Release: alt1

Summary: nstow - manage software installation from the command-line
License: GPL
Group: System/Configuration/Packaging
Url: http://www.gnusto.com/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.ru>

%description
Nstow is a reimplementation of Bob Glickstein's stow package management
Perl script in C.

Nstow is a command-line software installation management tool.

%prep
%setup -q

%build
%configure
%make_build
%__make check || exit 1

%install
%make_install DESTDIR=%buildroot install

mv %buildroot%_bindir/stow %buildroot%_bindir/nstow
mv %buildroot%_man1dir/stow.1 %buildroot%_man1dir/nstow.1

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Sat May 06 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt1
- Initial build for Sisyphus
