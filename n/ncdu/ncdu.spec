Name:           ncdu
Version:        1.7
Release:        alt1
Summary:        Text-based disk usage viewer

Group:          File tools
License:        MIT
URL:            http://dev.yorhel.nl/ncdu/
Source0:        http://dev.yorhel.nl/download/%name-%version.tar.gz

# Automatically added by buildreq on Fri Jun 11 2010
BuildRequires: libncursesw-devel

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog TODO
%_bindir/ncdu
%_man1dir/ncdu.1.gz

%changelog
* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 1.7-alt1
- update to new upstream version 1.7

* Fri Jun 11 2010 Mykola Grechukh <gns@altlinux.ru> 1.6-alt1
- first build for ALT Linux

* Sat Nov 28 2009 Richard Fearn <richardfearn@gmail.com> - 1.6-1
- update to new upstream version 1.6

%changelog
* Sun Jul 26 2009 Richard Fearn <richardfearn@gmail.com> - 1.5-1
- update to new upstream version 1.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.4-1
- new upstream version

* Fri Apr 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-2
- remove unnecessary Requires:
- use %%configure macro instead of ./configure
- don't need to mark man page as %%doc
- make package summary more descriptive

* Sat Mar  1 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-1
- initial package for Fedora
