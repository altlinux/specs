Name: untex
Version: 1.3
Release: alt1

Summary: untex - strip LaTeX comands from input
License: GPL
Group: Text tools

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.ru>

%description
Untex  removes  some  LaTeX commands from the files listed in the argu-
ments (or standard input) and prints the output to standard output.

%prep
%setup -q -c

%build
%make_build CFLAGS="%optflags"

%install
%__mkdir_p %buildroot%_bindir/
%__mkdir_p %buildroot%_man1dir/

%__install -p -m755 %name %buildroot%_bindir/
%__install -p -m644 %name.man %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Sat Apr 29 2006 Igor Zubkov <icesik@altlinux.ru> 1.3-alt1
- Initial build for Sisyphus
