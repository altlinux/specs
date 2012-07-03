Name: yeahconsole
Summary: Turn an xterm into a gamelike console
Version: 0.3.4
Release: alt1
License: GPL
Group: Terminals
Source: http://phrat.de/%name-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>
Url: http://phrat.de

# Automatically added by buildreq on Sun Mar 02 2008
BuildRequires: libX11-devel

%description
YeahConsole turns an xterm into a gamelike console.
This means it will slide down from top of your screen if you hit a shortcut key.
(You will need xterm version 168 or higher to make this happen)

%prep
%setup

%build
cc %name.c -lX11 -o %name

%install
mkdir -p %buildroot%_bindir
install -s %name %buildroot%_bindir

%files
%doc README
%_bindir/%name

%changelog
* Sun Mar 02 2008 Fr. Br. George <george@altlinux.ru> 0.3.4-alt1
- Initial build

