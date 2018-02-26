Name: viewglob
Version: 2.0.4
Release: alt1

Summary: filesystem visualization add-on for Bash and Zsh
License: GPL
Group: Shells
Url: http://viewglob.sourceforge.net/

Source: http://download.sourceforge.net/viewglob/%name-%version.tar.gz
Packager: Ilya Mashkin <oddity@altlinux.ru>

AutoReqProv: yes, noshell

# Automatically added by buildreq2 on Пнд Авг 29 2005
BuildRequires: libgtk+2-devel

%description
Viewglob is a filesystem visualization add-on for Bash and Zsh. It tracks
the command line and environment of any number of interactive shells
(local and remote). A graphical display follows the currently active
terminal, listing the contents of directories relevant to its shell and
highlighting file selections and potential name completions dynamically.

%prep
%setup

%build
%configure --disable-dependency-tracking
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS NEWS README TODO ChangeLog 
%_libdir/%name

%changelog
* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Mon Aug 29 2005 Alex V. Myltsev <avm@altlinux.ru> 2.0.3-alt1
- New version.

* Tue Jun 14 2005 Alex V. Myltsev <avm@altlinux.ru> 2.0.2-alt1
- Initial build for ALT Linux.

